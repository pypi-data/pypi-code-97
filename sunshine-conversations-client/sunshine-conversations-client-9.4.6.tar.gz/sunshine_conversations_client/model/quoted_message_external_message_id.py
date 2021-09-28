# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class QuotedMessageExternalMessageId(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'external_message_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'external_message_id': 'externalMessageId'
    }

    nulls = set()

    def __init__(self, type='externalMessageId', external_message_id=None, local_vars_configuration=None):  # noqa: E501
        """QuotedMessageExternalMessageId - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._external_message_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if external_message_id is not None:
            self.external_message_id = external_message_id

    @property
    def type(self):
        """Gets the type of this QuotedMessageExternalMessageId.  # noqa: E501

        The type of quotedMessage - `externalMessageId` if no Sunshine Conversations message matched the quoted message.  # noqa: E501

        :return: The type of this QuotedMessageExternalMessageId.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotedMessageExternalMessageId.

        The type of quotedMessage - `externalMessageId` if no Sunshine Conversations message matched the quoted message.  # noqa: E501

        :param type: The type of this QuotedMessageExternalMessageId.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def external_message_id(self):
        """Gets the external_message_id of this QuotedMessageExternalMessageId.  # noqa: E501

        The external message Id of the quoted message.  # noqa: E501

        :return: The external_message_id of this QuotedMessageExternalMessageId.  # noqa: E501
        :rtype: str
        """
        return self._external_message_id

    @external_message_id.setter
    def external_message_id(self, external_message_id):
        """Sets the external_message_id of this QuotedMessageExternalMessageId.

        The external message Id of the quoted message.  # noqa: E501

        :param external_message_id: The external_message_id of this QuotedMessageExternalMessageId.  # noqa: E501
        :type: str
        """

        self._external_message_id = external_message_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuotedMessageExternalMessageId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuotedMessageExternalMessageId):
            return True

        return self.to_dict() != other.to_dict()
