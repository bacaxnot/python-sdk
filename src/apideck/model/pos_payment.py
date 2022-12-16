"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 8.85.0
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
    from apideck.model.cash_details import CashDetails
    from apideck.model.currency import Currency
    from apideck.model.idempotency_key import IdempotencyKey
    from apideck.model.pos_bank_account import PosBankAccount
    from apideck.model.pos_payment_card_details import PosPaymentCardDetails
    from apideck.model.pos_payment_external_details import PosPaymentExternalDetails
    from apideck.model.service_charges import ServiceCharges
    from apideck.model.wallet_details import WalletDetails
    globals()['CashDetails'] = CashDetails
    globals()['Currency'] = Currency
    globals()['IdempotencyKey'] = IdempotencyKey
    globals()['PosBankAccount'] = PosBankAccount
    globals()['PosPaymentCardDetails'] = PosPaymentCardDetails
    globals()['PosPaymentExternalDetails'] = PosPaymentExternalDetails
    globals()['ServiceCharges'] = ServiceCharges
    globals()['WalletDetails'] = WalletDetails


class PosPayment(ModelNormal):
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
        ('source',): {
            'CARD': "card",
            'BANK_ACCOUNT': "bank_account",
            'WALLET': "wallet",
            'BNPL': "bnpl",
            'CASH': "cash",
            'EXTERNAL': "external",
            'OTHER': "other",
        },
        ('status',): {
            'APPROVED': "approved",
            'PENDING': "pending",
            'COMPLETED': "completed",
            'CANCELED': "canceled",
            'FAILED': "failed",
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
            'source_id': (str,),  # noqa: E501
            'order_id': (str,),  # noqa: E501
            'customer_id': (str,),  # noqa: E501
            'tender_id': (str,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'employee_id': (str,),  # noqa: E501
            'location_id': (str,),  # noqa: E501
            'device_id': (str,),  # noqa: E501
            'external_payment_id': (str,),  # noqa: E501
            'idempotency_key': (IdempotencyKey,),  # noqa: E501
            'tip': (float,),  # noqa: E501
            'tax': (float,),  # noqa: E501
            'total': (float,),  # noqa: E501
            'app_fee': (float,),  # noqa: E501
            'change_back_cash_amount': (float,),  # noqa: E501
            'approved': (float,),  # noqa: E501
            'refunded': (float,),  # noqa: E501
            'processing_fees': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'source': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'cash': (CashDetails,),  # noqa: E501
            'card_details': (PosPaymentCardDetails,),  # noqa: E501
            'bank_account': (PosBankAccount,),  # noqa: E501
            'wallet': (WalletDetails,),  # noqa: E501
            'external_details': (PosPaymentExternalDetails,),  # noqa: E501
            'service_charges': (ServiceCharges,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'source_id': 'source_id',  # noqa: E501
        'order_id': 'order_id',  # noqa: E501
        'customer_id': 'customer_id',  # noqa: E501
        'tender_id': 'tender_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'id': 'id',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'employee_id': 'employee_id',  # noqa: E501
        'location_id': 'location_id',  # noqa: E501
        'device_id': 'device_id',  # noqa: E501
        'external_payment_id': 'external_payment_id',  # noqa: E501
        'idempotency_key': 'idempotency_key',  # noqa: E501
        'tip': 'tip',  # noqa: E501
        'tax': 'tax',  # noqa: E501
        'total': 'total',  # noqa: E501
        'app_fee': 'app_fee',  # noqa: E501
        'change_back_cash_amount': 'change_back_cash_amount',  # noqa: E501
        'approved': 'approved',  # noqa: E501
        'refunded': 'refunded',  # noqa: E501
        'processing_fees': 'processing_fees',  # noqa: E501
        'source': 'source',  # noqa: E501
        'status': 'status',  # noqa: E501
        'cash': 'cash',  # noqa: E501
        'card_details': 'card_details',  # noqa: E501
        'bank_account': 'bank_account',  # noqa: E501
        'wallet': 'wallet',  # noqa: E501
        'external_details': 'external_details',  # noqa: E501
        'service_charges': 'service_charges',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, source_id, order_id, customer_id, tender_id, amount, currency, *args, **kwargs):  # noqa: E501
        """PosPayment - a model defined in OpenAPI

        Args:
            source_id (str): The ID for the source of funds for this payment. Square-only: This can be a payment token (card nonce) generated by the payment form or a card on file made linked to the customer. if recording a payment that the seller received outside of Square, specify either `CASH` or `EXTERNAL`.
            order_id (str):
            customer_id (str):
            tender_id (str):
            amount (float):
            currency (Currency):

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
            merchant_id (str): [optional]  # noqa: E501
            employee_id (str): [optional]  # noqa: E501
            location_id (str): [optional]  # noqa: E501
            device_id (str): [optional]  # noqa: E501
            external_payment_id (str): [optional]  # noqa: E501
            idempotency_key (IdempotencyKey): [optional]  # noqa: E501
            tip (float): [optional]  # noqa: E501
            tax (float): [optional]  # noqa: E501
            total (float): [optional]  # noqa: E501
            app_fee (float): The amount the developer is taking as a fee for facilitating the payment on behalf of the seller.. [optional]  # noqa: E501
            change_back_cash_amount (float): [optional]  # noqa: E501
            approved (float): The initial amount of money approved for this payment.. [optional]  # noqa: E501
            refunded (float): The initial amount of money approved for this payment.. [optional]  # noqa: E501
            processing_fees ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            source (str): Source of this payment.. [optional]  # noqa: E501
            status (str): Status of this payment.. [optional]  # noqa: E501
            cash (CashDetails): [optional]  # noqa: E501
            card_details (PosPaymentCardDetails): [optional]  # noqa: E501
            bank_account (PosBankAccount): [optional]  # noqa: E501
            wallet (WalletDetails): [optional]  # noqa: E501
            external_details (PosPaymentExternalDetails): [optional]  # noqa: E501
            service_charges (ServiceCharges): [optional]  # noqa: E501
            updated_by (str, none_type): [optional]  # noqa: E501
            created_by (str, none_type): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
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

        self.source_id = source_id
        self.order_id = order_id
        self.customer_id = customer_id
        self.tender_id = tender_id
        self.amount = amount
        self.currency = currency
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
    def __init__(self, source_id, order_id, customer_id, tender_id, amount, currency, *args, **kwargs):  # noqa: E501
        """PosPayment - a model defined in OpenAPI

        Args:
            source_id (str): The ID for the source of funds for this payment. Square-only: This can be a payment token (card nonce) generated by the payment form or a card on file made linked to the customer. if recording a payment that the seller received outside of Square, specify either `CASH` or `EXTERNAL`.
            order_id (str):
            customer_id (str):
            tender_id (str):
            amount (float):
            currency (Currency):

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
            merchant_id (str): [optional]  # noqa: E501
            employee_id (str): [optional]  # noqa: E501
            location_id (str): [optional]  # noqa: E501
            device_id (str): [optional]  # noqa: E501
            external_payment_id (str): [optional]  # noqa: E501
            idempotency_key (IdempotencyKey): [optional]  # noqa: E501
            tip (float): [optional]  # noqa: E501
            tax (float): [optional]  # noqa: E501
            total (float): [optional]  # noqa: E501
            app_fee (float): The amount the developer is taking as a fee for facilitating the payment on behalf of the seller.. [optional]  # noqa: E501
            change_back_cash_amount (float): [optional]  # noqa: E501
            approved (float): The initial amount of money approved for this payment.. [optional]  # noqa: E501
            refunded (float): The initial amount of money approved for this payment.. [optional]  # noqa: E501
            processing_fees ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            source (str): Source of this payment.. [optional]  # noqa: E501
            status (str): Status of this payment.. [optional]  # noqa: E501
            cash (CashDetails): [optional]  # noqa: E501
            card_details (PosPaymentCardDetails): [optional]  # noqa: E501
            bank_account (PosBankAccount): [optional]  # noqa: E501
            wallet (WalletDetails): [optional]  # noqa: E501
            external_details (PosPaymentExternalDetails): [optional]  # noqa: E501
            service_charges (ServiceCharges): [optional]  # noqa: E501
            updated_by (str, none_type): [optional]  # noqa: E501
            created_by (str, none_type): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
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

        self.source_id = source_id
        self.order_id = order_id
        self.customer_id = customer_id
        self.tender_id = tender_id
        self.amount = amount
        self.currency = currency
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
