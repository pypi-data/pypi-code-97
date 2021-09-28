# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class KeyValue(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, description=None, key=None, value=None):  # noqa: E501
        """KeyValue - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._key = None
        self._value = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def description(self):
        """Gets the description of this KeyValue.  # noqa: E501

        Optional description of the lookup value  # noqa: E501

        :return: The description of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeyValue.

        Optional description of the lookup value  # noqa: E501

        :param description: The description of this KeyValue.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this KeyValue.  # noqa: E501

        The key or id of this lookup value  # noqa: E501

        :return: The key of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this KeyValue.

        The key or id of this lookup value  # noqa: E501

        :param key: The key of this KeyValue.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this KeyValue.  # noqa: E501

        The value of this lookup value  # noqa: E501

        :return: The value of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this KeyValue.

        The value of this lookup value  # noqa: E501

        :param value: The value of this KeyValue.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(KeyValue, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
