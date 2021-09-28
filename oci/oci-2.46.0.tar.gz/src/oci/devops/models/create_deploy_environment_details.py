# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeployEnvironmentDetails(object):
    """
    The information about new deployment environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeployEnvironmentDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.CreateComputeInstanceGroupDeployEnvironmentDetails`
        * :class:`~oci.devops.models.CreateOkeClusterDeployEnvironmentDetails`
        * :class:`~oci.devops.models.CreateFunctionDeployEnvironmentDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateDeployEnvironmentDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateDeployEnvironmentDetails.
        :type display_name: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this CreateDeployEnvironmentDetails.
        :type deploy_environment_type: str

        :param project_id:
            The value to assign to the project_id property of this CreateDeployEnvironmentDetails.
        :type project_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeployEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeployEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_environment_type': 'str',
            'project_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_environment_type': 'deployEnvironmentType',
            'project_id': 'projectId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._deploy_environment_type = None
        self._project_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deployEnvironmentType']

        if type == 'COMPUTE_INSTANCE_GROUP':
            return 'CreateComputeInstanceGroupDeployEnvironmentDetails'

        if type == 'OKE_CLUSTER':
            return 'CreateOkeClusterDeployEnvironmentDetails'

        if type == 'FUNCTION':
            return 'CreateFunctionDeployEnvironmentDetails'
        else:
            return 'CreateDeployEnvironmentDetails'

    @property
    def description(self):
        """
        Gets the description of this CreateDeployEnvironmentDetails.
        Optional description about the deployment environment.


        :return: The description of this CreateDeployEnvironmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDeployEnvironmentDetails.
        Optional description about the deployment environment.


        :param description: The description of this CreateDeployEnvironmentDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDeployEnvironmentDetails.
        Deployment environment display name. Avoid entering confidential information.


        :return: The display_name of this CreateDeployEnvironmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDeployEnvironmentDetails.
        Deployment environment display name. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDeployEnvironmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def deploy_environment_type(self):
        """
        **[Required]** Gets the deploy_environment_type of this CreateDeployEnvironmentDetails.
        Deployment environment type.


        :return: The deploy_environment_type of this CreateDeployEnvironmentDetails.
        :rtype: str
        """
        return self._deploy_environment_type

    @deploy_environment_type.setter
    def deploy_environment_type(self, deploy_environment_type):
        """
        Sets the deploy_environment_type of this CreateDeployEnvironmentDetails.
        Deployment environment type.


        :param deploy_environment_type: The deploy_environment_type of this CreateDeployEnvironmentDetails.
        :type: str
        """
        self._deploy_environment_type = deploy_environment_type

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateDeployEnvironmentDetails.
        The OCID of a project.


        :return: The project_id of this CreateDeployEnvironmentDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateDeployEnvironmentDetails.
        The OCID of a project.


        :param project_id: The project_id of this CreateDeployEnvironmentDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDeployEnvironmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDeployEnvironmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDeployEnvironmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDeployEnvironmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDeployEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDeployEnvironmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDeployEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDeployEnvironmentDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
