# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Relationship(Model):
    """Relationship.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param annotations:
    :type annotations: list[~dynamics.customerinsights.api.models.Annotation]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'annotations': {'key': 'annotations', 'type': '[Annotation]'},
    }

    def __init__(self, **kwargs):
        super(Relationship, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.annotations = kwargs.get('annotations', None)
