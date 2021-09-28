# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DhcpOptions(object):
    """
    A set of DHCP options. Used by the VCN to automatically provide configuration
    information to the instances when they boot up. There are two options you can set:

    - :class:`DhcpDnsOption`: Lets you specify how DNS (hostname resolution) is
    handled in the subnets in your VCN.

    - :class:`DhcpSearchDomainOption`: Lets you specify
    a search domain name to use for DNS queries.

    For more information, see  `DNS in Your Virtual Cloud Network`__
    and `DHCP Options`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a DhcpOptions.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DhcpOptions.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DhcpOptions.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DhcpOptions.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the domain_name_type property of a DhcpOptions.
    #: This constant has a value of "SUBNET_DOMAIN"
    DOMAIN_NAME_TYPE_SUBNET_DOMAIN = "SUBNET_DOMAIN"

    #: A constant which can be used with the domain_name_type property of a DhcpOptions.
    #: This constant has a value of "VCN_DOMAIN"
    DOMAIN_NAME_TYPE_VCN_DOMAIN = "VCN_DOMAIN"

    #: A constant which can be used with the domain_name_type property of a DhcpOptions.
    #: This constant has a value of "CUSTOM_DOMAIN"
    DOMAIN_NAME_TYPE_CUSTOM_DOMAIN = "CUSTOM_DOMAIN"

    def __init__(self, **kwargs):
        """
        Initializes a new DhcpOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DhcpOptions.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DhcpOptions.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this DhcpOptions.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DhcpOptions.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this DhcpOptions.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DhcpOptions.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param options:
            The value to assign to the options property of this DhcpOptions.
        :type options: list[oci.core.models.DhcpOption]

        :param time_created:
            The value to assign to the time_created property of this DhcpOptions.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this DhcpOptions.
        :type vcn_id: str

        :param domain_name_type:
            The value to assign to the domain_name_type property of this DhcpOptions.
            Allowed values for this property are: "SUBNET_DOMAIN", "VCN_DOMAIN", "CUSTOM_DOMAIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type domain_name_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'options': 'list[DhcpOption]',
            'time_created': 'datetime',
            'vcn_id': 'str',
            'domain_name_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'options': 'options',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId',
            'domain_name_type': 'domainNameType'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._options = None
        self._time_created = None
        self._vcn_id = None
        self._domain_name_type = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DhcpOptions.
        The OCID of the compartment containing the set of DHCP options.


        :return: The compartment_id of this DhcpOptions.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DhcpOptions.
        The OCID of the compartment containing the set of DHCP options.


        :param compartment_id: The compartment_id of this DhcpOptions.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DhcpOptions.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DhcpOptions.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DhcpOptions.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DhcpOptions.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this DhcpOptions.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DhcpOptions.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DhcpOptions.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DhcpOptions.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DhcpOptions.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DhcpOptions.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DhcpOptions.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DhcpOptions.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DhcpOptions.
        Oracle ID (OCID) for the set of DHCP options.


        :return: The id of this DhcpOptions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DhcpOptions.
        Oracle ID (OCID) for the set of DHCP options.


        :param id: The id of this DhcpOptions.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DhcpOptions.
        The current state of the set of DHCP options.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DhcpOptions.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DhcpOptions.
        The current state of the set of DHCP options.


        :param lifecycle_state: The lifecycle_state of this DhcpOptions.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def options(self):
        """
        **[Required]** Gets the options of this DhcpOptions.
        The collection of individual DHCP options.


        :return: The options of this DhcpOptions.
        :rtype: list[oci.core.models.DhcpOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this DhcpOptions.
        The collection of individual DHCP options.


        :param options: The options of this DhcpOptions.
        :type: list[oci.core.models.DhcpOption]
        """
        self._options = options

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DhcpOptions.
        Date and time the set of DHCP options was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DhcpOptions.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DhcpOptions.
        Date and time the set of DHCP options was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DhcpOptions.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DhcpOptions.
        The OCID of the VCN the set of DHCP options belongs to.


        :return: The vcn_id of this DhcpOptions.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DhcpOptions.
        The OCID of the VCN the set of DHCP options belongs to.


        :param vcn_id: The vcn_id of this DhcpOptions.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def domain_name_type(self):
        """
        Gets the domain_name_type of this DhcpOptions.
        The search domain name type of DHCP options

        Allowed values for this property are: "SUBNET_DOMAIN", "VCN_DOMAIN", "CUSTOM_DOMAIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The domain_name_type of this DhcpOptions.
        :rtype: str
        """
        return self._domain_name_type

    @domain_name_type.setter
    def domain_name_type(self, domain_name_type):
        """
        Sets the domain_name_type of this DhcpOptions.
        The search domain name type of DHCP options


        :param domain_name_type: The domain_name_type of this DhcpOptions.
        :type: str
        """
        allowed_values = ["SUBNET_DOMAIN", "VCN_DOMAIN", "CUSTOM_DOMAIN"]
        if not value_allowed_none_or_none_sentinel(domain_name_type, allowed_values):
            domain_name_type = 'UNKNOWN_ENUM_VALUE'
        self._domain_name_type = domain_name_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
