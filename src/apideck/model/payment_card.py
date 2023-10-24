"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.0
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
    globals()['Address'] = Address


class PaymentCard(ModelNormal):
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
        ('card_brand',): {
            'None': None,
            'VISA': "visa",
            'MASTERCARD': "mastercard",
            'AMEX': "amex",
            'DISCOVER': "discover",
            'DISCOVER-DINERS': "discover-diners",
            'JCB': "jcb",
            'CHINA-UNIONPAY': "china-unionpay",
            'SQUARE-GIFT-CARD': "square-gift-card",
            'SQUARE-CAPITAL-CARD': "square-capital-card",
            'INTERAC': "interac",
            'EFTPOS': "eftpos",
            'FELICA': "felica",
            'EBT': "ebt",
            'OTHER': "other",
        },
        ('card_type',): {
            'None': None,
            'CREDIT': "credit",
            'DEBIT': "debit",
            'PREPAID': "prepaid",
            'OTHER': "other",
        },
        ('prepaid_type',): {
            'None': None,
            'NON-PREPAID': "non-prepaid",
            'PREPAID': "prepaid",
            'UNKNOWN': "unknown",
        },
    }

    validations = {
        ('exp_month',): {
            'inclusive_maximum': 12,
            'inclusive_minimum': 1,
        },
    }

    additional_properties_type = None

    _nullable = True

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
            'bin': (str, none_type,),  # noqa: E501
            'card_brand': (str, none_type,),  # noqa: E501
            'card_type': (str, none_type,),  # noqa: E501
            'prepaid_type': (str, none_type,),  # noqa: E501
            'cardholder_name': (str, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'exp_month': (int, none_type,),  # noqa: E501
            'exp_year': (int, none_type,),  # noqa: E501
            'fingerprint': (str, none_type,),  # noqa: E501
            'last_4': (str, none_type,),  # noqa: E501
            'enabled': (bool, none_type,),  # noqa: E501
            'billing_address': (Address,),  # noqa: E501
            'reference_id': (str, none_type,),  # noqa: E501
            'version': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'bin': 'bin',  # noqa: E501
        'card_brand': 'card_brand',  # noqa: E501
        'card_type': 'card_type',  # noqa: E501
        'prepaid_type': 'prepaid_type',  # noqa: E501
        'cardholder_name': 'cardholder_name',  # noqa: E501
        'customer_id': 'customer_id',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'exp_month': 'exp_month',  # noqa: E501
        'exp_year': 'exp_year',  # noqa: E501
        'fingerprint': 'fingerprint',  # noqa: E501
        'last_4': 'last_4',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'billing_address': 'billing_address',  # noqa: E501
        'reference_id': 'reference_id',  # noqa: E501
        'version': 'version',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PaymentCard - a model defined in OpenAPI

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
            bin (str, none_type): The first six digits of the card number, known as the Bank Identification Number (BIN).. [optional]  # noqa: E501
            card_brand (str, none_type): The first six digits of the card number, known as the Bank Identification Number (BIN).. [optional]  # noqa: E501
            card_type (str, none_type): [optional]  # noqa: E501
            prepaid_type (str, none_type): [optional]  # noqa: E501
            cardholder_name (str, none_type): [optional]  # noqa: E501
            customer_id (str, none_type): [optional]  # noqa: E501
            merchant_id (str): [optional]  # noqa: E501
            exp_month (int, none_type): The expiration month of the associated card as an integer between 1 and 12.. [optional]  # noqa: E501
            exp_year (int, none_type): The four-digit year of the card's expiration date.. [optional]  # noqa: E501
            fingerprint (str, none_type): [optional]  # noqa: E501
            last_4 (str, none_type): [optional]  # noqa: E501
            enabled (bool, none_type): Indicates whether or not a card can be used for payments.. [optional]  # noqa: E501
            billing_address (Address): [optional]  # noqa: E501
            reference_id (str, none_type): An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system.. [optional]  # noqa: E501
            version (str, none_type): [optional]  # noqa: E501
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
        """PaymentCard - a model defined in OpenAPI

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
            bin (str, none_type): The first six digits of the card number, known as the Bank Identification Number (BIN).. [optional]  # noqa: E501
            card_brand (str, none_type): The first six digits of the card number, known as the Bank Identification Number (BIN).. [optional]  # noqa: E501
            card_type (str, none_type): [optional]  # noqa: E501
            prepaid_type (str, none_type): [optional]  # noqa: E501
            cardholder_name (str, none_type): [optional]  # noqa: E501
            customer_id (str, none_type): [optional]  # noqa: E501
            merchant_id (str): [optional]  # noqa: E501
            exp_month (int, none_type): The expiration month of the associated card as an integer between 1 and 12.. [optional]  # noqa: E501
            exp_year (int, none_type): The four-digit year of the card's expiration date.. [optional]  # noqa: E501
            fingerprint (str, none_type): [optional]  # noqa: E501
            last_4 (str, none_type): [optional]  # noqa: E501
            enabled (bool, none_type): Indicates whether or not a card can be used for payments.. [optional]  # noqa: E501
            billing_address (Address): [optional]  # noqa: E501
            reference_id (str, none_type): An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system.. [optional]  # noqa: E501
            version (str, none_type): [optional]  # noqa: E501
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
