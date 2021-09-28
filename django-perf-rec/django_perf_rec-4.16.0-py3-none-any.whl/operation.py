from traceback import StackSummary
from types import TracebackType
from typing import Any, Callable, List, Optional, Type, Union

from django.conf import settings

from django_perf_rec.utils import sorted_names


class Operation:
    def __init__(
        self, alias: str, query: Union[str, List[str]], traceback: StackSummary
    ) -> None:
        self.alias = alias
        self.query = query
        self.traceback = traceback

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, type(self))
            and self.alias == other.alias
            and self.query == other.query
            and self.traceback == other.traceback
        )

    @property
    def name(self) -> str:
        raise TypeError("Needs implementing in subclass!")


class BaseRecorder:
    def __init__(self, alias: str, callback: Callable[[Operation], None]) -> None:
        self.alias = alias
        self.callback = callback

    def __enter__(self) -> None:
        pass

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType],
    ) -> None:
        pass


class AllSourceRecorder:
    """
    Launches Recorders on all the active sources
    """

    sources_setting: str
    recorder_class: Type[BaseRecorder]

    def __init__(self, callback: Callable[[Operation], None]) -> None:
        self.callback = callback

    def __enter__(self) -> None:
        self.recorders = []
        for name in sorted_names(getattr(settings, self.sources_setting).keys()):
            recorder = self.recorder_class(name, self.callback)
            recorder.__enter__()
            self.recorders.append(recorder)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType],
    ) -> None:
        for recorder in reversed(self.recorders):
            recorder.__exit__(exc_type, exc_value, exc_traceback)
        self.recorders = []
