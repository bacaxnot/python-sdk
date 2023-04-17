"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.1.5
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from apideck.model_utils import (  # noqa: F401
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
    OpenApiModel
)
from apideck.exceptions import ApiAttributeError


def lazy_import():
    from apideck.model.assignee import Assignee
    from apideck.model.collection_tag import CollectionTag
    globals()['Assignee'] = Assignee
    globals()['CollectionTag'] = CollectionTag


class Ticket(ModelNormal):
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
        ('priority',): {
            'LOW': "low",
            'NORMAL': "normal",
            'HIGH': "high",
            'URGENT': "urgent",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            'id': (str,),  # noqa: E501
            'parent_id': (str,),  # noqa: E501
            'collection_id': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'subject': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'priority': (str,),  # noqa: E501
            'assignees': ([Assignee],),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'due_date': (datetime, none_type,),  # noqa: E501
            'completed_at': (datetime, none_type,),  # noqa: E501
            'tags': ([CollectionTag],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'collection_id': 'collection_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'subject': 'subject',  # noqa: E501
        'description': 'description',  # noqa: E501
        'status': 'status',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'assignees': 'assignees',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'due_date': 'due_date',  # noqa: E501
        'completed_at': 'completed_at',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'collection_id',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
        'created_by',  # noqa: E501
        'completed_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, *args, **kwargs):  # noqa: E501
        """Ticket - a model defined in OpenAPI

        Args:
            id (str): A unique identifier for an object.

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
            parent_id (str): The ticket's parent ID. [optional]  # noqa: E501
            collection_id (str): The ticket's collection ID. [optional]  # noqa: E501
            type (str): The ticket's type. [optional]  # noqa: E501
            subject (str): Subject of the ticket. [optional]  # noqa: E501
            description (str): The ticket's description. HTML version of description is mapped if supported by the third-party platform. [optional]  # noqa: E501
            status (str, none_type): The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.. [optional]  # noqa: E501
            priority (str): Priority of the ticket. [optional]  # noqa: E501
            assignees ([Assignee]): [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime): The date and time when the object was created.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            due_date (datetime, none_type): Due date of the ticket. [optional]  # noqa: E501
            completed_at (datetime, none_type): When the ticket was completed. [optional]  # noqa: E501
            tags ([CollectionTag]): [optional]  # noqa: E501
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

        self.id = id
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
        """Ticket - a model defined in OpenAPI

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
            parent_id (str): The ticket's parent ID. [optional]  # noqa: E501
            collection_id (str): The ticket's collection ID. [optional]  # noqa: E501
            type (str): The ticket's type. [optional]  # noqa: E501
            subject (str): Subject of the ticket. [optional]  # noqa: E501
            description (str): The ticket's description. HTML version of description is mapped if supported by the third-party platform. [optional]  # noqa: E501
            status (str, none_type): The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.. [optional]  # noqa: E501
            priority (str): Priority of the ticket. [optional]  # noqa: E501
            assignees ([Assignee]): [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime): The date and time when the object was created.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            due_date (datetime, none_type): Due date of the ticket. [optional]  # noqa: E501
            completed_at (datetime, none_type): When the ticket was completed. [optional]  # noqa: E501
            tags ([CollectionTag]): [optional]  # noqa: E501
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
