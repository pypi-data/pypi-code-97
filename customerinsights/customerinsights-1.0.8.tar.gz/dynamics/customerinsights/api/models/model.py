# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Model(Model):
    """Model.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param is_hidden:
    :type is_hidden: bool
    :param version:
    :type version: str
    :param culture:
    :type culture: str
    :param pbitime_zone:
    :type pbitime_zone: str
    :param modified_time:
    :type modified_time: datetime
    :param pbimashup:
    :type pbimashup: ~dynamics.customerinsights.api.models.Mashup
    :param annotations:
    :type annotations: list[~dynamics.customerinsights.api.models.Annotation]
    :param entities:
    :type entities: list[~dynamics.customerinsights.api.models.Entity]
    :param relationships:
    :type relationships:
     list[~dynamics.customerinsights.api.models.Relationship]
    :param reference_models:
    :type reference_models:
     list[~dynamics.customerinsights.api.models.ReferenceModel]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_hidden': {'key': 'isHidden', 'type': 'bool'},
        'version': {'key': 'version', 'type': 'str'},
        'culture': {'key': 'culture', 'type': 'str'},
        'pbitime_zone': {'key': 'pbi:timeZone', 'type': 'str'},
        'modified_time': {'key': 'modifiedTime', 'type': 'iso-8601'},
        'pbimashup': {'key': 'pbi:mashup', 'type': 'Mashup'},
        'annotations': {'key': 'annotations', 'type': '[Annotation]'},
        'entities': {'key': 'entities', 'type': '[Entity]'},
        'relationships': {'key': 'relationships', 'type': '[Relationship]'},
        'reference_models': {'key': 'referenceModels', 'type': '[ReferenceModel]'},
    }

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.is_hidden = kwargs.get('is_hidden', None)
        self.version = kwargs.get('version', None)
        self.culture = kwargs.get('culture', None)
        self.pbitime_zone = kwargs.get('pbitime_zone', None)
        self.modified_time = kwargs.get('modified_time', None)
        self.pbimashup = kwargs.get('pbimashup', None)
        self.annotations = kwargs.get('annotations', None)
        self.entities = kwargs.get('entities', None)
        self.relationships = kwargs.get('relationships', None)
        self.reference_models = kwargs.get('reference_models', None)
