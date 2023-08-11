"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.8.1
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
    from apideck.model.currency import Currency
    from apideck.model.idempotency_key import IdempotencyKey
    globals()['Currency'] = Currency
    globals()['IdempotencyKey'] = IdempotencyKey


class Item(ModelNormal):
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
        ('product_type',): {
            'REGULAR': "regular",
            'OTHER': "other",
        },
        ('pricing_type',): {
            'FIXED': "fixed",
            'VARIABLE': "variable",
            'PER_UNIT': "per_unit",
            'OTHER': "other",
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
            'name': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'idempotency_key': (IdempotencyKey,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'abbreviation': (str,),  # noqa: E501
            'product_type': (str,),  # noqa: E501
            'price_amount': (float,),  # noqa: E501
            'pricing_type': (str,),  # noqa: E501
            'price_currency': (Currency,),  # noqa: E501
            'cost': (float,),  # noqa: E501
            'tax_ids': ([str],),  # noqa: E501
            'is_revenue': (bool,),  # noqa: E501
            'use_default_tax_rates': (bool,),  # noqa: E501
            'absent_at_location_ids': ([str],),  # noqa: E501
            'present_at_all_locations': (bool,),  # noqa: E501
            'available_for_pickup': (bool,),  # noqa: E501
            'available_online': (bool,),  # noqa: E501
            'sku': (str,),  # noqa: E501
            'code': (str,),  # noqa: E501
            'categories': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'options': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'variations': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'modifier_groups': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'available': (bool, none_type,),  # noqa: E501
            'hidden': (bool, none_type,),  # noqa: E501
            'version': (str, none_type,),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'id': 'id',  # noqa: E501
        'idempotency_key': 'idempotency_key',  # noqa: E501
        'description': 'description',  # noqa: E501
        'abbreviation': 'abbreviation',  # noqa: E501
        'product_type': 'product_type',  # noqa: E501
        'price_amount': 'price_amount',  # noqa: E501
        'pricing_type': 'pricing_type',  # noqa: E501
        'price_currency': 'price_currency',  # noqa: E501
        'cost': 'cost',  # noqa: E501
        'tax_ids': 'tax_ids',  # noqa: E501
        'is_revenue': 'is_revenue',  # noqa: E501
        'use_default_tax_rates': 'use_default_tax_rates',  # noqa: E501
        'absent_at_location_ids': 'absent_at_location_ids',  # noqa: E501
        'present_at_all_locations': 'present_at_all_locations',  # noqa: E501
        'available_for_pickup': 'available_for_pickup',  # noqa: E501
        'available_online': 'available_online',  # noqa: E501
        'sku': 'sku',  # noqa: E501
        'code': 'code',  # noqa: E501
        'categories': 'categories',  # noqa: E501
        'options': 'options',  # noqa: E501
        'variations': 'variations',  # noqa: E501
        'modifier_groups': 'modifier_groups',  # noqa: E501
        'available': 'available',  # noqa: E501
        'hidden': 'hidden',  # noqa: E501
        'version': 'version',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'version',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, *args, **kwargs):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            name (str):

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
            idempotency_key (IdempotencyKey): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            abbreviation (str): [optional]  # noqa: E501
            product_type (str): [optional]  # noqa: E501
            price_amount (float): [optional]  # noqa: E501
            pricing_type (str): [optional]  # noqa: E501
            price_currency (Currency): [optional]  # noqa: E501
            cost (float): [optional]  # noqa: E501
            tax_ids ([str]): A list of Tax IDs for the product.. [optional]  # noqa: E501
            is_revenue (bool): True if this item should be counted as revenue. For example, gift cards and donations would not be counted as revenue.. [optional]  # noqa: E501
            use_default_tax_rates (bool): [optional]  # noqa: E501
            absent_at_location_ids ([str]): A list of locations where the object is not present, even if present_at_all_locations is true. This can include locations that are deactivated.. [optional]  # noqa: E501
            present_at_all_locations (bool): [optional]  # noqa: E501
            available_for_pickup (bool): [optional]  # noqa: E501
            available_online (bool): [optional]  # noqa: E501
            sku (str): SKU of the item. [optional]  # noqa: E501
            code (str): Product code, e.g. UPC or EAN. [optional]  # noqa: E501
            categories ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            options ([bool, date, datetime, dict, float, int, list, str, none_type]): List of options pertaining to this item's attribute variation. [optional]  # noqa: E501
            variations ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            modifier_groups ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            available (bool, none_type): [optional]  # noqa: E501
            hidden (bool, none_type): [optional]  # noqa: E501
            version (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            deleted (bool, none_type): Flag to indicate if the object is deleted.. [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
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

        self.name = name
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
    def __init__(self, name, *args, **kwargs):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            name (str):

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
            idempotency_key (IdempotencyKey): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            abbreviation (str): [optional]  # noqa: E501
            product_type (str): [optional]  # noqa: E501
            price_amount (float): [optional]  # noqa: E501
            pricing_type (str): [optional]  # noqa: E501
            price_currency (Currency): [optional]  # noqa: E501
            cost (float): [optional]  # noqa: E501
            tax_ids ([str]): A list of Tax IDs for the product.. [optional]  # noqa: E501
            is_revenue (bool): True if this item should be counted as revenue. For example, gift cards and donations would not be counted as revenue.. [optional]  # noqa: E501
            use_default_tax_rates (bool): [optional]  # noqa: E501
            absent_at_location_ids ([str]): A list of locations where the object is not present, even if present_at_all_locations is true. This can include locations that are deactivated.. [optional]  # noqa: E501
            present_at_all_locations (bool): [optional]  # noqa: E501
            available_for_pickup (bool): [optional]  # noqa: E501
            available_online (bool): [optional]  # noqa: E501
            sku (str): SKU of the item. [optional]  # noqa: E501
            code (str): Product code, e.g. UPC or EAN. [optional]  # noqa: E501
            categories ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            options ([bool, date, datetime, dict, float, int, list, str, none_type]): List of options pertaining to this item's attribute variation. [optional]  # noqa: E501
            variations ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            modifier_groups ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            available (bool, none_type): [optional]  # noqa: E501
            hidden (bool, none_type): [optional]  # noqa: E501
            version (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            deleted (bool, none_type): Flag to indicate if the object is deleted.. [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
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

        self.name = name
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
