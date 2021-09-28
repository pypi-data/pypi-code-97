# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ParsingError(Model):
    """ParsingError.

    :param messages:
    :type messages: list[~dynamics.customerinsights.api.models.LogMessage]
    :param code: Possible values include: 'unknown', 'parsingFailed',
     'entityNotFound', 'attributeNotFound', 'unsupportedSyntax',
     'invalidOperation', 'incorrectArgumentCount', 'incorrectIntervalType',
     'invalidArgument'
    :type code: str or ~dynamics.customerinsights.api.models.enum
    """

    _attribute_map = {
        'messages': {'key': 'messages', 'type': '[LogMessage]'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ParsingError, self).__init__(**kwargs)
        self.messages = kwargs.get('messages', None)
        self.code = kwargs.get('code', None)
