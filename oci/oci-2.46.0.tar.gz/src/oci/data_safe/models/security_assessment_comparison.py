# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAssessmentComparison(object):
    """
    Provides a list of the differences in a comparison of the security assessment with the baseline value.
    """

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessmentComparison.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessmentComparison.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessmentComparison.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAssessmentComparison object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SecurityAssessmentComparison.
        :type id: str

        :param baseline_id:
            The value to assign to the baseline_id property of this SecurityAssessmentComparison.
        :type baseline_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityAssessmentComparison.
            Allowed values for this property are: "CREATING", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this SecurityAssessmentComparison.
        :type time_created: datetime

        :param targets:
            The value to assign to the targets property of this SecurityAssessmentComparison.
        :type targets: list[oci.data_safe.models.SecurityAssessmentComparisonPerTarget]

        """
        self.swagger_types = {
            'id': 'str',
            'baseline_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'targets': 'list[SecurityAssessmentComparisonPerTarget]'
        }

        self.attribute_map = {
            'id': 'id',
            'baseline_id': 'baselineId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'targets': 'targets'
        }

        self._id = None
        self._baseline_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._targets = None

    @property
    def id(self):
        """
        Gets the id of this SecurityAssessmentComparison.
        The OCID of the security assessment that is being compared with a baseline security assessment.


        :return: The id of this SecurityAssessmentComparison.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityAssessmentComparison.
        The OCID of the security assessment that is being compared with a baseline security assessment.


        :param id: The id of this SecurityAssessmentComparison.
        :type: str
        """
        self._id = id

    @property
    def baseline_id(self):
        """
        Gets the baseline_id of this SecurityAssessmentComparison.
        The OCID of the security assessment that is set as a baseline.


        :return: The baseline_id of this SecurityAssessmentComparison.
        :rtype: str
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        """
        Sets the baseline_id of this SecurityAssessmentComparison.
        The OCID of the security assessment that is set as a baseline.


        :param baseline_id: The baseline_id of this SecurityAssessmentComparison.
        :type: str
        """
        self._baseline_id = baseline_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SecurityAssessmentComparison.
        The current state of the security assessment comparison.

        Allowed values for this property are: "CREATING", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SecurityAssessmentComparison.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityAssessmentComparison.
        The current state of the security assessment comparison.


        :param lifecycle_state: The lifecycle_state of this SecurityAssessmentComparison.
        :type: str
        """
        allowed_values = ["CREATING", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SecurityAssessmentComparison.
        The date and time when the security assessment comparison was created. Conforms to the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SecurityAssessmentComparison.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityAssessmentComparison.
        The date and time when the security assessment comparison was created. Conforms to the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SecurityAssessmentComparison.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def targets(self):
        """
        Gets the targets of this SecurityAssessmentComparison.
        A target-based comparison between two security assessments.


        :return: The targets of this SecurityAssessmentComparison.
        :rtype: list[oci.data_safe.models.SecurityAssessmentComparisonPerTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this SecurityAssessmentComparison.
        A target-based comparison between two security assessments.


        :param targets: The targets of this SecurityAssessmentComparison.
        :type: list[oci.data_safe.models.SecurityAssessmentComparisonPerTarget]
        """
        self._targets = targets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
