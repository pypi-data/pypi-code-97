"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated bag](https://www.ncbi.nlm.nih.gov/datasets/docs/rehydrate/), and retrieve the individual data files at a later time.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ncbi.datasets.openapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from ncbi.datasets.openapi.exceptions import ApiAttributeError


def lazy_import():
    from ncbi.datasets.openapi.model.v1_organism_count_by_type import V1OrganismCountByType
    from ncbi.datasets.openapi.model.v1_organism_counts import V1OrganismCounts
    from ncbi.datasets.openapi.model.v1_organism_rank_type import V1OrganismRankType
    globals()['V1OrganismCountByType'] = V1OrganismCountByType
    globals()['V1OrganismCounts'] = V1OrganismCounts
    globals()['V1OrganismRankType'] = V1OrganismRankType


class V1Organism(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'tax_id': (str,),  # noqa: E501
            'sci_name': (str,),  # noqa: E501
            'common_name': (str,),  # noqa: E501
            'blast_node': (bool,),  # noqa: E501
            'breed': (str,),  # noqa: E501
            'cultivar': (str,),  # noqa: E501
            'ecotype': (str,),  # noqa: E501
            'isolate': (str,),  # noqa: E501
            'sex': (str,),  # noqa: E501
            'strain': (str,),  # noqa: E501
            'search_text': ([str],),  # noqa: E501
            'rank': (V1OrganismRankType,),  # noqa: E501
            'parent_tax_id': (str,),  # noqa: E501
            'assembly_count': (str,),  # noqa: E501
            'assembly_counts': (V1OrganismCounts,),  # noqa: E501
            'counts': ([V1OrganismCountByType],),  # noqa: E501
            'children': ([V1Organism],),  # noqa: E501
            'merged': ([V1Organism],),  # noqa: E501
            'merged_tax_ids': ([str],),  # noqa: E501
            'min_ord': (int,),  # noqa: E501
            'max_ord': (int,),  # noqa: E501
            'weight': (int,),  # noqa: E501
            'key': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'icon': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tax_id': 'tax_id',  # noqa: E501
        'sci_name': 'sci_name',  # noqa: E501
        'common_name': 'common_name',  # noqa: E501
        'blast_node': 'blast_node',  # noqa: E501
        'breed': 'breed',  # noqa: E501
        'cultivar': 'cultivar',  # noqa: E501
        'ecotype': 'ecotype',  # noqa: E501
        'isolate': 'isolate',  # noqa: E501
        'sex': 'sex',  # noqa: E501
        'strain': 'strain',  # noqa: E501
        'search_text': 'search_text',  # noqa: E501
        'rank': 'rank',  # noqa: E501
        'parent_tax_id': 'parent_tax_id',  # noqa: E501
        'assembly_count': 'assembly_count',  # noqa: E501
        'assembly_counts': 'assembly_counts',  # noqa: E501
        'counts': 'counts',  # noqa: E501
        'children': 'children',  # noqa: E501
        'merged': 'merged',  # noqa: E501
        'merged_tax_ids': 'merged_tax_ids',  # noqa: E501
        'min_ord': 'min_ord',  # noqa: E501
        'max_ord': 'max_ord',  # noqa: E501
        'weight': 'weight',  # noqa: E501
        'key': 'key',  # noqa: E501
        'title': 'title',  # noqa: E501
        'icon': 'icon',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V1Organism - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            tax_id (str): [optional]  # noqa: E501
            sci_name (str): [optional]  # noqa: E501
            common_name (str): [optional]  # noqa: E501
            blast_node (bool): [optional]  # noqa: E501
            breed (str): [optional]  # noqa: E501
            cultivar (str): [optional]  # noqa: E501
            ecotype (str): [optional]  # noqa: E501
            isolate (str): [optional]  # noqa: E501
            sex (str): [optional]  # noqa: E501
            strain (str): [optional]  # noqa: E501
            search_text ([str]): [optional]  # noqa: E501
            rank (V1OrganismRankType): [optional]  # noqa: E501
            parent_tax_id (str): [optional]  # noqa: E501
            assembly_count (str): [optional]  # noqa: E501
            assembly_counts (V1OrganismCounts): [optional]  # noqa: E501
            counts ([V1OrganismCountByType]): [optional]  # noqa: E501
            children ([V1Organism]): [optional]  # noqa: E501
            merged ([V1Organism]): [optional]  # noqa: E501
            merged_tax_ids ([str]): [optional]  # noqa: E501
            min_ord (int): [optional]  # noqa: E501
            max_ord (int): [optional]  # noqa: E501
            weight (int): [optional]  # noqa: E501
            key (str): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            icon (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V1Organism - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            tax_id (str): [optional]  # noqa: E501
            sci_name (str): [optional]  # noqa: E501
            common_name (str): [optional]  # noqa: E501
            blast_node (bool): [optional]  # noqa: E501
            breed (str): [optional]  # noqa: E501
            cultivar (str): [optional]  # noqa: E501
            ecotype (str): [optional]  # noqa: E501
            isolate (str): [optional]  # noqa: E501
            sex (str): [optional]  # noqa: E501
            strain (str): [optional]  # noqa: E501
            search_text ([str]): [optional]  # noqa: E501
            rank (V1OrganismRankType): [optional]  # noqa: E501
            parent_tax_id (str): [optional]  # noqa: E501
            assembly_count (str): [optional]  # noqa: E501
            assembly_counts (V1OrganismCounts): [optional]  # noqa: E501
            counts ([V1OrganismCountByType]): [optional]  # noqa: E501
            children ([V1Organism]): [optional]  # noqa: E501
            merged ([V1Organism]): [optional]  # noqa: E501
            merged_tax_ids ([str]): [optional]  # noqa: E501
            min_ord (int): [optional]  # noqa: E501
            max_ord (int): [optional]  # noqa: E501
            weight (int): [optional]  # noqa: E501
            key (str): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            icon (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
