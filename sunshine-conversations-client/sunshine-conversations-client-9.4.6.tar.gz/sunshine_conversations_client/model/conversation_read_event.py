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


class ConversationReadEvent(object):
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
        'id': 'str',
        'type': 'str',
        'created_at': 'str',
        'payload': 'ConversationReadEventAllOfPayload'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'created_at': 'createdAt',
        'payload': 'payload'
    }

    nulls = set()

    def __init__(self, id=None, type=None, created_at=None, payload=None, local_vars_configuration=None):  # noqa: E501
        """ConversationReadEvent - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._created_at = None
        self._payload = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if payload is not None:
            self.payload = payload

    @property
    def id(self):
        """Gets the id of this ConversationReadEvent.  # noqa: E501

        The unique ID of the event. May be used to ensure that an event is not processed twice in the case of a webhook that is re-tried due to an error or timeout.  # noqa: E501

        :return: The id of this ConversationReadEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConversationReadEvent.

        The unique ID of the event. May be used to ensure that an event is not processed twice in the case of a webhook that is re-tried due to an error or timeout.  # noqa: E501

        :param id: The id of this ConversationReadEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ConversationReadEvent.  # noqa: E501

        The type of the event. Will match one of the subscribed triggers for your [webhook](#operation/createWebhook).  # noqa: E501

        :return: The type of this ConversationReadEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationReadEvent.

        The type of the event. Will match one of the subscribed triggers for your [webhook](#operation/createWebhook).  # noqa: E501

        :param type: The type of this ConversationReadEvent.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ConversationReadEvent.  # noqa: E501

        A timestamp signifying when the event was generated. Formatted as `YYYY-MM-DDThh:mm:ss.SSSZ`.  # noqa: E501

        :return: The created_at of this ConversationReadEvent.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConversationReadEvent.

        A timestamp signifying when the event was generated. Formatted as `YYYY-MM-DDThh:mm:ss.SSSZ`.  # noqa: E501

        :param created_at: The created_at of this ConversationReadEvent.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def payload(self):
        """Gets the payload of this ConversationReadEvent.  # noqa: E501


        :return: The payload of this ConversationReadEvent.  # noqa: E501
        :rtype: ConversationReadEventAllOfPayload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ConversationReadEvent.


        :param payload: The payload of this ConversationReadEvent.  # noqa: E501
        :type: ConversationReadEventAllOfPayload
        """

        self._payload = payload

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
        if not isinstance(other, ConversationReadEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationReadEvent):
            return True

        return self.to_dict() != other.to_dict()
