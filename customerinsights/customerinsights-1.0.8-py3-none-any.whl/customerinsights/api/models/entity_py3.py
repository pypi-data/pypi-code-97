# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Entity(Model):
    """Entity.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param is_hidden:
    :type is_hidden: bool
    :param annotations:
    :type annotations: list[~dynamics.customerinsights.api.models.Annotation]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_hidden': {'key': 'isHidden', 'type': 'bool'},
        'annotations': {'key': 'annotations', 'type': '[Annotation]'},
    }

    def __init__(self, *, name: str=None, description: str=None, is_hidden: bool=None, annotations=None, **kwargs) -> None:
        super(Entity, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.is_hidden = is_hidden
        self.annotations = annotations
