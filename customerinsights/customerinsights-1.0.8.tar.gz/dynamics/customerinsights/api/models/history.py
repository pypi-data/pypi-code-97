# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class History(Model):
    """Defaults or user selected values to store across sessions.

    :param id: Gets history id.
    :type id: str
    :param viewed: Checks for already visited.
    :type viewed: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'viewed': {'key': 'viewed', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(History, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.viewed = kwargs.get('viewed', None)
