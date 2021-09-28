# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RenameHeaderPolicyItem(object):
    """
    The value will be a copy of the original value of the source header and will not be affected by any other
    transformation policies applied to that header.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RenameHeaderPolicyItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param _from:
            The value to assign to the _from property of this RenameHeaderPolicyItem.
        :type _from: str

        :param to:
            The value to assign to the to property of this RenameHeaderPolicyItem.
        :type to: str

        """
        self.swagger_types = {
            '_from': 'str',
            'to': 'str'
        }

        self.attribute_map = {
            '_from': 'from',
            'to': 'to'
        }

        self.__from = None
        self._to = None

    @property
    def _from(self):
        """
        **[Required]** Gets the _from of this RenameHeaderPolicyItem.
        The original case-insensitive name of the header.  This name must be unique across transformation policies.


        :return: The _from of this RenameHeaderPolicyItem.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this RenameHeaderPolicyItem.
        The original case-insensitive name of the header.  This name must be unique across transformation policies.


        :param _from: The _from of this RenameHeaderPolicyItem.
        :type: str
        """
        self.__from = _from

    @property
    def to(self):
        """
        **[Required]** Gets the to of this RenameHeaderPolicyItem.
        The new name of the header.  This name must be unique across transformation policies.


        :return: The to of this RenameHeaderPolicyItem.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this RenameHeaderPolicyItem.
        The new name of the header.  This name must be unique across transformation policies.


        :param to: The to of this RenameHeaderPolicyItem.
        :type: str
        """
        self._to = to

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
