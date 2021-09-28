# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InstanceProvisioningError(Model):
    """Represents an instance provisioning error.

    :param error_code: Possible values include:
     'invalidDynamics365DataSourceCredentials',
     'invalidSalesforceDataSourceCredentials', 'internalError',
     'bapCannotCreateEnvironment'
    :type error_code: str or ~dynamics.customerinsights.api.models.enum
    :param error_args: Gets string formatting arguments for the provisioning
     error
    :type error_args: list[str]
    """

    _attribute_map = {
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_args': {'key': 'errorArgs', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(InstanceProvisioningError, self).__init__(**kwargs)
        self.error_code = kwargs.get('error_code', None)
        self.error_args = kwargs.get('error_args', None)
