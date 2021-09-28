# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchHistoryEntry(object):
    """
    PatchHistoryEntry model.
    """

    #: A constant which can be used with the action property of a PatchHistoryEntry.
    #: This constant has a value of "APPLY"
    ACTION_APPLY = "APPLY"

    #: A constant which can be used with the action property of a PatchHistoryEntry.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the lifecycle_state property of a PatchHistoryEntry.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a PatchHistoryEntry.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a PatchHistoryEntry.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchHistoryEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PatchHistoryEntry.
        :type id: str

        :param patch_id:
            The value to assign to the patch_id property of this PatchHistoryEntry.
        :type patch_id: str

        :param action:
            The value to assign to the action property of this PatchHistoryEntry.
            Allowed values for this property are: "APPLY", "PRECHECK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PatchHistoryEntry.
            Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PatchHistoryEntry.
        :type lifecycle_details: str

        :param time_started:
            The value to assign to the time_started property of this PatchHistoryEntry.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this PatchHistoryEntry.
        :type time_ended: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'patch_id': 'str',
            'action': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'patch_id': 'patchId',
            'action': 'action',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded'
        }

        self._id = None
        self._patch_id = None
        self._action = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_started = None
        self._time_ended = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PatchHistoryEntry.
        The `OCID`__ of the patch history entry.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PatchHistoryEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PatchHistoryEntry.
        The `OCID`__ of the patch history entry.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PatchHistoryEntry.
        :type: str
        """
        self._id = id

    @property
    def patch_id(self):
        """
        **[Required]** Gets the patch_id of this PatchHistoryEntry.
        The `OCID`__ of the patch.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The patch_id of this PatchHistoryEntry.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this PatchHistoryEntry.
        The `OCID`__ of the patch.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param patch_id: The patch_id of this PatchHistoryEntry.
        :type: str
        """
        self._patch_id = patch_id

    @property
    def action(self):
        """
        Gets the action of this PatchHistoryEntry.
        The action being performed or was completed.

        Allowed values for this property are: "APPLY", "PRECHECK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this PatchHistoryEntry.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PatchHistoryEntry.
        The action being performed or was completed.


        :param action: The action of this PatchHistoryEntry.
        :type: str
        """
        allowed_values = ["APPLY", "PRECHECK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PatchHistoryEntry.
        The current state of the action.

        Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PatchHistoryEntry.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PatchHistoryEntry.
        The current state of the action.


        :param lifecycle_state: The lifecycle_state of this PatchHistoryEntry.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PatchHistoryEntry.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text.


        :return: The lifecycle_details of this PatchHistoryEntry.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PatchHistoryEntry.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text.


        :param lifecycle_details: The lifecycle_details of this PatchHistoryEntry.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this PatchHistoryEntry.
        The date and time when the patch action started.


        :return: The time_started of this PatchHistoryEntry.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PatchHistoryEntry.
        The date and time when the patch action started.


        :param time_started: The time_started of this PatchHistoryEntry.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this PatchHistoryEntry.
        The date and time when the patch action completed


        :return: The time_ended of this PatchHistoryEntry.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this PatchHistoryEntry.
        The date and time when the patch action completed


        :param time_ended: The time_ended of this PatchHistoryEntry.
        :type: datetime
        """
        self._time_ended = time_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
