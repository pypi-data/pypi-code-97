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


class ConversationReadEventAllOfPayload(object):
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
        'conversation': 'ConversationTruncated',
        'activity': 'Activity'
    }

    attribute_map = {
        'conversation': 'conversation',
        'activity': 'activity'
    }

    nulls = set()

    def __init__(self, conversation=None, activity=None, local_vars_configuration=None):  # noqa: E501
        """ConversationReadEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation = None
        self._activity = None
        self.discriminator = None

        if conversation is not None:
            self.conversation = conversation
        if activity is not None:
            self.activity = activity

    @property
    def conversation(self):
        """Gets the conversation of this ConversationReadEventAllOfPayload.  # noqa: E501

        The conversation in which the message was read.  # noqa: E501

        :return: The conversation of this ConversationReadEventAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ConversationReadEventAllOfPayload.

        The conversation in which the message was read.  # noqa: E501

        :param conversation: The conversation of this ConversationReadEventAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def activity(self):
        """Gets the activity of this ConversationReadEventAllOfPayload.  # noqa: E501

        The activity that was sent.  # noqa: E501

        :return: The activity of this ConversationReadEventAllOfPayload.  # noqa: E501
        :rtype: Activity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ConversationReadEventAllOfPayload.

        The activity that was sent.  # noqa: E501

        :param activity: The activity of this ConversationReadEventAllOfPayload.  # noqa: E501
        :type: Activity
        """

        self._activity = activity

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
        if not isinstance(other, ConversationReadEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationReadEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
