# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import inspect
import logging
import os
import pkgutil
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from textwrap import dedent
from typing import Any, Callable, Dict, List, Optional, Set, Type, get_type_hints

from jinja2 import Environment, PackageLoader, Template
from typing_inspect import get_args, get_origin, is_literal_type

import hydra
from omegaconf import OmegaConf, ValidationError
from omegaconf._utils import (
    _is_union,
    _resolve_optional,
    get_dict_key_value_types,
    get_list_element_type,
    is_dict_annotation,
    is_list_annotation,
    is_structured_config,
)

from configen.config import Config, ConfigenConf, ModuleConf
from configen.utils import (
    collect_imports,
    convert_imports,
    is_tuple_annotation,
    type_str,
)

# Adding the current working directory to the PYTHONPATH to allow generation of code
# that is not installed properly
sys.path.append(os.getcwd())

log = logging.getLogger(__name__)

jinja_env = Environment(
    loader=PackageLoader("configen", "templates"),
    keep_trailing_newline=True,
    trim_blocks=True,
)
jinja_env.tests["empty"] = lambda x: x == inspect.Signature.empty


def init_config(conf_dir: str) -> None:
    log.info(f"Initializing config in '{conf_dir}'")

    path = Path(hydra.utils.to_absolute_path(conf_dir))
    path.mkdir(parents=True, exist_ok=True)
    file = path / "configen.yaml"
    if file.exists():
        sys.stderr.write(f"Config file '{file}' already exists\n")
        sys.exit(1)

    sample_config = pkgutil.get_data(__name__, "templates/sample_config.yaml")
    assert sample_config is not None
    file.write_bytes(sample_config)


def save(cfg: ConfigenConf, module: str, code: str) -> None:
    module_path = module.replace(".", "/")

    module_path_pattern = Template(cfg.module_path_pattern).render(module_path=module_path)
    path = Path(cfg.output_dir) / module_path_pattern
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(code)
    log.info(f"{module}.{module} -> {path}")


@dataclass
class Parameter:
    name: str
    type_str: str
    default: Optional[str]


@dataclass
class ClassInfo:
    module: str
    name: str
    parameters: List[Parameter]
    target: str


def is_incompatible(type_: Type[Any]) -> bool:

    opt = _resolve_optional(type_)
    # Unions are not supported (Except Optional)
    if not opt[0] and _is_union(type_):
        return True

    type_ = opt[1]
    if type_ in (type(None), tuple, list, dict):
        return False

    try:
        if is_list_annotation(type_):
            lt = get_list_element_type(type_)
            return is_incompatible(lt)
        if is_dict_annotation(type_):
            kvt = get_dict_key_value_types(type_)
            if not issubclass(kvt[0], (str, Enum)):
                return True
            return is_incompatible(kvt[1])
        if is_tuple_annotation(type_):
            return any(arg is not ... and is_incompatible(arg) for arg in type_.__args__)
        origin = get_origin(type_)
        # Callable isn't a class so the subsequent issubclass check would raise
        # a rype-error if called on it
        if isinstance(origin, Callable):
            return True
        if origin is type:
            args = get_args(type_)
            return bool(is_incompatible(args[0]))
    except ValidationError:
        return True

    if type_ is Any or issubclass(type_, (int, float, str, bool, Enum)):
        return False
    if is_structured_config(type_):
        try:
            OmegaConf.structured(type_)  # verify it's actually legal
        except ValidationError as e:
            log.debug(
                f"Failed to create DictConfig from ({type_.__name__}) : {e}, flagging as incompatible"
            )
            return True
        return False
    return True


def get_default_flags(module: ModuleConf) -> List[Parameter]:

    def_flags: List[Parameter] = []

    if module.default_flags._convert_ is not None:
        def_flags.append(
            Parameter(
                name="_convert_",
                type_str="str",
                default=f'"{module.default_flags._convert_.name}"',
            )
        )

    if module.default_flags._recursive_ is not None:
        def_flags.append(
            Parameter(
                name="_recursive_",
                type_str="bool",
                default=str(module.default_flags._recursive_),
            )
        )

    return def_flags


def generate_module(cfg: ConfigenConf, module: ModuleConf) -> str:
    classes_map: Dict[str, ClassInfo] = {}
    imports = set()
    string_imports: Set[str] = set()

    default_flags = get_default_flags(module)

    for class_name in module.classes:
        full_name = f"{module.name}.{class_name}"
        cls = hydra.utils.get_class(full_name)
        params: List[Parameter] = []
        params += default_flags
        resolved_hints = get_type_hints(cls.__init__)
        sig = inspect.signature(cls.__init__)

        for name, p in sig.parameters.items():
            # Skip self as an attribute.
            if name in ("self", "args", "kwargs"):
                continue
            type_ = type_cached = resolved_hints.get(name, p.annotation)
            default_ = p.default

            missing_value = default_ == sig.empty
            incompatible_value_type = not missing_value and is_incompatible(type(default_))
            missing_annotation_type = name not in resolved_hints
            incompatible_annotation_type = not missing_annotation_type and is_incompatible(type_)

            if isinstance(default_, Enum):
                module_name = getattr(default_, "__module__", None)
                if module_name is not None:  # Import required
                    import_name = default_.__class__.__name__
                    string_imports.add(f"from {module_name} import {import_name}")

            if is_literal_type(type_):
                values = get_args(type_)
                elem_type = type(values[0])
                if all(isinstance(value, elem_type) for value in values[1:]):
                    type_ = elem_type
                    incompatible_annotation_type = False

            if missing_annotation_type or incompatible_annotation_type:
                type_ = Any
                collect_imports(imports, Any)

            if not missing_value:
                if type_ == str or type(default_) == str:
                    default_ = f'"{default_}"'
                elif isinstance(default_, list):
                    default_ = f"field(default_factory=lambda: {default_})"
                elif isinstance(default_, dict):
                    default_ = f"field(default_factory=lambda: {default_})"

            missing_default = True if incompatible_value_type else missing_value
            collect_imports(imports, type_)

            if missing_default:
                default_ = "MISSING"
                string_imports.add("from omegaconf import MISSING")

            if isinstance(default_, Enum):
                default_ = Enum.__str__(default_)

            if incompatible_annotation_type:
                default_ = f"{default_}  # {type_str(type_cached)}"
            elif incompatible_value_type:
                default_ = f"{default_}  # {type_str(type(p.default))}"  # if not missing_value:

            params.append(
                Parameter(
                    name=name,
                    type_str=type_str(type_),
                    default=str(default_),
                )
            )
        classes_map[class_name] = ClassInfo(
            target=full_name,
            module=module.name,
            name=class_name,
            parameters=params,
        )

    template = jinja_env.get_template("module.j2")
    return template.render(
        imports=convert_imports(imports, string_imports),
        classes=module.classes,
        classes_map=classes_map,
        header=cfg.header,
    )


@hydra.main(config_path=None, config_name="configen_schema")
def main(cfg: Config):
    if cfg.init_config_dir is not None:
        init_config(cfg.init_config_dir)
        return

    if OmegaConf.is_missing(cfg.configen, "modules"):  # type: ignore
        log.error(
            dedent(
                """\
                Use --config-dir DIR --config-name NAME
                e.g:
                \tconfigen --config-dir conf --config-name configen
                If you have no config dir yet use init_config_dir=DIR to create an initial config dir.
                e.g:
                \tconfigen init_config_dir=conf
                """
            )
        )
        sys.exit(1)

    for module in cfg.configen.modules:
        code = generate_module(cfg=cfg.configen, module=module)
        save(cfg=cfg.configen, module=module.name, code=code)


if __name__ == "__main__":
    main()
