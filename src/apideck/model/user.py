"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.7.6
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
    from apideck.model.address import Address
    from apideck.model.email import Email
    from apideck.model.phone_number import PhoneNumber
    globals()['Address'] = Address
    globals()['Email'] = Email
    globals()['PhoneNumber'] = PhoneNumber


class User(ModelNormal):
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
            'emails': ([Email],),  # noqa: E501
            'id': (str,),  # noqa: E501
            'parent_id': (str, none_type,),  # noqa: E501
            'username': (str, none_type,),  # noqa: E501
            'first_name': (str, none_type,),  # noqa: E501
            'last_name': (str, none_type,),  # noqa: E501
            'title': (str, none_type,),  # noqa: E501
            'division': (str, none_type,),  # noqa: E501
            'department': (str, none_type,),  # noqa: E501
            'company_name': (str, none_type,),  # noqa: E501
            'employee_number': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'image': (str, none_type,),  # noqa: E501
            'language': (str, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'addresses': ([Address],),  # noqa: E501
            'phone_numbers': ([PhoneNumber],),  # noqa: E501
            'updated_at': (str,),  # noqa: E501
            'created_at': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'emails': 'emails',  # noqa: E501
        'id': 'id',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'username': 'username',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'title': 'title',  # noqa: E501
        'division': 'division',  # noqa: E501
        'department': 'department',  # noqa: E501
        'company_name': 'company_name',  # noqa: E501
        'employee_number': 'employee_number',  # noqa: E501
        'description': 'description',  # noqa: E501
        'image': 'image',  # noqa: E501
        'language': 'language',  # noqa: E501
        'status': 'status',  # noqa: E501
        'password': 'password',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, emails, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Args:
            emails ([Email]):

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
            id (str): [optional]  # noqa: E501
            parent_id (str, none_type): [optional]  # noqa: E501
            username (str, none_type): [optional]  # noqa: E501
            first_name (str, none_type): The first name of the person.. [optional]  # noqa: E501
            last_name (str, none_type): The last name of the person.. [optional]  # noqa: E501
            title (str, none_type): The job title of the person.. [optional]  # noqa: E501
            division (str, none_type): The division the person is currently in. Usually a collection of departments or teams or regions.. [optional]  # noqa: E501
            department (str, none_type): The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.. [optional]  # noqa: E501
            company_name (str, none_type): The name of the company.. [optional]  # noqa: E501
            employee_number (str, none_type): An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.. [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            image (str, none_type): [optional]  # noqa: E501
            language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            status (str, none_type): [optional]  # noqa: E501
            password (str): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            updated_at (str): [optional]  # noqa: E501
            created_at (str): [optional]  # noqa: E501
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

        self.emails = emails
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
    def __init__(self, emails, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Args:
            emails ([Email]):

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
            id (str): [optional]  # noqa: E501
            parent_id (str, none_type): [optional]  # noqa: E501
            username (str, none_type): [optional]  # noqa: E501
            first_name (str, none_type): The first name of the person.. [optional]  # noqa: E501
            last_name (str, none_type): The last name of the person.. [optional]  # noqa: E501
            title (str, none_type): The job title of the person.. [optional]  # noqa: E501
            division (str, none_type): The division the person is currently in. Usually a collection of departments or teams or regions.. [optional]  # noqa: E501
            department (str, none_type): The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.. [optional]  # noqa: E501
            company_name (str, none_type): The name of the company.. [optional]  # noqa: E501
            employee_number (str, none_type): An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.. [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            image (str, none_type): [optional]  # noqa: E501
            language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            status (str, none_type): [optional]  # noqa: E501
            password (str): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            updated_at (str): [optional]  # noqa: E501
            created_at (str): [optional]  # noqa: E501
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

        self.emails = emails
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
