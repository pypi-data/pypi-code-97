# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1419
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class PolicyIdRoleResource(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'policies': 'list[PolicyId]',
        'policy_collections': 'list[PolicyCollectionId]'
    }

    attribute_map = {
        'policies': 'policies',
        'policy_collections': 'policyCollections'
    }

    required_map = {
        'policies': 'optional',
        'policy_collections': 'optional'
    }

    def __init__(self, policies=None, policy_collections=None, local_vars_configuration=None):  # noqa: E501
        """PolicyIdRoleResource - a model defined in OpenAPI"
        
        :param policies: 
        :type policies: list[finbourne_access.PolicyId]
        :param policy_collections: 
        :type policy_collections: list[finbourne_access.PolicyCollectionId]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._policies = None
        self._policy_collections = None
        self.discriminator = None

        self.policies = policies
        self.policy_collections = policy_collections

    @property
    def policies(self):
        """Gets the policies of this PolicyIdRoleResource.  # noqa: E501


        :return: The policies of this PolicyIdRoleResource.  # noqa: E501
        :rtype: list[finbourne_access.PolicyId]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyIdRoleResource.


        :param policies: The policies of this PolicyIdRoleResource.  # noqa: E501
        :type policies: list[finbourne_access.PolicyId]
        """

        self._policies = policies

    @property
    def policy_collections(self):
        """Gets the policy_collections of this PolicyIdRoleResource.  # noqa: E501


        :return: The policy_collections of this PolicyIdRoleResource.  # noqa: E501
        :rtype: list[finbourne_access.PolicyCollectionId]
        """
        return self._policy_collections

    @policy_collections.setter
    def policy_collections(self, policy_collections):
        """Sets the policy_collections of this PolicyIdRoleResource.


        :param policy_collections: The policy_collections of this PolicyIdRoleResource.  # noqa: E501
        :type policy_collections: list[finbourne_access.PolicyCollectionId]
        """

        self._policy_collections = policy_collections

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyIdRoleResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyIdRoleResource):
            return True

        return self.to_dict() != other.to_dict()
