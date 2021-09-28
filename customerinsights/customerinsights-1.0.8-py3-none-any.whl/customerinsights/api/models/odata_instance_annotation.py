# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ODataInstanceAnnotation(Model):
    """ODataInstanceAnnotation.

    :param name:
    :type name: str
    :param value:
    :type value: ~dynamics.customerinsights.api.models.ODataValue
    :param type_annotation:
    :type type_annotation:
     ~dynamics.customerinsights.api.models.ODataTypeAnnotation
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'ODataValue'},
        'type_annotation': {'key': 'typeAnnotation', 'type': 'ODataTypeAnnotation'},
    }

    def __init__(self, **kwargs):
        super(ODataInstanceAnnotation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)
        self.type_annotation = kwargs.get('type_annotation', None)
