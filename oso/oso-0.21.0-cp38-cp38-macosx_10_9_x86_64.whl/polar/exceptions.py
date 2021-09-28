"""Exceptions used within Oso."""
# @TODO: Should we just generate these from the rust code?
from textwrap import dedent


# @TODO(gkaemmer): Move this to an `exceptions` module so that it can be shared
# between here and oso/exceptions.py without causing a circular dependency.
class OsoError(Exception):
    """Base exception class for Oso."""

    def __init__(self, message=None, details=None):
        self.message = message
        self.details = details
        self.stack_trace = details.get("stack_trace") if details else None
        super().__init__(self.add_get_help(self.message))

    @classmethod
    def add_get_help(cls, message):
        return (
            str(message)
            + f"\n\tGet help with Oso from our engineers: https://help.osohq.com/error/{cls.__name__}"
        )


class FFIErrorNotFound(OsoError):
    """Raised when an error is generated by the Oso Rust core, but the error type is not found."""

    pass


# ==================
# RUNTIME EXCEPTIONS
# ==================


class PolarRuntimeError(OsoError):
    """Errors generated by Oso at runtime"""

    pass


class SerializationError(PolarRuntimeError):
    """Error serializing data across the FFI boundary"""

    pass


class UnsupportedError(PolarRuntimeError):
    """Unsupported action error generated by the Rust core"""

    pass


class PolarTypeError(PolarRuntimeError):
    """Error related to the type of a Polar object, generated by the Rust core"""

    pass


class StackOverflowError(PolarRuntimeError):
    """Polar stack overflow error, generated by the Rust core"""

    pass


class FileLoadingError(PolarRuntimeError):
    """Error loading a Polar file"""

    pass


class UnregisteredClassError(PolarRuntimeError):
    """Raised on attempts to reference unregistered Python classes from a Polar policy."""

    pass


class DuplicateClassAliasError(PolarRuntimeError):
    """Raised on attempts to register a class with the same name as a class that has already been registered"""

    def __init__(self, name, old, new):
        super().__init__(
            f"Attempted to alias {new} as '{name}', but {old} already has that alias."
        )


class DuplicateInstanceRegistrationError(PolarRuntimeError):
    pass


class PolarFileExtensionError(PolarRuntimeError):
    def __init__(self, file):
        super().__init__(
            f"Polar files must have .polar extension. Offending file: {file}"
        )


class PolarFileNotFoundError(PolarRuntimeError):
    def __init__(self, file):
        super().__init__(f"Could not find file: {file}")


class UnregisteredInstanceError(PolarRuntimeError):
    pass


class InlineQueryFailedError(PolarRuntimeError):
    def __init__(self, source):
        super().__init__(f"Inline query failed: {source}")


class UnexpectedPolarTypeError(PolarRuntimeError):
    pass


class InvalidQueryTypeError(PolarRuntimeError):
    pass


class InvalidCallError(PolarRuntimeError):
    """Invalid attempt to call a field or method on an object in Polar"""

    pass


class InvalidIteratorError(PolarRuntimeError):
    """Invalid attempt to iterate over a non-iterable value"""

    pass


class InvalidConstructorError(PolarRuntimeError):
    pass


# =================
# PARSER EXCEPTIONS
# =================


class ParserError(OsoError):
    """Parse time errors."""

    pass


class IntegerOverflow(ParserError):
    pass


class InvalidTokenCharacter(ParserError):
    pass


class InvalidToken(ParserError):
    pass


class UnrecognizedEOF(ParserError):
    pass


class UnrecognizedToken(ParserError):
    pass


class ExtraToken(ParserError):
    pass


# ======================
# OPERATIONAL EXCEPTIONS
# ======================


class OperationalError(OsoError):
    """Errors from polar that are not necessarily the user's fault. OOM etc..."""

    pass


class UnknownError(OperationalError):
    pass


# ==============
# API EXCEPTIONS
# ==============


class PolarApiError(OsoError):
    """Errors coming from the python bindings to polar, not the engine itself."""

    pass


class ParameterError(PolarApiError):
    pass


class ValidationError(PolarApiError):
    pass


UNEXPECTED_EXPRESSION_MESSAGE = dedent(
    """\
Received Expression from Polar VM. The Expression type is only supported when
using django-oso or sqlalchemy-oso's data filtering features. Did you perform an
operation over an unbound variable in your policy?

To silence this error and receive an Expression result, pass
accept_expression=True to Oso.query.
"""
)
