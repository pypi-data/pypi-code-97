# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ODataTypeAnnotation(Model):
    """ODataTypeAnnotation.

    :param type_name:
    :type type_name: str
    """

    _attribute_map = {
        'type_name': {'key': 'typeName', 'type': 'str'},
    }

    def __init__(self, *, type_name: str=None, **kwargs) -> None:
        super(ODataTypeAnnotation, self).__init__(**kwargs)
        self.type_name = type_name
