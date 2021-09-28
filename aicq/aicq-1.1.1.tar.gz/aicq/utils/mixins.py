import typing
from contextvars import ContextVar

T = typing.TypeVar('T')

"""
Took from aiogram (https://github.com/aiogram/aiogram)
"""

class ContextInstanceMixin:

    def __init_subclass__(cls):
        cls.__context_instance = ContextVar(f'instance_{cls.__name__}')
        return cls

    @classmethod
    def get_current(cls: typing.Type[T], no_error=True) -> T:
        if no_error:
            return cls.__context_instance.get(None)
        return cls.__context_instance.get()

    @classmethod
    def set_current(cls: typing.Type[T], value: T):
        if not isinstance(value, cls):
            raise TypeError(f"Value should be instance of {cls.__name__!r} not {type(value).__name__!r}")
        cls.__context_instance.set(value)