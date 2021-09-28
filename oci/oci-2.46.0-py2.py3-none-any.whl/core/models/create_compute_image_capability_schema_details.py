# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeImageCapabilitySchemaDetails(object):
    """
    Create Image Capability Schema for an image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeImageCapabilitySchemaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateComputeImageCapabilitySchemaDetails.
        :type compartment_id: str

        :param compute_global_image_capability_schema_version_name:
            The value to assign to the compute_global_image_capability_schema_version_name property of this CreateComputeImageCapabilitySchemaDetails.
        :type compute_global_image_capability_schema_version_name: str

        :param image_id:
            The value to assign to the image_id property of this CreateComputeImageCapabilitySchemaDetails.
        :type image_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateComputeImageCapabilitySchemaDetails.
        :type freeform_tags: dict(str, str)

        :param display_name:
            The value to assign to the display_name property of this CreateComputeImageCapabilitySchemaDetails.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateComputeImageCapabilitySchemaDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param schema_data:
            The value to assign to the schema_data property of this CreateComputeImageCapabilitySchemaDetails.
        :type schema_data: dict(str, ImageCapabilitySchemaDescriptor)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'compute_global_image_capability_schema_version_name': 'str',
            'image_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'schema_data': 'dict(str, ImageCapabilitySchemaDescriptor)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'compute_global_image_capability_schema_version_name': 'computeGlobalImageCapabilitySchemaVersionName',
            'image_id': 'imageId',
            'freeform_tags': 'freeformTags',
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'schema_data': 'schemaData'
        }

        self._compartment_id = None
        self._compute_global_image_capability_schema_version_name = None
        self._image_id = None
        self._freeform_tags = None
        self._display_name = None
        self._defined_tags = None
        self._schema_data = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateComputeImageCapabilitySchemaDetails.
        The OCID of the compartment that contains the resource.


        :return: The compartment_id of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateComputeImageCapabilitySchemaDetails.
        The OCID of the compartment that contains the resource.


        :param compartment_id: The compartment_id of this CreateComputeImageCapabilitySchemaDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compute_global_image_capability_schema_version_name(self):
        """
        **[Required]** Gets the compute_global_image_capability_schema_version_name of this CreateComputeImageCapabilitySchemaDetails.
        The name of the compute global image capability schema version


        :return: The compute_global_image_capability_schema_version_name of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: str
        """
        return self._compute_global_image_capability_schema_version_name

    @compute_global_image_capability_schema_version_name.setter
    def compute_global_image_capability_schema_version_name(self, compute_global_image_capability_schema_version_name):
        """
        Sets the compute_global_image_capability_schema_version_name of this CreateComputeImageCapabilitySchemaDetails.
        The name of the compute global image capability schema version


        :param compute_global_image_capability_schema_version_name: The compute_global_image_capability_schema_version_name of this CreateComputeImageCapabilitySchemaDetails.
        :type: str
        """
        self._compute_global_image_capability_schema_version_name = compute_global_image_capability_schema_version_name

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this CreateComputeImageCapabilitySchemaDetails.
        The ocid of the image


        :return: The image_id of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this CreateComputeImageCapabilitySchemaDetails.
        The ocid of the image


        :param image_id: The image_id of this CreateComputeImageCapabilitySchemaDetails.
        :type: str
        """
        self._image_id = image_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateComputeImageCapabilitySchemaDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateComputeImageCapabilitySchemaDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateComputeImageCapabilitySchemaDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateComputeImageCapabilitySchemaDetails.
        A user-friendly name for the compute image capability schema


        :return: The display_name of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateComputeImageCapabilitySchemaDetails.
        A user-friendly name for the compute image capability schema


        :param display_name: The display_name of this CreateComputeImageCapabilitySchemaDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateComputeImageCapabilitySchemaDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateComputeImageCapabilitySchemaDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateComputeImageCapabilitySchemaDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def schema_data(self):
        """
        **[Required]** Gets the schema_data of this CreateComputeImageCapabilitySchemaDetails.
        The map of each capability name to its ImageCapabilitySchemaDescriptor.


        :return: The schema_data of this CreateComputeImageCapabilitySchemaDetails.
        :rtype: dict(str, ImageCapabilitySchemaDescriptor)
        """
        return self._schema_data

    @schema_data.setter
    def schema_data(self, schema_data):
        """
        Sets the schema_data of this CreateComputeImageCapabilitySchemaDetails.
        The map of each capability name to its ImageCapabilitySchemaDescriptor.


        :param schema_data: The schema_data of this CreateComputeImageCapabilitySchemaDetails.
        :type: dict(str, ImageCapabilitySchemaDescriptor)
        """
        self._schema_data = schema_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
