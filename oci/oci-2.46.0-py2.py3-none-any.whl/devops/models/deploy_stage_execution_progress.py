# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployStageExecutionProgress(object):
    """
    Details about the execution progress of a stage in a deployment.
    """

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "ROLLBACK_IN_PROGRESS"
    STATUS_ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "ROLLBACK_SUCCEEDED"
    STATUS_ROLLBACK_SUCCEEDED = "ROLLBACK_SUCCEEDED"

    #: A constant which can be used with the status property of a DeployStageExecutionProgress.
    #: This constant has a value of "ROLLBACK_FAILED"
    STATUS_ROLLBACK_FAILED = "ROLLBACK_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployStageExecutionProgress object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress`
        * :class:`~oci.devops.models.ComputeInstanceGroupCanaryDeployStageExecutionProgress`
        * :class:`~oci.devops.models.ComputeInstanceGroupDeployStageExecutionProgress`
        * :class:`~oci.devops.models.LoadBalancerTrafficShiftDeployStageExecutionProgress`
        * :class:`~oci.devops.models.WaitDeployStageExecutionProgress`
        * :class:`~oci.devops.models.ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress`
        * :class:`~oci.devops.models.RunValidationTestOnComputeInstanceDeployStageExecutionProgress`
        * :class:`~oci.devops.models.ManualApprovalDeployStageExecutionProgress`
        * :class:`~oci.devops.models.RunPipelineDeployStageExecutionProgress`
        * :class:`~oci.devops.models.OkeDeployStageExecutionProgress`
        * :class:`~oci.devops.models.FunctionDeployStageExecutionProgress`
        * :class:`~oci.devops.models.InvokeFunctionDeployStageExecutionProgress`
        * :class:`~oci.devops.models.ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress`
        * :class:`~oci.devops.models.ComputeInstanceGroupBlueGreenDeployStageExecutionProgress`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_stage_display_name:
            The value to assign to the deploy_stage_display_name property of this DeployStageExecutionProgress.
        :type deploy_stage_display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this DeployStageExecutionProgress.
        :type deploy_stage_type: str

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this DeployStageExecutionProgress.
        :type deploy_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this DeployStageExecutionProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this DeployStageExecutionProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this DeployStageExecutionProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "ROLLBACK_IN_PROGRESS", "ROLLBACK_SUCCEEDED", "ROLLBACK_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param deploy_stage_predecessors:
            The value to assign to the deploy_stage_predecessors property of this DeployStageExecutionProgress.
        :type deploy_stage_predecessors: oci.devops.models.DeployStagePredecessorCollection

        :param deploy_stage_execution_progress_details:
            The value to assign to the deploy_stage_execution_progress_details property of this DeployStageExecutionProgress.
        :type deploy_stage_execution_progress_details: list[oci.devops.models.DeployStageExecutionProgressDetails]

        """
        self.swagger_types = {
            'deploy_stage_display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'deploy_stage_predecessors': 'DeployStagePredecessorCollection',
            'deploy_stage_execution_progress_details': 'list[DeployStageExecutionProgressDetails]'
        }

        self.attribute_map = {
            'deploy_stage_display_name': 'deployStageDisplayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_id': 'deployStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'deploy_stage_predecessors': 'deployStagePredecessors',
            'deploy_stage_execution_progress_details': 'deployStageExecutionProgressDetails'
        }

        self._deploy_stage_display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._deploy_stage_predecessors = None
        self._deploy_stage_execution_progress_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deployStageType']

        if type == 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT':
            return 'ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT':
            return 'ComputeInstanceGroupCanaryDeployStageExecutionProgress'

        if type == 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT':
            return 'ComputeInstanceGroupDeployStageExecutionProgress'

        if type == 'LOAD_BALANCER_TRAFFIC_SHIFT':
            return 'LoadBalancerTrafficShiftDeployStageExecutionProgress'

        if type == 'WAIT':
            return 'WaitDeployStageExecutionProgress'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT':
            return 'ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress'

        if type == 'RUN_VALIDATION_TEST_ON_COMPUTE_INSTANCE':
            return 'RunValidationTestOnComputeInstanceDeployStageExecutionProgress'

        if type == 'MANUAL_APPROVAL':
            return 'ManualApprovalDeployStageExecutionProgress'

        if type == 'RUN_DEPLOYMENT_PIPELINE':
            return 'RunPipelineDeployStageExecutionProgress'

        if type == 'OKE_DEPLOYMENT':
            return 'OkeDeployStageExecutionProgress'

        if type == 'DEPLOY_FUNCTION':
            return 'FunctionDeployStageExecutionProgress'

        if type == 'INVOKE_FUNCTION':
            return 'InvokeFunctionDeployStageExecutionProgress'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL':
            return 'ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress'

        if type == 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT':
            return 'ComputeInstanceGroupBlueGreenDeployStageExecutionProgress'
        else:
            return 'DeployStageExecutionProgress'

    @property
    def deploy_stage_display_name(self):
        """
        Gets the deploy_stage_display_name of this DeployStageExecutionProgress.
        Stage display name. Avoid entering confidential information.


        :return: The deploy_stage_display_name of this DeployStageExecutionProgress.
        :rtype: str
        """
        return self._deploy_stage_display_name

    @deploy_stage_display_name.setter
    def deploy_stage_display_name(self, deploy_stage_display_name):
        """
        Sets the deploy_stage_display_name of this DeployStageExecutionProgress.
        Stage display name. Avoid entering confidential information.


        :param deploy_stage_display_name: The deploy_stage_display_name of this DeployStageExecutionProgress.
        :type: str
        """
        self._deploy_stage_display_name = deploy_stage_display_name

    @property
    def deploy_stage_type(self):
        """
        Gets the deploy_stage_type of this DeployStageExecutionProgress.
        Deployment stage type.


        :return: The deploy_stage_type of this DeployStageExecutionProgress.
        :rtype: str
        """
        return self._deploy_stage_type

    @deploy_stage_type.setter
    def deploy_stage_type(self, deploy_stage_type):
        """
        Sets the deploy_stage_type of this DeployStageExecutionProgress.
        Deployment stage type.


        :param deploy_stage_type: The deploy_stage_type of this DeployStageExecutionProgress.
        :type: str
        """
        self._deploy_stage_type = deploy_stage_type

    @property
    def deploy_stage_id(self):
        """
        Gets the deploy_stage_id of this DeployStageExecutionProgress.
        The OCID of the stage.


        :return: The deploy_stage_id of this DeployStageExecutionProgress.
        :rtype: str
        """
        return self._deploy_stage_id

    @deploy_stage_id.setter
    def deploy_stage_id(self, deploy_stage_id):
        """
        Sets the deploy_stage_id of this DeployStageExecutionProgress.
        The OCID of the stage.


        :param deploy_stage_id: The deploy_stage_id of this DeployStageExecutionProgress.
        :type: str
        """
        self._deploy_stage_id = deploy_stage_id

    @property
    def time_started(self):
        """
        Gets the time_started of this DeployStageExecutionProgress.
        Time the stage started executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_started of this DeployStageExecutionProgress.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DeployStageExecutionProgress.
        Time the stage started executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_started: The time_started of this DeployStageExecutionProgress.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this DeployStageExecutionProgress.
        Time the stage finished executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_finished of this DeployStageExecutionProgress.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this DeployStageExecutionProgress.
        Time the stage finished executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_finished: The time_finished of this DeployStageExecutionProgress.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def status(self):
        """
        Gets the status of this DeployStageExecutionProgress.
        The current state of the stage.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "ROLLBACK_IN_PROGRESS", "ROLLBACK_SUCCEEDED", "ROLLBACK_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DeployStageExecutionProgress.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DeployStageExecutionProgress.
        The current state of the stage.


        :param status: The status of this DeployStageExecutionProgress.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "ROLLBACK_IN_PROGRESS", "ROLLBACK_SUCCEEDED", "ROLLBACK_FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def deploy_stage_predecessors(self):
        """
        Gets the deploy_stage_predecessors of this DeployStageExecutionProgress.

        :return: The deploy_stage_predecessors of this DeployStageExecutionProgress.
        :rtype: oci.devops.models.DeployStagePredecessorCollection
        """
        return self._deploy_stage_predecessors

    @deploy_stage_predecessors.setter
    def deploy_stage_predecessors(self, deploy_stage_predecessors):
        """
        Sets the deploy_stage_predecessors of this DeployStageExecutionProgress.

        :param deploy_stage_predecessors: The deploy_stage_predecessors of this DeployStageExecutionProgress.
        :type: oci.devops.models.DeployStagePredecessorCollection
        """
        self._deploy_stage_predecessors = deploy_stage_predecessors

    @property
    def deploy_stage_execution_progress_details(self):
        """
        Gets the deploy_stage_execution_progress_details of this DeployStageExecutionProgress.
        Details about stage execution for all the target environments.


        :return: The deploy_stage_execution_progress_details of this DeployStageExecutionProgress.
        :rtype: list[oci.devops.models.DeployStageExecutionProgressDetails]
        """
        return self._deploy_stage_execution_progress_details

    @deploy_stage_execution_progress_details.setter
    def deploy_stage_execution_progress_details(self, deploy_stage_execution_progress_details):
        """
        Sets the deploy_stage_execution_progress_details of this DeployStageExecutionProgress.
        Details about stage execution for all the target environments.


        :param deploy_stage_execution_progress_details: The deploy_stage_execution_progress_details of this DeployStageExecutionProgress.
        :type: list[oci.devops.models.DeployStageExecutionProgressDetails]
        """
        self._deploy_stage_execution_progress_details = deploy_stage_execution_progress_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
