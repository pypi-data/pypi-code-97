import sys
from typing import Optional, Tuple

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal  # pragma: no cover


from rich._loop import loop_last
from quo.terminal import Terminal, ConsoleOptions, RenderableType, RenderResult
from rich.control import Control
from rich.segment import ControlType, Segment
from rich.style import StyleType
from quo.text import Text

VerticalOverflowMethod = Literal["crop", "ellipsis", "visible"]


class LiveRender:
    """Creates a renderable that may be updated.

    Args:
        renderable (RenderableType): Any renderable object.
        style (StyleType, optional): An optional style to apply to the renderable. Defaults to "".
    """

    def __init__(
        self,
        renderable: RenderableType,
        style: StyleType = "",
        vertical_overflow: VerticalOverflowMethod = "ellipsis",
    ) -> None:
        self.renderable = renderable
        self.style = style
        self.vertical_overflow = vertical_overflow
        self._shape: Optional[Tuple[int, int]] = None

    def set_renderable(self, renderable: RenderableType) -> None:
        """Set a new renderable.

        Args:
            renderable (RenderableType): Any renderable object, including str.
        """
        self.renderable = renderable

    def position_cursor(self) -> Control:
        """Get control codes to move cursor to beginning of live render.

        Returns:
            Control: A control instance that may be printed.
        """
        if self._shape is not None:
            _, height = self._shape
            return Control(
                ControlType.CARRIAGE_RETURN,
                (ControlType.ERASE_IN_LINE, 2),
                *(
                    (
                        (ControlType.CURSOR_UP, 1),
                        (ControlType.ERASE_IN_LINE, 2),
                    )
                    * (height - 1)
                )
            )
        return Control()

    def restore_cursor(self) -> Control:
        """Get control codes to clear the render and restore the cursor to its previous position.

        Returns:
            Control: A Control instance that may be printed.
        """
        if self._shape is not None:
            _, height = self._shape
            return Control(
                ControlType.CARRIAGE_RETURN,
                *((ControlType.CURSOR_UP, 1), (ControlType.ERASE_IN_LINE, 2)) * height
            )
        return Control()

    def __rich_console__(
        self, console: Terminal, options: ConsoleOptions
    ) -> RenderResult:

        renderable = self.renderable
        _Segment = Segment
        style = console.get_style(self.style)
        lines = console.render_lines(renderable, options, style=style, pad=False)
        shape = _Segment.get_shape(lines)

        _, height = shape
        if height > options.size.height:
            if self.vertical_overflow == "crop":
                lines = lines[: options.size.height]
                shape = _Segment.get_shape(lines)
            elif self.vertical_overflow == "ellipsis":
                lines = lines[: (options.size.height - 1)]
                overflow_text = Text(
                    "...",
                    overflow="crop",
                    justify="center",
                    end="",
                    style="live.ellipsis",
                )
                lines.append(list(console.render(overflow_text)))
                shape = _Segment.get_shape(lines)
        self._shape = shape

        for last, line in loop_last(lines):
            yield from line
            if not last:
                yield _Segment.line()
