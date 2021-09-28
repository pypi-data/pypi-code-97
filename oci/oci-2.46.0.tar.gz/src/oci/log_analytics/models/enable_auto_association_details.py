# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableAutoAssociationDetails(object):
    """
    The information required to enable log source auto-association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableAutoAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this EnableAutoAssociationDetails.
        :type items: list[oci.log_analytics.models.EnableAutoAssociationDetail]

        """
        self.swagger_types = {
            'items': 'list[EnableAutoAssociationDetail]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        Gets the items of this EnableAutoAssociationDetails.
        A list of information required to enable auto association on a source.


        :return: The items of this EnableAutoAssociationDetails.
        :rtype: list[oci.log_analytics.models.EnableAutoAssociationDetail]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this EnableAutoAssociationDetails.
        A list of information required to enable auto association on a source.


        :param items: The items of this EnableAutoAssociationDetails.
        :type: list[oci.log_analytics.models.EnableAutoAssociationDetail]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
