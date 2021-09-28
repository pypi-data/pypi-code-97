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


class ParticipantLeaveBodyParticipantId(object):
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
        'participant_id': 'str'
    }

    attribute_map = {
        'participant_id': 'participantId'
    }

    nulls = set()

    def __init__(self, participant_id=None, local_vars_configuration=None):  # noqa: E501
        """ParticipantLeaveBodyParticipantId - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._participant_id = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id

    @property
    def participant_id(self):
        """Gets the participant_id of this ParticipantLeaveBodyParticipantId.  # noqa: E501

        The participantId of the user that will be removed from the conversation. It will return 404 if the user can’t be found.   # noqa: E501

        :return: The participant_id of this ParticipantLeaveBodyParticipantId.  # noqa: E501
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this ParticipantLeaveBodyParticipantId.

        The participantId of the user that will be removed from the conversation. It will return 404 if the user can’t be found.   # noqa: E501

        :param participant_id: The participant_id of this ParticipantLeaveBodyParticipantId.  # noqa: E501
        :type: str
        """

        self._participant_id = participant_id

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
        if not isinstance(other, ParticipantLeaveBodyParticipantId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParticipantLeaveBodyParticipantId):
            return True

        return self.to_dict() != other.to_dict()
