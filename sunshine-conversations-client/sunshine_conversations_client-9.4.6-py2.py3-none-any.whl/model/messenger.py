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

try:
    Integration = __import__("sunshine_conversations_client.model."+re.sub(r'(?<!^)(?=[A-Z])', '_', "Integration").lower(), fromlist=("Integration")).Integration
except ImportError:
    pass

class Messenger(Integration):
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
        'page_access_token': 'str',
        'app_id': 'str',
        'app_secret': 'str'
    }

    attribute_map = {
        'type': 'type',
        'page_access_token': 'pageAccessToken',
        'app_id': 'appId',
        'app_secret': 'appSecret'
    }

    nulls = set()

    def __init__(self, type='messenger', page_access_token=None, app_id=None, app_secret=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """Messenger - a model defined in OpenAPI"""  # noqa: E501
        super().__init__(**kwargs)

        if (super().openapi_types is not None):
            all_types = super().openapi_types.copy()
            all_types.update(self.openapi_types)
            self.openapi_types = all_types

        if (super().attribute_map is not None):
            all_attributes = super().attribute_map.copy()
            all_attributes.update(self.attribute_map)
            self.attribute_map = all_attributes
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._page_access_token = None
        self._app_id = None
        self._app_secret = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.page_access_token = page_access_token
        self.app_id = app_id
        if app_secret is not None:
            self.app_secret = app_secret

    @property
    def type(self):
        """Gets the type of this Messenger.  # noqa: E501

        Facebook Messenger Setup steps: - Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); - The Facebook app must have been submitted to Facebook for app review with the “manage_pages” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. - In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.   # noqa: E501

        :return: The type of this Messenger.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Messenger.

        Facebook Messenger Setup steps: - Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); - The Facebook app must have been submitted to Facebook for app review with the “manage_pages” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. - In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.   # noqa: E501

        :param type: The type of this Messenger.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def page_access_token(self):
        """Gets the page_access_token of this Messenger.  # noqa: E501

        A Facebook Page Access Token.  # noqa: E501

        :return: The page_access_token of this Messenger.  # noqa: E501
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """Sets the page_access_token of this Messenger.

        A Facebook Page Access Token.  # noqa: E501

        :param page_access_token: The page_access_token of this Messenger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `page_access_token`, must not be `None`")  # noqa: E501

        self._page_access_token = page_access_token

    @property
    def app_id(self):
        """Gets the app_id of this Messenger.  # noqa: E501

        A Facebook App ID.  # noqa: E501

        :return: The app_id of this Messenger.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this Messenger.

        A Facebook App ID.  # noqa: E501

        :param app_id: The app_id of this Messenger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_secret(self):
        """Gets the app_secret of this Messenger.  # noqa: E501

        A Facebook App Secret.  # noqa: E501

        :return: The app_secret of this Messenger.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this Messenger.

        A Facebook App Secret.  # noqa: E501

        :param app_secret: The app_secret of this Messenger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `app_secret`, must not be `None`")  # noqa: E501

        self._app_secret = app_secret

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
        if not isinstance(other, Messenger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Messenger):
            return True

        return self.to_dict() != other.to_dict()
