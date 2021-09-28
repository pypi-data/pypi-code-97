# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApiErrorResult(Model):
    """Api Error response class (DTO).

    :param exception:
    :type exception: object
    :param http_status_code:
    :type http_status_code: str
    :param exception_culprit: Possible values include: 'system', 'user',
     'external'
    :type exception_culprit: str or ~dynamics.customerinsights.api.models.enum
    :param error_code:
    :type error_code: str
    :param result_severity: Possible values include: 'error', 'warning',
     'recommendation'
    :type result_severity: str or ~dynamics.customerinsights.api.models.enum
    :param message: Message providing more information about the event.
    :type message: str
    :param name: Message providing more information about the event.
    :type name: str
    :param params:
    :type params: dict[str, object]
    :param ci_results: List of CiResult contining CI result error code and
     information (if any).
    :type ci_results: list[~dynamics.customerinsights.api.models.CIResult]
    """

    _attribute_map = {
        'exception': {'key': 'exception', 'type': 'object'},
        'http_status_code': {'key': 'httpStatusCode', 'type': 'str'},
        'exception_culprit': {'key': 'exceptionCulprit', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'result_severity': {'key': 'resultSeverity', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'params': {'key': 'params', 'type': '{object}'},
        'ci_results': {'key': 'ciResults', 'type': '[CIResult]'},
    }

    def __init__(self, *, exception=None, http_status_code: str=None, exception_culprit=None, error_code: str=None, result_severity=None, message: str=None, name: str=None, params=None, ci_results=None, **kwargs) -> None:
        super(ApiErrorResult, self).__init__(**kwargs)
        self.exception = exception
        self.http_status_code = http_status_code
        self.exception_culprit = exception_culprit
        self.error_code = error_code
        self.result_severity = result_severity
        self.message = message
        self.name = name
        self.params = params
        self.ci_results = ci_results
