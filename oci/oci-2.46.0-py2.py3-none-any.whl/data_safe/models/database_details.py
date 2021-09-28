# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseDetails(object):
    """
    Details of the database for the registration in Data Safe.
    To choose applicable database type and infrastructure type refer to
    https://confluence.oci.oraclecorp.com/display/DATASAFE/Target+V2+Design
    """

    #: A constant which can be used with the database_type property of a DatabaseDetails.
    #: This constant has a value of "DATABASE_CLOUD_SERVICE"
    DATABASE_TYPE_DATABASE_CLOUD_SERVICE = "DATABASE_CLOUD_SERVICE"

    #: A constant which can be used with the database_type property of a DatabaseDetails.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    DATABASE_TYPE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    #: A constant which can be used with the database_type property of a DatabaseDetails.
    #: This constant has a value of "INSTALLED_DATABASE"
    DATABASE_TYPE_INSTALLED_DATABASE = "INSTALLED_DATABASE"

    #: A constant which can be used with the infrastructure_type property of a DatabaseDetails.
    #: This constant has a value of "ORACLE_CLOUD"
    INFRASTRUCTURE_TYPE_ORACLE_CLOUD = "ORACLE_CLOUD"

    #: A constant which can be used with the infrastructure_type property of a DatabaseDetails.
    #: This constant has a value of "CLOUD_AT_CUSTOMER"
    INFRASTRUCTURE_TYPE_CLOUD_AT_CUSTOMER = "CLOUD_AT_CUSTOMER"

    #: A constant which can be used with the infrastructure_type property of a DatabaseDetails.
    #: This constant has a value of "ON_PREMISES"
    INFRASTRUCTURE_TYPE_ON_PREMISES = "ON_PREMISES"

    #: A constant which can be used with the infrastructure_type property of a DatabaseDetails.
    #: This constant has a value of "NON_ORACLE_CLOUD"
    INFRASTRUCTURE_TYPE_NON_ORACLE_CLOUD = "NON_ORACLE_CLOUD"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.InstalledDatabaseDetails`
        * :class:`~oci.data_safe.models.AutonomousDatabaseDetails`
        * :class:`~oci.data_safe.models.DatabaseCloudServiceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_type:
            The value to assign to the database_type property of this DatabaseDetails.
            Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this DatabaseDetails.
            Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type infrastructure_type: str

        """
        self.swagger_types = {
            'database_type': 'str',
            'infrastructure_type': 'str'
        }

        self.attribute_map = {
            'database_type': 'databaseType',
            'infrastructure_type': 'infrastructureType'
        }

        self._database_type = None
        self._infrastructure_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['databaseType']

        if type == 'INSTALLED_DATABASE':
            return 'InstalledDatabaseDetails'

        if type == 'AUTONOMOUS_DATABASE':
            return 'AutonomousDatabaseDetails'

        if type == 'DATABASE_CLOUD_SERVICE':
            return 'DatabaseCloudServiceDetails'
        else:
            return 'DatabaseDetails'

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this DatabaseDetails.
        The database type.

        Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this DatabaseDetails.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseDetails.
        The database type.


        :param database_type: The database_type of this DatabaseDetails.
        :type: str
        """
        allowed_values = ["DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def infrastructure_type(self):
        """
        **[Required]** Gets the infrastructure_type of this DatabaseDetails.
        The infrastructure type the database is running on.

        Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The infrastructure_type of this DatabaseDetails.
        :rtype: str
        """
        return self._infrastructure_type

    @infrastructure_type.setter
    def infrastructure_type(self, infrastructure_type):
        """
        Sets the infrastructure_type of this DatabaseDetails.
        The infrastructure type the database is running on.


        :param infrastructure_type: The infrastructure_type of this DatabaseDetails.
        :type: str
        """
        allowed_values = ["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]
        if not value_allowed_none_or_none_sentinel(infrastructure_type, allowed_values):
            infrastructure_type = 'UNKNOWN_ENUM_VALUE'
        self._infrastructure_type = infrastructure_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
