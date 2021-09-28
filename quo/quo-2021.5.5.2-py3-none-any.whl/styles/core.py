"""
The base classes for the styling.
"""
from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Callable, Dict, Hashable, List, NamedTuple, Optional, Tuple

__all__ = [
    "Attrs",
    "DEFAULT_ATTRS",
    "ANSI_COLOR_NAMES",
    "ANSI_COLOR_NAMES_ALIASES",
    "BaseStyle",
    "DummyStyle",
    "DynamicStyle",
]


#: Style attributes.
Attrs = NamedTuple(
    "Attrs",
    [
        ("color", Optional[str]),
        ("bgcolor", Optional[str]),
        ("bold", Optional[bool]),
        ("underline", Optional[bool]),
        ("italic", Optional[bool]),
        ("blink", Optional[bool]),
        ("reverse", Optional[bool]),
        ("hidden", Optional[bool]),
    ],
)

"""
:param color: Hexadecimal string. E.g. '000000' or Ansi color name: e.g. 'ansiblue'
:param bgcolor: Hexadecimal string. E.g. 'ffffff' or Ansi color name: e.g. 'ansired'
:param bold: Boolean
:param underline: Boolean
:param italic: Boolean
:param blink: Boolean
:param reverse: Boolean
:param hidden: Boolean
"""

#: The default `Attrs`.
DEFAULT_ATTRS = Attrs(
    color="",
    bgcolor="",
    bold=False,
    underline=False,
    italic=False,
    blink=False,
    reverse=False,
    hidden=False,
)


#: ``Attrs.bgcolor/fgcolor`` can be in either 'ffffff' format, or can be any of
#: the following in case we want to take colors from the 8/16 color palette.
#: Usually, in that case, the terminal application allows to configure the RGB
#: values for these names.
#: ISO 6429 colors
ANSI_COLOR_NAMES = [
    "ansidefault",
    # Low intensity, dark.  (One or two components 0x80, the other 0x00.)
    "ansiblack",
    "ansired",
    "ansigreen",
    "ansiyellow",
    "ansiblue",
    "ansimagenta",
    "ansicyan",
    "ansigray",
    # High intensity, bright. (One or two components 0xff, the other 0x00. Not supported everywhere.)
    "ansibrightblack",
    "ansibrightred",
    "ansibrightgreen",
    "ansibrightyellow",
    "ansibrightblue",
    "ansibrightmagenta",
    "ansibrightcyan",
    "ansiwhite",
]


# The table below maps the old aliases to the current names.
ANSI_COLOR_NAMES_ALIASES: Dict[str, str] = {
    "ansidarkgray": "ansibrightblack",
    "ansiteal": "ansicyan",
    "ansiturquoise": "ansibrightcyan",
    "ansibrown": "ansiyellow",
    "ansipurple": "ansimagenta",
    "ansifuchsia": "ansibrightmagenta",
    "ansilightgray": "ansigray",
    "ansidarkred": "ansired",
    "ansidarkgreen": "ansigreen",
    "ansidarkblue": "ansiblue",
}
assert set(ANSI_COLOR_NAMES_ALIASES.values()).issubset(set(ANSI_COLOR_NAMES))
assert not (set(ANSI_COLOR_NAMES_ALIASES.keys()) & set(ANSI_COLOR_NAMES))


class BaseStyle(metaclass=ABCMeta):
    """
    Abstract base class for quo  styles.
    """

    @abstractmethod
    def get_attrs_for_style_str(
        self, style_str: str, default: Attrs = DEFAULT_ATTRS
    ) -> Attrs:
        """
        Return :class:`.Attrs` for the given style string.

        :param style_str: The style string. This can contain inline styling as
            well as classnames (e.g. "class:title").
        :param default: `Attrs` to be used if no styling was defined.
        """

    @abstractproperty
    def style_rules(self) -> List[Tuple[str, str]]:
        """
        The list of style rules, used to create this style.
        (Required for `DynamicStyle` and `_MergedStyle` to work.)
        """
        return []

    @abstractmethod
    def invalidation_hash(self) -> Hashable:
        """
        Invalidation hash for the style. When this changes over time, the
        renderer knows that something in the style changed, and that everything
        has to be redrawn.
        """


class DummyStyle(BaseStyle):
    """
    A style that doesn't style anything.
    """

    def get_attrs_for_style_str(
        self, style_str: str, default: Attrs = DEFAULT_ATTRS
    ) -> Attrs:
        return default

    def invalidation_hash(self) -> Hashable:
        return 1  # Always the same value.

    @property
    def style_rules(self) -> List[Tuple[str, str]]:
        return []


class DynamicStyle(BaseStyle):
    """
    Style class that can dynamically returns an other Style.

    :param get_style: Callable that returns a :class:`.Style` instance.
    """

    def __init__(self, get_style: Callable[[], Optional[BaseStyle]]):
        self.get_style = get_style
        self._dummy = DummyStyle()

    def get_attrs_for_style_str(
        self, style_str: str, default: Attrs = DEFAULT_ATTRS
    ) -> Attrs:
        style = self.get_style() or self._dummy

        return style.get_attrs_for_style_str(style_str, default)

    def invalidation_hash(self) -> Hashable:
        return (self.get_style() or self._dummy).invalidation_hash()

    @property
    def style_rules(self) -> List[Tuple[str, str]]:
        return (self.get_style() or self._dummy).style_rules
