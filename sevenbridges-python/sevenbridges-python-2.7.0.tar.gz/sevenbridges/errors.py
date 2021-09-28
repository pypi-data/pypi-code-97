class SbgError(Exception):
    """Base class for SBG errors.

    Provides a base exception for all errors
    that are thrown by sevenbridges-python library.
    """

    def __init__(self, message=None, code=None, status=None, more_info=None):
        """
        :param code: Custom error code
        :param status: Http status code.
        :param message: Message describing the error.
        """
        self.code = code
        self.status = status
        self.message = message
        self.more_info = more_info

    def __str__(self):
        return str(self.message)


class ResourceNotModified(SbgError):
    def __init__(self):
        super().__init__(
            code=-1,
            status=-1,
            message=(
                'No relevant changes were detected in order to update the '
                'resource on the server.'
            )
        )


class NonJSONResponseError(SbgError):
    def __init__(self, status, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=status, message=message, more_info=more_info
        )


class ReadOnlyPropertyError(SbgError):
    def __init__(self, message):
        super().__init__(
            code=-1, status=-1, message=message
        )


class ValidationError(SbgError):
    def __init__(self, message):
        super().__init__(
            code=-1, status=-1, message=message
        )


class TaskValidationError(SbgError):
    def __init__(self, message, task=None):
        self.task = task
        super().__init__(
            code=-1, status=-1, message=message
        )


class PaginationError(SbgError):
    def __init__(self, message):
        super().__init__(
            code=-1, status=-1, message=message
        )


class AdvanceAccessError(SbgError):
    def __init__(self, message=None):
        super().__init__(
            code=-1, status=-1, message=message
        )


class BadRequest(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=400, message=message, more_info=more_info)


class Unauthorized(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=401, message=message, more_info=more_info
        )


class Forbidden(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=403, message=message, more_info=more_info
        )


class NotFound(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=404, message=message, more_info=more_info
        )


class Conflict(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=409, message=message, more_info=more_info
        )


class TooManyRequests(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=429, message=message, more_info=more_info
        )


class ServerError(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=500, message=message, more_info=more_info
        )


class ServiceUnavailable(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=503, message=message, more_info=more_info
        )


class MethodNotAllowed(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=405, message=message, more_info=more_info
        )


class RequestTimeout(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=408, message=message, more_info=more_info
        )


class LocalFileAlreadyExists(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=-1, message=message, more_info=more_info
        )


class ExecutionDetailsInvalidTaskType(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=-1, message=message, more_info=more_info
        )


class URITooLong(SbgError):
    def __init__(self, code=None, message=None, more_info=None):
        super().__init__(
            code=code, status=414, message=message, more_info=more_info
        )
