# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RoleDefinition(Model):
    """RoleDefinition.

    :param description:
    :type description: str
    :param role_name:
    :type role_name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'role_name': {'key': 'roleName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoleDefinition, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.role_name = kwargs.get('role_name', None)
