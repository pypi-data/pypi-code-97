# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ValueCount(Model):
    """A value and the count of that value.

    :param value: Represents the value.
    :type value: object
    :param count: Represents Count of the value.
    :type count: long
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
        'count': {'key': 'count', 'type': 'long'},
    }

    def __init__(self, *, value=None, count: int=None, **kwargs) -> None:
        super(ValueCount, self).__init__(**kwargs)
        self.value = value
        self.count = count
