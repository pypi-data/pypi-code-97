# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SupportedSkuSummary(object):
    """
    A specific SKU. Oracle Cloud Infrastructure VMware Solution supports the following billing interval SKUs:
    HOUR, MONTH, ONE_YEAR, and THREE_YEARS.
    """

    #: A constant which can be used with the name property of a SupportedSkuSummary.
    #: This constant has a value of "HOUR"
    NAME_HOUR = "HOUR"

    #: A constant which can be used with the name property of a SupportedSkuSummary.
    #: This constant has a value of "MONTH"
    NAME_MONTH = "MONTH"

    #: A constant which can be used with the name property of a SupportedSkuSummary.
    #: This constant has a value of "ONE_YEAR"
    NAME_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the name property of a SupportedSkuSummary.
    #: This constant has a value of "THREE_YEARS"
    NAME_THREE_YEARS = "THREE_YEARS"

    def __init__(self, **kwargs):
        """
        Initializes a new SupportedSkuSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SupportedSkuSummary.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SupportedSkuSummary.
        name of SKU

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this SupportedSkuSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SupportedSkuSummary.
        name of SKU


        :param name: The name of this SupportedSkuSummary.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
