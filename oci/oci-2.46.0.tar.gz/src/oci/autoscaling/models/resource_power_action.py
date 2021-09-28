# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .resource_action import ResourceAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourcePowerAction(ResourceAction):
    """
    A power action against a resource.
    """

    #: A constant which can be used with the action property of a ResourcePowerAction.
    #: This constant has a value of "STOP"
    ACTION_STOP = "STOP"

    #: A constant which can be used with the action property of a ResourcePowerAction.
    #: This constant has a value of "START"
    ACTION_START = "START"

    #: A constant which can be used with the action property of a ResourcePowerAction.
    #: This constant has a value of "SOFTRESET"
    ACTION_SOFTRESET = "SOFTRESET"

    #: A constant which can be used with the action property of a ResourcePowerAction.
    #: This constant has a value of "RESET"
    ACTION_RESET = "RESET"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourcePowerAction object with values from keyword arguments. The default value of the :py:attr:`~oci.autoscaling.models.ResourcePowerAction.action_type` attribute
        of this class is ``power`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this ResourcePowerAction.
        :type action_type: str

        :param action:
            The value to assign to the action property of this ResourcePowerAction.
            Allowed values for this property are: "STOP", "START", "SOFTRESET", "RESET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'action': 'action'
        }

        self._action_type = None
        self._action = None
        self._action_type = 'power'

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ResourcePowerAction.
        Allowed values for this property are: "STOP", "START", "SOFTRESET", "RESET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ResourcePowerAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ResourcePowerAction.

        :param action: The action of this ResourcePowerAction.
        :type: str
        """
        allowed_values = ["STOP", "START", "SOFTRESET", "RESET"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
