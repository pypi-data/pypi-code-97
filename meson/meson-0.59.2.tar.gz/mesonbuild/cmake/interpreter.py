# Copyright 2019 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This class contains the basic functionality needed to run any interpreter
# or an interpreter-based tool.

from .common import CMakeException, CMakeTarget, TargetOptions, CMakeConfiguration, language_map, backend_generator_map, cmake_get_generator_args, check_cmake_args
from .client import CMakeClient, RequestCMakeInputs, RequestConfigure, RequestCompute, RequestCodeModel, ReplyCMakeInputs, ReplyCodeModel
from .fileapi import CMakeFileAPI
from .executor import CMakeExecutor
from .toolchain import CMakeToolchain, CMakeExecScope
from .traceparser import CMakeTraceParser, CMakeGeneratorTarget
from .. import mlog, mesonlib
from ..mesonlib import MachineChoice, OrderedSet, version_compare, path_is_in_root, relative_to_if_possible, OptionKey
from ..mesondata import mesondata
from ..compilers.compilers import assembler_suffixes, lang_suffixes, header_suffixes, obj_suffixes, lib_suffixes, is_header
from ..programs import ExternalProgram
from ..coredata import FORBIDDEN_TARGET_NAMES
from enum import Enum
from functools import lru_cache
from pathlib import Path
import typing as T
import re
from os import environ

from ..mparser import (
    Token,
    BaseNode,
    CodeBlockNode,
    FunctionNode,
    ArrayNode,
    ArgumentNode,
    AssignmentNode,
    BooleanNode,
    StringNode,
    IdNode,
    IndexNode,
    MethodNode,
    NumberNode,
)


if T.TYPE_CHECKING:
    from .._typing import ImmutableListProtocol
    from ..build import Build
    from ..backend.backends import Backend
    from ..environment import Environment

TYPE_mixed        = T.Union[str, int, bool, Path, BaseNode]
TYPE_mixed_list   = T.Union[TYPE_mixed, T.Sequence[TYPE_mixed]]
TYPE_mixed_kwargs = T.Dict[str, TYPE_mixed_list]

# Disable all warnings automaticall enabled with --trace and friends
# See https://cmake.org/cmake/help/latest/variable/CMAKE_POLICY_WARNING_CMPNNNN.html
disable_policy_warnings = [
    'CMP0025',
    'CMP0047',
    'CMP0056',
    'CMP0060',
    'CMP0065',
    'CMP0066',
    'CMP0067',
    'CMP0082',
    'CMP0089',
    'CMP0102',
]

target_type_map = {
    'STATIC_LIBRARY': 'static_library',
    'MODULE_LIBRARY': 'shared_module',
    'SHARED_LIBRARY': 'shared_library',
    'EXECUTABLE': 'executable',
    'OBJECT_LIBRARY': 'static_library',
    'INTERFACE_LIBRARY': 'header_only'
}

skip_targets = ['UTILITY']

blacklist_compiler_flags = [
    '-Wall', '-Wextra', '-Weverything', '-Werror', '-Wpedantic', '-pedantic', '-w',
    '/W1', '/W2', '/W3', '/W4', '/Wall', '/WX', '/w',
    '/O1', '/O2', '/Ob', '/Od', '/Og', '/Oi', '/Os', '/Ot', '/Ox', '/Oy', '/Ob0',
    '/RTC1', '/RTCc', '/RTCs', '/RTCu',
    '/Z7', '/Zi', '/ZI',
]

blacklist_link_flags = [
    '/machine:x64', '/machine:x86', '/machine:arm', '/machine:ebc',
    '/debug', '/debug:fastlink', '/debug:full', '/debug:none',
    '/incremental',
]

blacklist_clang_cl_link_flags = ['/GR', '/EHsc', '/MDd', '/Zi', '/RTC1']

blacklist_link_libs = [
    'kernel32.lib',
    'user32.lib',
    'gdi32.lib',
    'winspool.lib',
    'shell32.lib',
    'ole32.lib',
    'oleaut32.lib',
    'uuid.lib',
    'comdlg32.lib',
    'advapi32.lib'
]

transfer_dependencies_from = ['header_only']

_cmake_name_regex = re.compile(r'[^_a-zA-Z0-9]')
def _sanitize_cmake_name(name: str) -> str:
    name = _cmake_name_regex.sub('_', name)
    if name in FORBIDDEN_TARGET_NAMES or name.startswith('meson'):
        name = 'cm_' + name
    return name

class OutputTargetMap:
    rm_so_version = re.compile(r'(\.[0-9]+)+$')

    def __init__(self, build_dir: Path):
        self.tgt_map   = {}          # type: T.Dict[str, T.Union['ConverterTarget', 'ConverterCustomTarget']]
        self.build_dir = build_dir

    def add(self, tgt: T.Union['ConverterTarget', 'ConverterCustomTarget']) -> None:
        def assign_keys(keys: T.List[str]) -> None:
            for i in [x for x in keys if x]:
                self.tgt_map[i] = tgt
        keys = [self._target_key(tgt.cmake_name)]
        if isinstance(tgt, ConverterTarget):
            keys += [tgt.full_name]
            keys += [self._rel_artifact_key(x) for x in tgt.artifacts]
            keys += [self._base_artifact_key(x) for x in tgt.artifacts]
        if isinstance(tgt, ConverterCustomTarget):
            keys += [self._rel_generated_file_key(x) for x in tgt.original_outputs]
            keys += [self._base_generated_file_key(x) for x in tgt.original_outputs]
        assign_keys(keys)

    def _return_first_valid_key(self, keys: T.List[str]) -> T.Optional[T.Union['ConverterTarget', 'ConverterCustomTarget']]:
        for i in keys:
            if i and i in self.tgt_map:
                return self.tgt_map[i]
        return None

    def target(self, name: str) -> T.Optional[T.Union['ConverterTarget', 'ConverterCustomTarget']]:
        return self._return_first_valid_key([self._target_key(name)])

    def executable(self, name: str) -> T.Optional['ConverterTarget']:
        tgt = self.target(name)
        if tgt is None or not isinstance(tgt, ConverterTarget):
            return None
        if tgt.meson_func() != 'executable':
            return None
        return tgt

    def artifact(self, name: str) -> T.Optional[T.Union['ConverterTarget', 'ConverterCustomTarget']]:
        keys = []
        candidates = [name, OutputTargetMap.rm_so_version.sub('', name)]
        for i in lib_suffixes:
            if not name.endswith('.' + i):
                continue
            new_name = name[:-len(i) - 1]
            new_name = OutputTargetMap.rm_so_version.sub('', new_name)
            candidates += [f'{new_name}.{i}']
        for i in candidates:
            keys += [self._rel_artifact_key(Path(i)), Path(i).name, self._base_artifact_key(Path(i))]
        return self._return_first_valid_key(keys)

    def generated(self, name: Path) -> T.Optional['ConverterCustomTarget']:
        res = self._return_first_valid_key([self._rel_generated_file_key(name), self._base_generated_file_key(name)])
        assert res is None or isinstance(res, ConverterCustomTarget)
        return res

    # Utility functions to generate local keys
    def _rel_path(self, fname: Path) -> T.Optional[Path]:
        try:
            return fname.resolve().relative_to(self.build_dir)
        except ValueError:
            pass
        return None

    def _target_key(self, tgt_name: str) -> str:
        return f'__tgt_{tgt_name}__'

    def _rel_generated_file_key(self, fname: Path) -> T.Optional[str]:
        path = self._rel_path(fname)
        return f'__relgen_{path.as_posix()}__' if path else None

    def _base_generated_file_key(self, fname: Path) -> str:
        return f'__gen_{fname.name}__'

    def _rel_artifact_key(self, fname: Path) -> T.Optional[str]:
        path = self._rel_path(fname)
        return f'__relart_{path.as_posix()}__' if path else None

    def _base_artifact_key(self, fname: Path) -> str:
        return f'__art_{fname.name}__'

class ConverterTarget:
    def __init__(self, target: CMakeTarget, env: 'Environment', for_machine: MachineChoice) -> None:
        self.env            = env
        self.for_machine    = for_machine
        self.artifacts      = target.artifacts
        self.src_dir        = target.src_dir
        self.build_dir      = target.build_dir
        self.name           = target.name
        self.cmake_name     = target.name
        self.full_name      = target.full_name
        self.type           = target.type
        self.install        = target.install
        self.install_dir    = None  # type: T.Optional[Path]
        self.link_libraries = target.link_libraries
        self.link_flags     = target.link_flags + target.link_lang_flags
        self.depends_raw    = []  # type: T.List[str]
        self.depends        = []  # type: T.List[T.Union[ConverterTarget, ConverterCustomTarget]]

        if target.install_paths:
            self.install_dir = target.install_paths[0]

        self.languages           = set() # type: T.Set[str]
        self.sources             = []  # type: T.List[Path]
        self.generated           = []  # type: T.List[Path]
        self.generated_ctgt      = []  # type: T.List[CustomTargetReference]
        self.includes            = []  # type: T.List[Path]
        self.sys_includes        = []  # type: T.List[Path]
        self.link_with           = []  # type: T.List[T.Union[ConverterTarget, ConverterCustomTarget]]
        self.object_libs         = []  # type: T.List[ConverterTarget]
        self.compile_opts        = {}  # type: T.Dict[str, T.List[str]]
        self.public_compile_opts = []  # type: T.List[str]
        self.pie                 = False

        # Project default override options (c_std, cpp_std, etc.)
        self.override_options = []  # type: T.List[str]

        # Convert the target name to a valid meson target name
        self.name = _sanitize_cmake_name(self.name)

        self.generated_raw = []  # type: T.List[Path]

        for i in target.files:
            languages    = set()  #  type: T.Set[str]
            src_suffixes = set()  #  type: T.Set[str]

            # Insert suffixes
            for j in i.sources:
                if not j.suffix:
                    continue
                src_suffixes.add(j.suffix[1:])

            # Determine the meson language(s)
            # Extract the default language from the explicit CMake field
            lang_cmake_to_meson = {val.lower(): key for key, val in language_map.items()}
            languages.add(lang_cmake_to_meson.get(i.language.lower(), 'c'))

            # Determine missing languages from the source suffixes
            for sfx in src_suffixes:
                for key, val in lang_suffixes.items():
                    if sfx in val:
                        languages.add(key)
                        break

            # Register the new languages and initialize the compile opts array
            for lang in languages:
                self.languages.add(lang)
                if lang not in self.compile_opts:
                    self.compile_opts[lang] = []

            # Add arguments, but avoid duplicates
            args = i.flags
            args += [f'-D{x}' for x in i.defines]
            for lang in languages:
                self.compile_opts[lang] += [x for x in args if x not in self.compile_opts[lang]]

            # Handle include directories
            self.includes += [x.path for x in i.includes if x.path not in self.includes and not x.isSystem]
            self.sys_includes += [x.path for x in i.includes if x.path not in self.sys_includes and x.isSystem]

            # Add sources to the right array
            if i.is_generated:
                self.generated_raw += i.sources
            else:
                self.sources += i.sources

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.name}>'

    std_regex = re.compile(r'([-]{1,2}std=|/std:v?|[-]{1,2}std:)(.*)')

    def postprocess(self, output_target_map: OutputTargetMap, root_src_dir: Path, subdir: Path, install_prefix: Path, trace: CMakeTraceParser) -> None:
        # Detect setting the C and C++ standard and do additional compiler args manipulation
        for i in ['c', 'cpp']:
            if i not in self.compile_opts:
                continue

            temp = []
            for j in self.compile_opts[i]:
                m = ConverterTarget.std_regex.match(j)
                ctgt = output_target_map.generated(Path(j))
                if m:
                    std = m.group(2)
                    supported = self._all_lang_stds(i)
                    if std not in supported:
                        mlog.warning(
                            'Unknown {0}_std "{1}" -> Ignoring. Try setting the project-'
                            'level {0}_std if build errors occur. Known '
                            '{0}_stds are: {2}'.format(i, std, ' '.join(supported)),
                            once=True
                        )
                        continue
                    self.override_options += [f'{i}_std={std}']
                elif j in ['-fPIC', '-fpic', '-fPIE', '-fpie']:
                    self.pie = True
                elif isinstance(ctgt, ConverterCustomTarget):
                    # Sometimes projects pass generated source files as compiler
                    # flags. Add these as generated sources to ensure that the
                    # corresponding custom target is run.2
                    self.generated_raw += [Path(j)]
                    temp += [j]
                elif j in blacklist_compiler_flags:
                    pass
                else:
                    temp += [j]

            self.compile_opts[i] = temp

        # Make sure to force enable -fPIC for OBJECT libraries
        if self.type.upper() == 'OBJECT_LIBRARY':
            self.pie = True

        # Use the CMake trace, if required
        tgt = trace.targets.get(self.cmake_name)
        if tgt:
            self.depends_raw = trace.targets[self.cmake_name].depends

            # TODO refactor this copy paste from CMakeDependency for future releases
            reg_is_lib = re.compile(r'^(-l[a-zA-Z0-9_]+|-l?pthread)$')
            to_process = [self.cmake_name]
            processed = []
            while len(to_process) > 0:
                curr = to_process.pop(0)

                if curr in processed or curr not in trace.targets:
                    continue

                tgt = trace.targets[curr]
                cfgs = []
                cfg = ''
                otherDeps = []
                libraries = []
                mlog.debug(str(tgt))

                if 'INTERFACE_INCLUDE_DIRECTORIES' in tgt.properties:
                    self.includes += [Path(x) for x in tgt.properties['INTERFACE_INCLUDE_DIRECTORIES'] if x]

                if 'INTERFACE_LINK_OPTIONS' in tgt.properties:
                    self.link_flags += [x for x in tgt.properties['INTERFACE_LINK_OPTIONS'] if x]

                if 'INTERFACE_COMPILE_DEFINITIONS' in tgt.properties:
                    self.public_compile_opts += ['-D' + re.sub('^-D', '', x) for x in tgt.properties['INTERFACE_COMPILE_DEFINITIONS'] if x]

                if 'INTERFACE_COMPILE_OPTIONS' in tgt.properties:
                    self.public_compile_opts += [x for x in tgt.properties['INTERFACE_COMPILE_OPTIONS'] if x]

                if 'IMPORTED_CONFIGURATIONS' in tgt.properties:
                    cfgs += [x for x in tgt.properties['IMPORTED_CONFIGURATIONS'] if x]
                    cfg = cfgs[0]

                if 'CONFIGURATIONS' in tgt.properties:
                    cfgs += [x for x in tgt.properties['CONFIGURATIONS'] if x]
                    cfg = cfgs[0]

                is_debug = self.env.coredata.get_option(OptionKey('debug'));
                if is_debug:
                    if 'DEBUG' in cfgs:
                        cfg = 'DEBUG'
                    elif 'RELEASE' in cfgs:
                        cfg = 'RELEASE'
                else:
                    if 'RELEASE' in cfgs:
                        cfg = 'RELEASE'

                if f'IMPORTED_IMPLIB_{cfg}' in tgt.properties:
                    libraries += [x for x in tgt.properties[f'IMPORTED_IMPLIB_{cfg}'] if x]
                elif 'IMPORTED_IMPLIB' in tgt.properties:
                    libraries += [x for x in tgt.properties['IMPORTED_IMPLIB'] if x]
                elif f'IMPORTED_LOCATION_{cfg}' in tgt.properties:
                    libraries += [x for x in tgt.properties[f'IMPORTED_LOCATION_{cfg}'] if x]
                elif 'IMPORTED_LOCATION' in tgt.properties:
                    libraries += [x for x in tgt.properties['IMPORTED_LOCATION'] if x]

                if 'LINK_LIBRARIES' in tgt.properties:
                    otherDeps += [x for x in tgt.properties['LINK_LIBRARIES'] if x]

                if 'INTERFACE_LINK_LIBRARIES' in tgt.properties:
                    otherDeps += [x for x in tgt.properties['INTERFACE_LINK_LIBRARIES'] if x]

                if f'IMPORTED_LINK_DEPENDENT_LIBRARIES_{cfg}' in tgt.properties:
                    otherDeps += [x for x in tgt.properties[f'IMPORTED_LINK_DEPENDENT_LIBRARIES_{cfg}'] if x]
                elif 'IMPORTED_LINK_DEPENDENT_LIBRARIES' in tgt.properties:
                    otherDeps += [x for x in tgt.properties['IMPORTED_LINK_DEPENDENT_LIBRARIES'] if x]

                for j in otherDeps:
                    if j in trace.targets:
                        to_process += [j]
                    elif reg_is_lib.match(j) or Path(j).exists():
                        libraries += [j]

                for j in libraries:
                    if j not in self.link_libraries:
                        self.link_libraries += [j]

                processed += [curr]
        elif self.type.upper() not in ['EXECUTABLE', 'OBJECT_LIBRARY']:
            mlog.warning('CMake: Target', mlog.bold(self.cmake_name), 'not found in CMake trace. This can lead to build errors')

        temp = []
        for i in self.link_libraries:
            # Let meson handle this arcane magic
            if ',-rpath,' in i:
                continue
            if not Path(i).is_absolute():
                link_with = output_target_map.artifact(i)
                if link_with:
                    self.link_with += [link_with]
                    continue

            temp += [i]
        self.link_libraries = temp

        # Filter out files that are not supported by the language
        supported = list(assembler_suffixes) + list(header_suffixes) + list(obj_suffixes)
        for i in self.languages:
            supported += list(lang_suffixes[i])
        supported = [f'.{x}' for x in supported]
        self.sources       = [x for x in self.sources       if any([x.name.endswith(y) for y in supported])]
        self.generated_raw = [x for x in self.generated_raw if any([x.name.endswith(y) for y in supported])]

        # Make paths relative
        def rel_path(x: Path, is_header: bool, is_generated: bool) -> T.Optional[Path]:
            if not x.is_absolute():
                x = self.src_dir / x
            x = x.resolve()
            assert x.is_absolute()
            if not x.exists() and not any([x.name.endswith(y) for y in obj_suffixes]) and not is_generated:
                if path_is_in_root(x, Path(self.env.get_build_dir()), resolve=True):
                    x.mkdir(parents=True, exist_ok=True)
                    return x.relative_to(Path(self.env.get_build_dir()) / subdir)
                else:
                    mlog.warning('CMake: path', mlog.bold(x.as_posix()), 'does not exist.')
                    mlog.warning(' --> Ignoring. This can lead to build errors.')
                    return None
            if x in trace.explicit_headers:
                return None
            if (
                    path_is_in_root(x, Path(self.env.get_source_dir()))
                    and not (
                        path_is_in_root(x, root_src_dir) or
                        path_is_in_root(x, Path(self.env.get_build_dir()))
                    )
                ):
                mlog.warning('CMake: path', mlog.bold(x.as_posix()), 'is inside the root project but', mlog.bold('not'), 'inside the subproject.')
                mlog.warning(' --> Ignoring. This can lead to build errors.')
                return None
            if path_is_in_root(x, Path(self.env.get_build_dir())) and is_header:
                return x.relative_to(Path(self.env.get_build_dir()) / subdir)
            if path_is_in_root(x, root_src_dir):
                return x.relative_to(root_src_dir)
            return x

        build_dir_rel = self.build_dir.relative_to(Path(self.env.get_build_dir()) / subdir)
        self.generated_raw = [rel_path(x, False, True) for x in self.generated_raw]
        self.includes = list(OrderedSet([rel_path(x, True, False) for x in OrderedSet(self.includes)] + [build_dir_rel]))
        self.sys_includes = list(OrderedSet([rel_path(x, True, False) for x in OrderedSet(self.sys_includes)]))
        self.sources = [rel_path(x, False, False) for x in self.sources]

        # Resolve custom targets
        for gen_file in self.generated_raw:
            ctgt = output_target_map.generated(gen_file)
            if ctgt:
                assert isinstance(ctgt, ConverterCustomTarget)
                ref = ctgt.get_ref(gen_file)
                assert isinstance(ref, CustomTargetReference) and ref.valid()
                self.generated_ctgt += [ref]
            elif gen_file is not None:
                self.generated += [gen_file]

        # Remove delete entries
        self.includes     = [x for x in self.includes     if x is not None]
        self.sys_includes = [x for x in self.sys_includes if x is not None]
        self.sources      = [x for x in self.sources      if x is not None]

        # Make sure '.' is always in the include directories
        if Path('.') not in self.includes:
            self.includes += [Path('.')]

        # make install dir relative to the install prefix
        if self.install_dir and self.install_dir.is_absolute():
            if path_is_in_root(self.install_dir, install_prefix):
                self.install_dir = self.install_dir.relative_to(install_prefix)

        # Remove blacklisted options and libs
        def check_flag(flag: str) -> bool:
            if flag.lower() in blacklist_link_flags or flag in blacklist_compiler_flags + blacklist_clang_cl_link_flags:
                return False
            if flag.startswith('/D'):
                return False
            return True

        self.link_libraries = [x for x in self.link_libraries if x.lower() not in blacklist_link_libs]
        self.link_flags = [x for x in self.link_flags if check_flag(x)]

        # Handle OSX frameworks
        def handle_frameworks(flags: T.List[str]) -> T.List[str]:
            res: T.List[str] = []
            for i in flags:
                p = Path(i)
                if not p.exists() or not p.name.endswith('.framework'):
                    res += [i]
                    continue
                res += ['-framework', p.stem]
            return res

        self.link_libraries = handle_frameworks(self.link_libraries)
        self.link_flags     = handle_frameworks(self.link_flags)

        # Handle explicit CMake add_dependency() calls
        for i in self.depends_raw:
            dep_tgt = output_target_map.target(i)
            if dep_tgt:
                self.depends.append(dep_tgt)

    def process_object_libs(self, obj_target_list: T.List['ConverterTarget'], linker_workaround: bool) -> None:
        # Try to detect the object library(s) from the generated input sources
        temp = [x for x in self.generated if any([x.name.endswith('.' + y) for y in obj_suffixes])]
        stem = [x.stem for x in temp]
        exts = self._all_source_suffixes()
        # Temp now stores the source filenames of the object files
        for i in obj_target_list:
            source_files = [x.name for x in i.sources + i.generated]
            for j in stem:
                # On some platforms (specifically looking at you Windows with vs20xy backend) CMake does
                # not produce object files with the format `foo.cpp.obj`, instead it skipps the language
                # suffix and just produces object files like `foo.obj`. Thus we have to do our best to
                # undo this step and guess the correct language suffix of the object file. This is done
                # by trying all language suffixes meson knows and checking if one of them fits.
                candidates = [j]  # type: T.List[str]
                if not any([j.endswith('.' + x) for x in exts]):
                    mlog.warning('Object files do not contain source file extensions, thus falling back to guessing them.', once=True)
                    candidates += [f'{j}.{x}' for x in exts]
                if any([x in source_files for x in candidates]):
                    if linker_workaround:
                        self._append_objlib_sources(i)
                    else:
                        self.includes += i.includes
                        self.includes = list(OrderedSet(self.includes))
                        self.object_libs += [i]
                    break

        # Filter out object files from the sources
        self.generated = [x for x in self.generated if not any([x.name.endswith('.' + y) for y in obj_suffixes])]

    def _append_objlib_sources(self, tgt: 'ConverterTarget') -> None:
        self.includes       += tgt.includes
        self.sources        += tgt.sources
        self.generated      += tgt.generated
        self.generated_ctgt += tgt.generated_ctgt
        self.includes        = list(OrderedSet(self.includes))
        self.sources         = list(OrderedSet(self.sources))
        self.generated       = list(OrderedSet(self.generated))
        self.generated_ctgt  = list(OrderedSet(self.generated_ctgt))

        # Inherit compiler arguments since they may be required for building
        for lang, opts in tgt.compile_opts.items():
            if lang not in self.compile_opts:
                self.compile_opts[lang] = []
            self.compile_opts[lang] += [x for x in opts if x not in self.compile_opts[lang]]

    @lru_cache(maxsize=None)
    def _all_source_suffixes(self) -> 'ImmutableListProtocol[str]':
        suffixes = []  # type: T.List[str]
        for exts in lang_suffixes.values():
            suffixes += [x for x in exts]
        return suffixes

    @lru_cache(maxsize=None)
    def _all_lang_stds(self, lang: str) -> 'ImmutableListProtocol[str]':
        try:
            res = self.env.coredata.options[OptionKey('std', machine=MachineChoice.BUILD, lang=lang)].choices
        except KeyError:
            return []

        # TODO: Get rid of this once we have proper typing for options
        assert isinstance(res, list)
        for i in res:
            assert isinstance(i, str)

        return res

    def process_inter_target_dependencies(self) -> None:
        # Move the dependencies from all transfer_dependencies_from to the target
        to_process = list(self.depends)
        processed = []
        new_deps = []
        for i in to_process:
            processed += [i]
            if isinstance(i, ConverterTarget) and i.meson_func() in transfer_dependencies_from:
                to_process += [x for x in i.depends if x not in processed]
            else:
                new_deps += [i]
        self.depends = list(OrderedSet(new_deps))

    def cleanup_dependencies(self) -> None:
        # Clear the dependencies from targets that where moved from
        if self.meson_func() in transfer_dependencies_from:
            self.depends = []

    def meson_func(self) -> str:
        return target_type_map.get(self.type.upper())

    def log(self) -> None:
        mlog.log('Target', mlog.bold(self.name), f'({self.cmake_name})')
        mlog.log('  -- artifacts:      ', mlog.bold(str(self.artifacts)))
        mlog.log('  -- full_name:      ', mlog.bold(self.full_name))
        mlog.log('  -- type:           ', mlog.bold(self.type))
        mlog.log('  -- install:        ', mlog.bold('true' if self.install else 'false'))
        mlog.log('  -- install_dir:    ', mlog.bold(self.install_dir.as_posix() if self.install_dir else ''))
        mlog.log('  -- link_libraries: ', mlog.bold(str(self.link_libraries)))
        mlog.log('  -- link_with:      ', mlog.bold(str(self.link_with)))
        mlog.log('  -- object_libs:    ', mlog.bold(str(self.object_libs)))
        mlog.log('  -- link_flags:     ', mlog.bold(str(self.link_flags)))
        mlog.log('  -- languages:      ', mlog.bold(str(self.languages)))
        mlog.log('  -- includes:       ', mlog.bold(str(self.includes)))
        mlog.log('  -- sys_includes:   ', mlog.bold(str(self.sys_includes)))
        mlog.log('  -- sources:        ', mlog.bold(str(self.sources)))
        mlog.log('  -- generated:      ', mlog.bold(str(self.generated)))
        mlog.log('  -- generated_ctgt: ', mlog.bold(str(self.generated_ctgt)))
        mlog.log('  -- pie:            ', mlog.bold('true' if self.pie else 'false'))
        mlog.log('  -- override_opts:  ', mlog.bold(str(self.override_options)))
        mlog.log('  -- depends:        ', mlog.bold(str(self.depends)))
        mlog.log('  -- options:')
        for key, val in self.compile_opts.items():
            mlog.log('    -', key, '=', mlog.bold(str(val)))

class CustomTargetReference:
    def __init__(self, ctgt: 'ConverterCustomTarget', index: int) -> None:
        self.ctgt = ctgt    # type: ConverterCustomTarget
        self.index = index  # type: int

    def __repr__(self) -> str:
        if self.valid():
            return '<{}: {} [{}]>'.format(self.__class__.__name__, self.ctgt.name, self.ctgt.outputs[self.index])
        else:
            return f'<{self.__class__.__name__}: INVALID REFERENCE>'

    def valid(self) -> bool:
        return self.ctgt is not None and self.index >= 0

    def filename(self) -> str:
        return self.ctgt.outputs[self.index]

class ConverterCustomTarget:
    tgt_counter = 0  # type: int
    out_counter = 0  # type: int

    def __init__(self, target: CMakeGeneratorTarget, env: 'Environment', for_machine: MachineChoice) -> None:
        assert target.current_bin_dir is not None
        assert target.current_src_dir is not None
        self.name = target.name
        if not self.name:
            self.name = f'custom_tgt_{ConverterCustomTarget.tgt_counter}'
            ConverterCustomTarget.tgt_counter += 1
        self.cmake_name       = str(self.name)
        self.original_outputs = list(target.outputs)
        self.outputs          = [x.name for x in self.original_outputs]
        self.conflict_map     = {}                      # type: T.Dict[str, str]
        self.command          = []                      # type: T.List[T.List[T.Union[str, ConverterTarget]]]
        self.working_dir      = target.working_dir
        self.depends_raw      = target.depends
        self.inputs           = []                      # type: T.List[T.Union[str, CustomTargetReference]]
        self.depends          = []                      # type: T.List[T.Union[ConverterTarget, ConverterCustomTarget]]
        self.current_bin_dir  = target.current_bin_dir  # type: Path
        self.current_src_dir  = target.current_src_dir  # type: Path
        self.env              = env
        self.for_machine      = for_machine
        self._raw_target      = target

        # Convert the target name to a valid meson target name
        self.name = _sanitize_cmake_name(self.name)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.name} {self.outputs}>'

    def postprocess(self, output_target_map: OutputTargetMap, root_src_dir: Path, all_outputs: T.List[str], trace: CMakeTraceParser) -> None:
        # Default the working directory to ${CMAKE_CURRENT_BINARY_DIR}
        if self.working_dir is None:
            self.working_dir = self.current_bin_dir

        # relative paths in the working directory are always relative
        # to ${CMAKE_CURRENT_BINARY_DIR}
        if not self.working_dir.is_absolute():
            self.working_dir = self.current_bin_dir / self.working_dir

        # Modify the original outputs if they are relative. Again,
        # relative paths are relative to ${CMAKE_CURRENT_BINARY_DIR}
        def ensure_absolute(x: Path) -> Path:
            if x.is_absolute():
                return x
            else:
                return self.current_bin_dir / x
        self.original_outputs = [ensure_absolute(x) for x in self.original_outputs]

        # Ensure that there is no duplicate output in the project so
        # that meson can handle cases where the same filename is
        # generated in multiple directories
        temp_outputs = []  # type: T.List[str]
        for i in self.outputs:
            if i in all_outputs:
                old = str(i)
                i = f'c{ConverterCustomTarget.out_counter}_{i}'
                ConverterCustomTarget.out_counter += 1
                self.conflict_map[old] = i
            all_outputs += [i]
            temp_outputs += [i]
        self.outputs = temp_outputs

        # Check if the command is a build target
        commands = []  # type: T.List[T.List[T.Union[str, ConverterTarget]]]
        for curr_cmd in self._raw_target.command:
            assert(isinstance(curr_cmd, list))
            cmd = []  # type: T.List[T.Union[str, ConverterTarget]]

            for j in curr_cmd:
                if not j:
                    continue
                target = output_target_map.executable(j)
                if target:
                    # When cross compiling, binaries have to be executed with an exe_wrapper (for instance wine for mingw-w64)
                    if self.env.exe_wrapper is not None and self.env.properties[self.for_machine].get_cmake_use_exe_wrapper():
                        assert isinstance(self.env.exe_wrapper, ExternalProgram)
                        cmd += self.env.exe_wrapper.get_command()
                    cmd += [target]
                    continue
                elif j in trace.targets:
                    trace_tgt = trace.targets[j]
                    if trace_tgt.type == 'EXECUTABLE' and 'IMPORTED_LOCATION' in trace_tgt.properties:
                        cmd += trace_tgt.properties['IMPORTED_LOCATION']
                        continue
                    mlog.debug(f'CMake: Found invalid CMake target "{j}" --> ignoring \n{trace_tgt}')

                # Fallthrough on error
                cmd += [j]

            commands += [cmd]
        self.command = commands

        # If the custom target does not declare any output, create a dummy
        # one that can be used as dependency.
        if not self.outputs:
            self.outputs = [self.name + '.h']

        # Check dependencies and input files
        for i in self.depends_raw:
            if not i:
                continue
            raw = Path(i)
            art = output_target_map.artifact(i)
            tgt = output_target_map.target(i)
            gen = output_target_map.generated(raw)

            rel_to_root = None
            try:
                rel_to_root = raw.relative_to(root_src_dir)
            except ValueError:
                rel_to_root = None

            # First check for existing files. Only then check for existing
            # targets, etc. This reduces the chance of misdetecting input files
            # as outputs from other targets.
            # See https://github.com/mesonbuild/meson/issues/6632
            if not raw.is_absolute() and (self.current_src_dir / raw).exists():
                self.inputs += [(self.current_src_dir / raw).relative_to(root_src_dir).as_posix()]
            elif raw.is_absolute() and raw.exists() and rel_to_root is not None:
                self.inputs += [rel_to_root.as_posix()]
            elif art:
                self.depends += [art]
            elif tgt:
                self.depends += [tgt]
            elif gen:
                ctgt_ref = gen.get_ref(raw)
                assert ctgt_ref is not None
                self.inputs += [ctgt_ref]

    def process_inter_target_dependencies(self) -> None:
        # Move the dependencies from all transfer_dependencies_from to the target
        to_process = list(self.depends)
        processed = []
        new_deps = []
        for i in to_process:
            processed += [i]
            if isinstance(i, ConverterTarget) and i.meson_func() in transfer_dependencies_from:
                to_process += [x for x in i.depends if x not in processed]
            else:
                new_deps += [i]
        self.depends = list(OrderedSet(new_deps))

    def get_ref(self, fname: Path) -> T.Optional[CustomTargetReference]:
        name = fname.name
        try:
            if name in self.conflict_map:
                name = self.conflict_map[name]
            idx = self.outputs.index(name)
            return CustomTargetReference(self, idx)
        except ValueError:
            return None

    def log(self) -> None:
        mlog.log('Custom Target', mlog.bold(self.name), f'({self.cmake_name})')
        mlog.log('  -- command:      ', mlog.bold(str(self.command)))
        mlog.log('  -- outputs:      ', mlog.bold(str(self.outputs)))
        mlog.log('  -- conflict_map: ', mlog.bold(str(self.conflict_map)))
        mlog.log('  -- working_dir:  ', mlog.bold(str(self.working_dir)))
        mlog.log('  -- depends_raw:  ', mlog.bold(str(self.depends_raw)))
        mlog.log('  -- inputs:       ', mlog.bold(str(self.inputs)))
        mlog.log('  -- depends:      ', mlog.bold(str(self.depends)))

class CMakeAPI(Enum):
    SERVER = 1
    FILE = 2

class CMakeInterpreter:
    def __init__(self, build: 'Build', subdir: Path, src_dir: Path, install_prefix: Path, env: 'Environment', backend: 'Backend'):
        self.build          = build
        self.subdir         = subdir
        self.src_dir        = src_dir
        self.build_dir_rel  = subdir / '__CMake_build'
        self.build_dir      = Path(env.get_build_dir()) / self.build_dir_rel
        self.install_prefix = install_prefix
        self.env            = env
        self.for_machine    = MachineChoice.HOST # TODO make parameter
        self.backend_name   = backend.name
        self.linkers        = set()  # type: T.Set[str]
        self.cmake_api      = CMakeAPI.SERVER
        self.client         = CMakeClient(self.env)
        self.fileapi        = CMakeFileAPI(self.build_dir)

        # Raw CMake results
        self.bs_files          = []    # type: T.List[Path]
        self.codemodel_configs = None  # type: T.Optional[T.List[CMakeConfiguration]]
        self.raw_trace         = None  # type: T.Optional[str]

        # Analysed data
        self.project_name      = ''
        self.languages         = []  # type: T.List[str]
        self.targets           = []  # type: T.List[ConverterTarget]
        self.custom_targets    = []  # type: T.List[ConverterCustomTarget]
        self.trace             = CMakeTraceParser('', Path('.'))  # Will be replaced in analyse
        self.output_target_map = OutputTargetMap(self.build_dir)

        # Generated meson data
        self.generated_targets = {}  # type: T.Dict[str, T.Dict[str, T.Optional[str]]]
        self.internal_name_map = {}  # type: T.Dict[str, str]

        # Do some special handling for object libraries for certain configurations
        self._object_lib_workaround = False
        if self.backend_name.startswith('vs'):
            for comp in self.env.coredata.compilers[self.for_machine].values():
                if comp.get_linker_id() == 'link':
                    self._object_lib_workaround = True
                    break

    def configure(self, extra_cmake_options: T.List[str]) -> CMakeExecutor:
        # Find CMake
        # TODO: Using MachineChoice.BUILD should always be correct here, but also evaluate the use of self.for_machine
        cmake_exe = CMakeExecutor(self.env, '>=3.7', MachineChoice.BUILD)
        if not cmake_exe.found():
            raise CMakeException('Unable to find CMake')
        self.trace = CMakeTraceParser(cmake_exe.version(), self.build_dir, permissive=True)

        preload_file = mesondata['cmake/data/preload.cmake'].write_to_private(self.env)
        toolchain = CMakeToolchain(cmake_exe, self.env, self.for_machine, CMakeExecScope.SUBPROJECT, self.build_dir, preload_file)
        toolchain_file = toolchain.write()

        # TODO: drop this check once the deprecated `cmake_args` kwarg is removed
        extra_cmake_options = check_cmake_args(extra_cmake_options)

        cmake_args = []
        cmake_args += cmake_get_generator_args(self.env)
        cmake_args += [f'-DCMAKE_INSTALL_PREFIX={self.install_prefix}']
        cmake_args += extra_cmake_options
        trace_args = self.trace.trace_args()
        cmcmp_args = [f'-DCMAKE_POLICY_WARNING_{x}=OFF' for x in disable_policy_warnings]

        if version_compare(cmake_exe.version(), '>=3.14'):
            self.cmake_api = CMakeAPI.FILE
            self.fileapi.setup_request()

        # Run CMake
        mlog.log()
        with mlog.nested():
            mlog.log('Configuring the build directory with', mlog.bold('CMake'), 'version', mlog.cyan(cmake_exe.version()))
            mlog.log(mlog.bold('Running CMake with:'), ' '.join(cmake_args))
            mlog.log(mlog.bold('  - build directory:         '), self.build_dir.as_posix())
            mlog.log(mlog.bold('  - source directory:        '), self.src_dir.as_posix())
            mlog.log(mlog.bold('  - toolchain file:          '), toolchain_file.as_posix())
            mlog.log(mlog.bold('  - preload file:            '), preload_file.as_posix())
            mlog.log(mlog.bold('  - trace args:              '), ' '.join(trace_args))
            mlog.log(mlog.bold('  - disabled policy warnings:'), '[{}]'.format(', '.join(disable_policy_warnings)))
            mlog.log()
            self.build_dir.mkdir(parents=True, exist_ok=True)
            os_env = environ.copy()
            os_env['LC_ALL'] = 'C'
            final_args = cmake_args + trace_args + cmcmp_args + toolchain.get_cmake_args() + [self.src_dir.as_posix()]

            cmake_exe.set_exec_mode(print_cmout=True, always_capture_stderr=self.trace.requires_stderr())
            rc, _, self.raw_trace = cmake_exe.call(final_args, self.build_dir, env=os_env, disable_cache=True)

        mlog.log()
        h = mlog.green('SUCCEEDED') if rc == 0 else mlog.red('FAILED')
        mlog.log('CMake configuration:', h)
        if rc != 0:
            raise CMakeException('Failed to configure the CMake subproject')

        return cmake_exe

    def initialise(self, extra_cmake_options: T.List[str]) -> None:
        # Run configure the old way because doing it
        # with the server doesn't work for some reason
        # Additionally, the File API requires a configure anyway
        cmake_exe = self.configure(extra_cmake_options)

        # Continue with the file API If supported
        if self.cmake_api is CMakeAPI.FILE:
            # Parse the result
            self.fileapi.load_reply()

            # Load the buildsystem file list
            cmake_files = self.fileapi.get_cmake_sources()
            self.bs_files = [x.file for x in cmake_files if not x.is_cmake and not x.is_temp]
            self.bs_files = [relative_to_if_possible(x, Path(self.env.get_source_dir())) for x in self.bs_files]
            self.bs_files = [x for x in self.bs_files if not path_is_in_root(x, Path(self.env.get_build_dir()), resolve=True)]
            self.bs_files = list(OrderedSet(self.bs_files))

            # Load the codemodel configurations
            self.codemodel_configs = self.fileapi.get_cmake_configurations()
            return

        with self.client.connect(cmake_exe):
            generator = backend_generator_map[self.backend_name]
            self.client.do_handshake(self.src_dir, self.build_dir, generator, 1)

            # Do a second configure to initialise the server
            self.client.query_checked(RequestConfigure(), 'CMake server configure')

            # Generate the build system files
            self.client.query_checked(RequestCompute(), 'Generating build system files')

            # Get CMake build system files
            bs_reply = self.client.query_checked(RequestCMakeInputs(), 'Querying build system files')
            assert isinstance(bs_reply, ReplyCMakeInputs)

            # Now get the CMake code model
            cm_reply = self.client.query_checked(RequestCodeModel(), 'Querying the CMake code model')
            assert isinstance(cm_reply, ReplyCodeModel)

        src_dir = bs_reply.src_dir
        self.bs_files = [x.file for x in bs_reply.build_files if not x.is_cmake and not x.is_temp]
        self.bs_files = [relative_to_if_possible(src_dir / x, Path(self.env.get_source_dir()), resolve=True) for x in self.bs_files]
        self.bs_files = [x for x in self.bs_files if not path_is_in_root(x, Path(self.env.get_build_dir()), resolve=True)]
        self.bs_files = list(OrderedSet(self.bs_files))
        self.codemodel_configs = cm_reply.configs

    def analyse(self) -> None:
        if self.codemodel_configs is None:
            raise CMakeException('CMakeInterpreter was not initialized')

        # Clear analyser data
        self.project_name = ''
        self.languages = []
        self.targets = []
        self.custom_targets = []

        # Parse the trace
        self.trace.parse(self.raw_trace)

        # Find all targets
        added_target_names = []  # type: T.List[str]
        for i_0 in self.codemodel_configs:
            for j_0 in i_0.projects:
                if not self.project_name:
                    self.project_name = j_0.name
                for k_0 in j_0.targets:
                    # Avoid duplicate targets from different configurations and known
                    # dummy CMake internal target types
                    if k_0.type not in skip_targets and k_0.name not in added_target_names:
                        added_target_names += [k_0.name]
                        self.targets += [ConverterTarget(k_0, self.env, self.for_machine)]

        # Add interface targets from trace, if not already present.
        # This step is required because interface targets were removed from
        # the CMake file API output.
        api_target_name_list = [x.name for x in self.targets]
        for i_1 in self.trace.targets.values():
            if i_1.type != 'INTERFACE' or i_1.name in api_target_name_list or i_1.imported:
                continue
            dummy = CMakeTarget({
                'name': i_1.name,
                'type': 'INTERFACE_LIBRARY',
                'sourceDirectory': self.src_dir,
                'buildDirectory': self.build_dir,
            })
            self.targets += [ConverterTarget(dummy, self.env, self.for_machine)]

        for i_2 in self.trace.custom_targets:
            self.custom_targets += [ConverterCustomTarget(i_2, self.env, self.for_machine)]

        # generate the output_target_map
        for i_3 in [*self.targets, *self.custom_targets]:
            assert isinstance(i_3, (ConverterTarget, ConverterCustomTarget))
            self.output_target_map.add(i_3)

        # First pass: Basic target cleanup
        object_libs = []
        custom_target_outputs = []  # type: T.List[str]
        for ctgt in self.custom_targets:
            ctgt.postprocess(self.output_target_map, self.src_dir, custom_target_outputs, self.trace)
        for tgt in self.targets:
            tgt.postprocess(self.output_target_map, self.src_dir, self.subdir, self.install_prefix, self.trace)
            if tgt.type == 'OBJECT_LIBRARY':
                object_libs += [tgt]
            self.languages += [x for x in tgt.languages if x not in self.languages]

        # Second pass: Detect object library dependencies
        for tgt in self.targets:
            tgt.process_object_libs(object_libs, self._object_lib_workaround)

        # Third pass: Reassign dependencies to avoid some loops
        for tgt in self.targets:
            tgt.process_inter_target_dependencies()
        for ctgt in self.custom_targets:
            ctgt.process_inter_target_dependencies()

        # Fourth pass: Remove rassigned dependencies
        for tgt in self.targets:
            tgt.cleanup_dependencies()

        mlog.log('CMake project', mlog.bold(self.project_name), 'has', mlog.bold(str(len(self.targets) + len(self.custom_targets))), 'build targets.')

    def pretend_to_be_meson(self, options: TargetOptions) -> CodeBlockNode:
        if not self.project_name:
            raise CMakeException('CMakeInterpreter was not analysed')

        def token(tid: str = 'string', val: TYPE_mixed = '') -> Token:
            return Token(tid, self.subdir.as_posix(), 0, 0, 0, None, val)

        def string(value: str) -> StringNode:
            return StringNode(token(val=value))

        def id_node(value: str) -> IdNode:
            return IdNode(token(val=value))

        def number(value: int) -> NumberNode:
            return NumberNode(token(val=value))

        def nodeify(value: TYPE_mixed_list) -> BaseNode:
            if isinstance(value, str):
                return string(value)
            if isinstance(value, Path):
                return string(value.as_posix())
            elif isinstance(value, bool):
                return BooleanNode(token(val=value))
            elif isinstance(value, int):
                return number(value)
            elif isinstance(value, list):
                return array(value)
            elif isinstance(value, BaseNode):
                return value
            raise RuntimeError('invalid type of value: {} ({})'.format(type(value).__name__, str(value)))

        def indexed(node: BaseNode, index: int) -> IndexNode:
            return IndexNode(node, nodeify(index))

        def array(elements: TYPE_mixed_list) -> ArrayNode:
            args = ArgumentNode(token())
            if not isinstance(elements, list):
                elements = [args]
            args.arguments += [nodeify(x) for x in elements if x is not None]
            return ArrayNode(args, 0, 0, 0, 0)

        def function(name: str, args: T.Optional[TYPE_mixed_list] = None, kwargs: T.Optional[TYPE_mixed_kwargs] = None) -> FunctionNode:
            args = [] if args is None else args
            kwargs = {} if kwargs is None else kwargs
            args_n = ArgumentNode(token())
            if not isinstance(args, list):
                assert isinstance(args, (str, int, bool, Path, BaseNode))
                args = [args]
            args_n.arguments = [nodeify(x) for x in args if x is not None]
            args_n.kwargs = {id_node(k): nodeify(v) for k, v in kwargs.items() if v is not None}
            func_n = FunctionNode(self.subdir.as_posix(), 0, 0, 0, 0, name, args_n)
            return func_n

        def method(obj: BaseNode, name: str, args: T.Optional[TYPE_mixed_list] = None, kwargs: T.Optional[TYPE_mixed_kwargs] = None) -> MethodNode:
            args = [] if args is None else args
            kwargs = {} if kwargs is None else kwargs
            args_n = ArgumentNode(token())
            if not isinstance(args, list):
                assert isinstance(args, (str, int, bool, Path, BaseNode))
                args = [args]
            args_n.arguments = [nodeify(x) for x in args if x is not None]
            args_n.kwargs = {id_node(k): nodeify(v) for k, v in kwargs.items() if v is not None}
            return MethodNode(self.subdir.as_posix(), 0, 0, obj, name, args_n)

        def assign(var_name: str, value: BaseNode) -> AssignmentNode:
            return AssignmentNode(self.subdir.as_posix(), 0, 0, var_name, value)

        # Generate the root code block and the project function call
        root_cb = CodeBlockNode(token())
        root_cb.lines += [function('project', [self.project_name] + self.languages)]

        # Add the run script for custom commands

        # Add the targets
        processing = []   # type: T.List[str]
        processed  = {}   # type: T.Dict[str, T.Dict[str, T.Optional[str]]]
        name_map   = {}   # type: T.Dict[str, str]

        def extract_tgt(tgt: T.Union[ConverterTarget, ConverterCustomTarget, CustomTargetReference]) -> IdNode:
            tgt_name = None
            if isinstance(tgt, (ConverterTarget, ConverterCustomTarget)):
                tgt_name = tgt.name
            elif isinstance(tgt, CustomTargetReference):
                tgt_name = tgt.ctgt.name
            assert(tgt_name is not None and tgt_name in processed)
            res_var = processed[tgt_name]['tgt']
            return id_node(res_var) if res_var else None

        def detect_cycle(tgt: T.Union[ConverterTarget, ConverterCustomTarget]) -> None:
            if tgt.name in processing:
                raise CMakeException('Cycle in CMake inputs/dependencies detected')
            processing.append(tgt.name)

        def resolve_ctgt_ref(ref: CustomTargetReference) -> T.Union[IdNode, IndexNode]:
            tgt_var = extract_tgt(ref)
            if len(ref.ctgt.outputs) == 1:
                return tgt_var
            else:
                return indexed(tgt_var, ref.index)

        def process_target(tgt: ConverterTarget) -> None:
            detect_cycle(tgt)

            # First handle inter target dependencies
            link_with           = []  # type: T.List[IdNode]
            objec_libs          = []  # type: T.List[IdNode]
            sources             = []  # type: T.List[Path]
            generated           = []  # type: T.List[T.Union[IdNode, IndexNode]]
            generated_filenames = []  # type: T.List[str]
            custom_targets      = []  # type: T.List[ConverterCustomTarget]
            dependencies        = []  # type: T.List[IdNode]
            for i in tgt.link_with:
                assert(isinstance(i, ConverterTarget))
                if i.name not in processed:
                    process_target(i)
                link_with += [extract_tgt(i)]
            for i in tgt.object_libs:
                assert(isinstance(i, ConverterTarget))
                if i.name not in processed:
                    process_target(i)
                objec_libs += [extract_tgt(i)]
            for i in tgt.depends:
                if not isinstance(i, ConverterCustomTarget):
                    continue
                if i.name not in processed:
                    process_custom_target(i)
                dependencies += [extract_tgt(i)]

            # Generate the source list and handle generated sources
            sources += tgt.sources
            sources += tgt.generated

            for ctgt_ref in tgt.generated_ctgt:
                ctgt = ctgt_ref.ctgt
                if ctgt.name not in processed:
                    process_custom_target(ctgt)
                generated += [resolve_ctgt_ref(ctgt_ref)]
                generated_filenames += [ctgt_ref.filename()]
                if ctgt not in custom_targets:
                    custom_targets += [ctgt]

            # Add all header files from all used custom targets. This
            # ensures that all custom targets are built before any
            # sources of the current target are compiled and thus all
            # header files are present. This step is necessary because
            # CMake always ensures that a custom target is executed
            # before another target if at least one output is used.
            for ctgt in custom_targets:
                for j in ctgt.outputs:
                    if not is_header(j) or j in generated_filenames:
                        continue

                    generated += [resolve_ctgt_ref(ctgt.get_ref(Path(j)))]
                    generated_filenames += [j]

            # Determine the meson function to use for the build target
            tgt_func = tgt.meson_func()
            if not tgt_func:
                raise CMakeException(f'Unknown target type "{tgt.type}"')

            # Determine the variable names
            inc_var = f'{tgt.name}_inc'
            dir_var = f'{tgt.name}_dir'
            sys_var = f'{tgt.name}_sys'
            src_var = f'{tgt.name}_src'
            dep_var = f'{tgt.name}_dep'
            tgt_var = tgt.name

            install_tgt = options.get_install(tgt.cmake_name, tgt.install)

            # Generate target kwargs
            tgt_kwargs = {
                'build_by_default': install_tgt,
                'link_args': options.get_link_args(tgt.cmake_name, tgt.link_flags + tgt.link_libraries),
                'link_with': link_with,
                'include_directories': id_node(inc_var),
                'install': install_tgt,
                'override_options': options.get_override_options(tgt.cmake_name, tgt.override_options),
                'objects': [method(x, 'extract_all_objects') for x in objec_libs],
            }  # type: TYPE_mixed_kwargs

            # Only set if installed and only override if it is set
            if install_tgt and tgt.install_dir:
                tgt_kwargs['install_dir'] = tgt.install_dir

            # Handle compiler args
            for key, val in tgt.compile_opts.items():
                tgt_kwargs[f'{key}_args'] = options.get_compile_args(tgt.cmake_name, key, val)

            # Handle -fPCI, etc
            if tgt_func == 'executable':
                tgt_kwargs['pie'] = tgt.pie
            elif tgt_func == 'static_library':
                tgt_kwargs['pic'] = tgt.pie

            # declare_dependency kwargs
            dep_kwargs = {
                'link_args': tgt.link_flags + tgt.link_libraries,
                'link_with': id_node(tgt_var),
                'compile_args': tgt.public_compile_opts,
                'include_directories': id_node(inc_var),
            }  # type: TYPE_mixed_kwargs

            if dependencies:
                generated += dependencies

            # Generate the function nodes
            dir_node = assign(dir_var, function('include_directories', tgt.includes))
            sys_node = assign(sys_var, function('include_directories', tgt.sys_includes, {'is_system': True}))
            inc_node = assign(inc_var, array([id_node(dir_var), id_node(sys_var)]))
            node_list = [dir_node, sys_node, inc_node]
            if tgt_func == 'header_only':
                del dep_kwargs['link_with']
                dep_node = assign(dep_var, function('declare_dependency', kwargs=dep_kwargs))
                node_list += [dep_node]
                src_var = None
                tgt_var = None
            else:
                src_node = assign(src_var, function('files', sources))
                tgt_node = assign(tgt_var, function(tgt_func, [tgt_var, id_node(src_var), *generated], tgt_kwargs))
                node_list += [src_node, tgt_node]
                if tgt_func in ['static_library', 'shared_library']:
                    dep_node = assign(dep_var, function('declare_dependency', kwargs=dep_kwargs))
                    node_list += [dep_node]
                elif tgt_func in ['shared_module']:
                    del dep_kwargs['link_with']
                    dep_node = assign(dep_var, function('declare_dependency', kwargs=dep_kwargs))
                    node_list += [dep_node]
                else:
                    dep_var = None

            # Add the nodes to the ast
            root_cb.lines += node_list
            processed[tgt.name] = {'inc': inc_var, 'src': src_var, 'dep': dep_var, 'tgt': tgt_var, 'func': tgt_func}
            name_map[tgt.cmake_name] = tgt.name

        def process_custom_target(tgt: ConverterCustomTarget) -> None:
            # CMake allows to specify multiple commands in a custom target.
            # To map this to meson, a helper script is used to execute all
            # commands in order. This additionally allows setting the working
            # directory.

            detect_cycle(tgt)
            tgt_var = tgt.name  # type: str

            def resolve_source(x: T.Union[str, ConverterTarget, ConverterCustomTarget, CustomTargetReference]) -> T.Union[str, IdNode, IndexNode]:
                if isinstance(x, ConverterTarget):
                    if x.name not in processed:
                        process_target(x)
                    return extract_tgt(x)
                if isinstance(x, ConverterCustomTarget):
                    if x.name not in processed:
                        process_custom_target(x)
                    return extract_tgt(x)
                elif isinstance(x, CustomTargetReference):
                    if x.ctgt.name not in processed:
                        process_custom_target(x.ctgt)
                    return resolve_ctgt_ref(x)
                else:
                    return x

            # Generate the command list
            command = []  # type: T.List[T.Union[str, IdNode, IndexNode]]
            command += mesonlib.get_meson_command()
            command += ['--internal', 'cmake_run_ctgt']
            command += ['-o', '@OUTPUT@']
            if tgt.original_outputs:
                command += ['-O'] + [x.as_posix() for x in tgt.original_outputs]
            command += ['-d', tgt.working_dir.as_posix()]

            # Generate the commands. Subcommands are separated by ';;;'
            for cmd in tgt.command:
                command += [resolve_source(x) for x in cmd] + [';;;']

            tgt_kwargs = {
                'input': [resolve_source(x) for x in tgt.inputs],
                'output': tgt.outputs,
                'command': command,
                'depends': [resolve_source(x) for x in tgt.depends],
            }  # type: TYPE_mixed_kwargs

            root_cb.lines += [assign(tgt_var, function('custom_target', [tgt.name], tgt_kwargs))]
            processed[tgt.name] = {'inc': None, 'src': None, 'dep': None, 'tgt': tgt_var, 'func': 'custom_target'}
            name_map[tgt.cmake_name] = tgt.name

        # Now generate the target function calls
        for ctgt in self.custom_targets:
            if ctgt.name not in processed:
                process_custom_target(ctgt)
        for tgt in self.targets:
            if tgt.name not in processed:
                process_target(tgt)

        self.generated_targets = processed
        self.internal_name_map = name_map
        return root_cb

    def target_info(self, target: str) -> T.Optional[T.Dict[str, str]]:
        # Try resolving the target name
        # start by checking if there is a 100% match (excluding the name prefix)
        prx_tgt = _sanitize_cmake_name(target)
        if prx_tgt in self.generated_targets:
            return self.generated_targets[prx_tgt]
        # check if there exists a name mapping
        if target in self.internal_name_map:
            target = self.internal_name_map[target]
            assert(target in self.generated_targets)
            return self.generated_targets[target]
        return None

    def target_list(self) -> T.List[str]:
        return list(self.internal_name_map.keys())
