# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeReplicaDetails(object):
    """
    Contains the details for the boot volume replica
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeReplicaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this BootVolumeReplicaDetails.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this BootVolumeReplicaDetails.
        :type availability_domain: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'availability_domain': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain'
        }

        self._display_name = None
        self._availability_domain = None

    @property
    def display_name(self):
        """
        Gets the display_name of this BootVolumeReplicaDetails.
        The display name of the boot volume replica. You may optionally specify a *display name* for
        the boot volume replica, otherwise a default is provided.


        :return: The display_name of this BootVolumeReplicaDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BootVolumeReplicaDetails.
        The display name of the boot volume replica. You may optionally specify a *display name* for
        the boot volume replica, otherwise a default is provided.


        :param display_name: The display_name of this BootVolumeReplicaDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this BootVolumeReplicaDetails.
        The availability domain of the boot volume replica.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this BootVolumeReplicaDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this BootVolumeReplicaDetails.
        The availability domain of the boot volume replica.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this BootVolumeReplicaDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
