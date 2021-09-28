# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeasureVariableCondition(Model):
    """Represents a variable condition.

    :param kind: Possible values include: 'replaceNulls',
     'replaceTargetValues'
    :type kind: str or ~dynamics.customerinsights.api.models.enum
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, *, kind=None, **kwargs) -> None:
        super(MeasureVariableCondition, self).__init__(**kwargs)
        self.kind = kind
