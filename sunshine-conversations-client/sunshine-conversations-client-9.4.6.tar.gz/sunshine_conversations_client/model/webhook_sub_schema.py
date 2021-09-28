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


class WebhookSubSchema(object):
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
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version'
    }

    nulls = set()

    def __init__(self, id=None, version=None, local_vars_configuration=None):  # noqa: E501
        """WebhookSubSchema - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this WebhookSubSchema.  # noqa: E501

        The unique ID of the webhook.  # noqa: E501

        :return: The id of this WebhookSubSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookSubSchema.

        The unique ID of the webhook.  # noqa: E501

        :param id: The id of this WebhookSubSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this WebhookSubSchema.  # noqa: E501

        Schema version of the payload delivered to this webhook (v2).  # noqa: E501

        :return: The version of this WebhookSubSchema.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WebhookSubSchema.

        Schema version of the payload delivered to this webhook (v2).  # noqa: E501

        :param version: The version of this WebhookSubSchema.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, WebhookSubSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookSubSchema):
            return True

        return self.to_dict() != other.to_dict()
