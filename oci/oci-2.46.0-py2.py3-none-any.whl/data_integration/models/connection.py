# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Connection(object):
    """
    The connection for a data asset.
    """

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "ORACLE_ADWC_CONNECTION"
    MODEL_TYPE_ORACLE_ADWC_CONNECTION = "ORACLE_ADWC_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "ORACLE_ATP_CONNECTION"
    MODEL_TYPE_ORACLE_ATP_CONNECTION = "ORACLE_ATP_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_CONNECTION"
    MODEL_TYPE_ORACLE_OBJECT_STORAGE_CONNECTION = "ORACLE_OBJECT_STORAGE_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "ORACLEDB_CONNECTION"
    MODEL_TYPE_ORACLEDB_CONNECTION = "ORACLEDB_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "MYSQL_CONNECTION"
    MODEL_TYPE_MYSQL_CONNECTION = "MYSQL_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "GENERIC_JDBC_CONNECTION"
    MODEL_TYPE_GENERIC_JDBC_CONNECTION = "GENERIC_JDBC_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "BICC_CONNECTION"
    MODEL_TYPE_BICC_CONNECTION = "BICC_CONNECTION"

    #: A constant which can be used with the model_type property of a Connection.
    #: This constant has a value of "AMAZON_S3_CONNECTION"
    MODEL_TYPE_AMAZON_S3_CONNECTION = "AMAZON_S3_CONNECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new Connection object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.ConnectionFromObjectStorage`
        * :class:`~oci.data_integration.models.ConnectionFromAdwc`
        * :class:`~oci.data_integration.models.ConnectionFromAtp`
        * :class:`~oci.data_integration.models.ConnectionFromOracle`
        * :class:`~oci.data_integration.models.ConnectionFromAmazonS3`
        * :class:`~oci.data_integration.models.ConnectionFromMySQL`
        * :class:`~oci.data_integration.models.ConnectionFromJdbc`
        * :class:`~oci.data_integration.models.ConnectionFromBICC`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Connection.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Connection.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Connection.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Connection.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Connection.
        :type name: str

        :param description:
            The value to assign to the description property of this Connection.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Connection.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this Connection.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Connection.
        :type identifier: str

        :param primary_schema:
            The value to assign to the primary_schema property of this Connection.
        :type primary_schema: oci.data_integration.models.Schema

        :param connection_properties:
            The value to assign to the connection_properties property of this Connection.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param is_default:
            The value to assign to the is_default property of this Connection.
        :type is_default: bool

        :param metadata:
            The value to assign to the metadata property of this Connection.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this Connection.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'primary_schema': 'Schema',
            'connection_properties': 'list[ConnectionProperty]',
            'is_default': 'bool',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'primary_schema': 'primarySchema',
            'connection_properties': 'connectionProperties',
            'is_default': 'isDefault',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._primary_schema = None
        self._connection_properties = None
        self._is_default = None
        self._metadata = None
        self._key_map = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'ORACLE_OBJECT_STORAGE_CONNECTION':
            return 'ConnectionFromObjectStorage'

        if type == 'ORACLE_ADWC_CONNECTION':
            return 'ConnectionFromAdwc'

        if type == 'ORACLE_ATP_CONNECTION':
            return 'ConnectionFromAtp'

        if type == 'ORACLEDB_CONNECTION':
            return 'ConnectionFromOracle'

        if type == 'AMAZON_S3_CONNECTION':
            return 'ConnectionFromAmazonS3'

        if type == 'MYSQL_CONNECTION':
            return 'ConnectionFromMySQL'

        if type == 'GENERIC_JDBC_CONNECTION':
            return 'ConnectionFromJdbc'

        if type == 'BICC_CONNECTION':
            return 'ConnectionFromBICC'
        else:
            return 'Connection'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this Connection.
        The type of the connection.

        Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this Connection.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Connection.
        The type of the connection.


        :param model_type: The model_type of this Connection.
        :type: str
        """
        allowed_values = ["ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this Connection.
        Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.


        :return: The key of this Connection.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Connection.
        Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.


        :param key: The key of this Connection.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this Connection.
        The model version of an object.


        :return: The model_version of this Connection.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Connection.
        The model version of an object.


        :param model_version: The model_version of this Connection.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Connection.

        :return: The parent_ref of this Connection.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Connection.

        :param parent_ref: The parent_ref of this Connection.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this Connection.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this Connection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Connection.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this Connection.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Connection.
        User-defined description for the connection.


        :return: The description of this Connection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Connection.
        User-defined description for the connection.


        :param description: The description of this Connection.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this Connection.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this Connection.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this Connection.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this Connection.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this Connection.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Connection.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Connection.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Connection.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this Connection.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this Connection.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Connection.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this Connection.
        :type: str
        """
        self._identifier = identifier

    @property
    def primary_schema(self):
        """
        Gets the primary_schema of this Connection.

        :return: The primary_schema of this Connection.
        :rtype: oci.data_integration.models.Schema
        """
        return self._primary_schema

    @primary_schema.setter
    def primary_schema(self, primary_schema):
        """
        Sets the primary_schema of this Connection.

        :param primary_schema: The primary_schema of this Connection.
        :type: oci.data_integration.models.Schema
        """
        self._primary_schema = primary_schema

    @property
    def connection_properties(self):
        """
        Gets the connection_properties of this Connection.
        The properties for the connection.


        :return: The connection_properties of this Connection.
        :rtype: list[oci.data_integration.models.ConnectionProperty]
        """
        return self._connection_properties

    @connection_properties.setter
    def connection_properties(self, connection_properties):
        """
        Sets the connection_properties of this Connection.
        The properties for the connection.


        :param connection_properties: The connection_properties of this Connection.
        :type: list[oci.data_integration.models.ConnectionProperty]
        """
        self._connection_properties = connection_properties

    @property
    def is_default(self):
        """
        Gets the is_default of this Connection.
        The default property for the connection.


        :return: The is_default of this Connection.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this Connection.
        The default property for the connection.


        :param is_default: The is_default of this Connection.
        :type: bool
        """
        self._is_default = is_default

    @property
    def metadata(self):
        """
        Gets the metadata of this Connection.

        :return: The metadata of this Connection.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Connection.

        :param metadata: The metadata of this Connection.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this Connection.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this Connection.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this Connection.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this Connection.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
