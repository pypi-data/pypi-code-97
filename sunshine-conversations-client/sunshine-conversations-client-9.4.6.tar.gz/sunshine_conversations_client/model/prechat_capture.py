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


class PrechatCapture(object):
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
        'avatar_url': 'str',
        'enabled': 'bool',
        'enable_email_linking': 'bool',
        'fields': 'list[Field]'
    }

    attribute_map = {
        'avatar_url': 'avatarUrl',
        'enabled': 'enabled',
        'enable_email_linking': 'enableEmailLinking',
        'fields': 'fields'
    }

    nulls = set()

    def __init__(self, avatar_url='undefined', enabled=False, enable_email_linking=False, fields=None, local_vars_configuration=None):  # noqa: E501
        """PrechatCapture - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._avatar_url = None
        self._enabled = None
        self._enable_email_linking = None
        self._fields = None
        self.discriminator = None

        if avatar_url is not None:
            self.avatar_url = avatar_url
        if enabled is not None:
            self.enabled = enabled
        if enable_email_linking is not None:
            self.enable_email_linking = enable_email_linking
        if fields is not None:
            self.fields = fields

    @property
    def avatar_url(self):
        """Gets the avatar_url of this PrechatCapture.  # noqa: E501

        Sets the URL of the avatar to use for the automatic reply to the prechat capture messages.  # noqa: E501

        :return: The avatar_url of this PrechatCapture.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this PrechatCapture.

        Sets the URL of the avatar to use for the automatic reply to the prechat capture messages.  # noqa: E501

        :param avatar_url: The avatar_url of this PrechatCapture.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def enabled(self):
        """Gets the enabled of this PrechatCapture.  # noqa: E501

        If true, enables the Prechat Capture add-on when the Web Messenger is initialized.  # noqa: E501

        :return: The enabled of this PrechatCapture.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PrechatCapture.

        If true, enables the Prechat Capture add-on when the Web Messenger is initialized.  # noqa: E501

        :param enabled: The enabled of this PrechatCapture.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def enable_email_linking(self):
        """Gets the enable_email_linking of this PrechatCapture.  # noqa: E501

        f true and Mailgun is integrated, will automatically link submitted emails.  # noqa: E501

        :return: The enable_email_linking of this PrechatCapture.  # noqa: E501
        :rtype: bool
        """
        return self._enable_email_linking

    @enable_email_linking.setter
    def enable_email_linking(self, enable_email_linking):
        """Sets the enable_email_linking of this PrechatCapture.

        f true and Mailgun is integrated, will automatically link submitted emails.  # noqa: E501

        :param enable_email_linking: The enable_email_linking of this PrechatCapture.  # noqa: E501
        :type: bool
        """

        self._enable_email_linking = enable_email_linking

    @property
    def fields(self):
        """Gets the fields of this PrechatCapture.  # noqa: E501

        Array of Fields. Overrides the default Prechat Capture fields to define a custom form.  # noqa: E501

        :return: The fields of this PrechatCapture.  # noqa: E501
        :rtype: list[Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this PrechatCapture.

        Array of Fields. Overrides the default Prechat Capture fields to define a custom form.  # noqa: E501

        :param fields: The fields of this PrechatCapture.  # noqa: E501
        :type: list[Field]
        """

        self._fields = fields

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
        if not isinstance(other, PrechatCapture):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrechatCapture):
            return True

        return self.to_dict() != other.to_dict()
