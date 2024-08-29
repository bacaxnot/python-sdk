"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.1
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
    from apideck.model.currency import Currency
    from apideck.model.email import Email
    from apideck.model.pass_through_body import PassThroughBody
    from apideck.model.phone_number import PhoneNumber
    from apideck.model.website import Website
    globals()['Address'] = Address
    globals()['Currency'] = Currency
    globals()['Email'] = Email
    globals()['PassThroughBody'] = PassThroughBody
    globals()['PhoneNumber'] = PhoneNumber
    globals()['Website'] = Website


class HrisCompany(ModelNormal):
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
        ('status',): {
            'ACTIVE': "active",
            'INACTIVE': "inactive",
            'TRIAL': "trial",
            'OTHER': "other",
        },
    }

    validations = {
        ('legal_name',): {
            'min_length': 1,
        },
        ('display_name',): {
            'min_length': 1,
        },
        ('subdomain',): {
            'min_length': 1,
        },
        ('debtor_id',): {
            'min_length': 1,
        },
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
            'legal_name': (str, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'display_name': (str, none_type,),  # noqa: E501
            'subdomain': (str, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'company_number': (str, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'addresses': ([Address],),  # noqa: E501
            'phone_numbers': ([PhoneNumber],),  # noqa: E501
            'emails': ([Email],),  # noqa: E501
            'websites': ([Website],),  # noqa: E501
            'debtor_id': (str, none_type,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'pass_through': (PassThroughBody,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'legal_name': 'legal_name',  # noqa: E501
        'id': 'id',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'subdomain': 'subdomain',  # noqa: E501
        'status': 'status',  # noqa: E501
        'company_number': 'company_number',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'emails': 'emails',  # noqa: E501
        'websites': 'websites',  # noqa: E501
        'debtor_id': 'debtor_id',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'pass_through': 'pass_through',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'deleted',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, legal_name, *args, **kwargs):  # noqa: E501
        """HrisCompany - a model defined in OpenAPI

        Args:
            legal_name (str, none_type):

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
            id (str): A unique identifier for an object.. [optional]  # noqa: E501
            display_name (str, none_type): [optional]  # noqa: E501
            subdomain (str, none_type): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            company_number (str, none_type): An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            websites ([Website]): [optional]  # noqa: E501
            debtor_id (str, none_type): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
            pass_through (PassThroughBody): [optional]  # noqa: E501
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

        self.legal_name = legal_name
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
    def __init__(self, legal_name, *args, **kwargs):  # noqa: E501
        """HrisCompany - a model defined in OpenAPI

        Args:
            legal_name (str, none_type):

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
            id (str): A unique identifier for an object.. [optional]  # noqa: E501
            display_name (str, none_type): [optional]  # noqa: E501
            subdomain (str, none_type): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            company_number (str, none_type): An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            websites ([Website]): [optional]  # noqa: E501
            debtor_id (str, none_type): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
            pass_through (PassThroughBody): [optional]  # noqa: E501
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

        self.legal_name = legal_name
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
