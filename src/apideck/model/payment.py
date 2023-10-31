"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.0.1
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
    from apideck.model.linked_customer import LinkedCustomer
    from apideck.model.linked_ledger_account import LinkedLedgerAccount
    from apideck.model.linked_supplier import LinkedSupplier
    from apideck.model.payment_allocations import PaymentAllocations
    globals()['Currency'] = Currency
    globals()['LinkedCustomer'] = LinkedCustomer
    globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
    globals()['LinkedSupplier'] = LinkedSupplier
    globals()['PaymentAllocations'] = PaymentAllocations


class Payment(ModelNormal):
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
            'AUTHORISED': "authorised",
            'PAID': "paid",
            'VOIDED': "voided",
            'DELETED': "deleted",
        },
        ('type',): {
            'RECEIVABLE': "accounts_receivable",
            'PAYABLE': "accounts_payable",
            'RECEIVABLE_CREDIT': "accounts_receivable_credit",
            'PAYABLE_CREDIT': "accounts_payable_credit",
            'RECEIVABLE_OVERPAYMENT': "accounts_receivable_overpayment",
            'PAYABLE_OVERPAYMENT': "accounts_payable_overpayment",
            'RECEIVABLE_PREPAYMENT': "accounts_receivable_prepayment",
            'PAYABLE_PREPAYMENT': "accounts_payable_prepayment",
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
            'total_amount': (float,),  # noqa: E501
            'transaction_date': (datetime,),  # noqa: E501
            'downstream_id': (str, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'currency_rate': (float, none_type,),  # noqa: E501
            'reference': (str, none_type,),  # noqa: E501
            'payment_method': (str, none_type,),  # noqa: E501
            'payment_method_reference': (str, none_type,),  # noqa: E501
            'payment_method_id': (str, none_type,),  # noqa: E501
            'accounts_receivable_account_type': (str, none_type,),  # noqa: E501
            'accounts_receivable_account_id': (str, none_type,),  # noqa: E501
            'account': (LinkedLedgerAccount,),  # noqa: E501
            'customer': (LinkedCustomer,),  # noqa: E501
            'supplier': (LinkedSupplier,),  # noqa: E501
            'reconciled': (bool,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'allocations': ([PaymentAllocations],),  # noqa: E501
            'note': (str, none_type,),  # noqa: E501
            'row_version': (str, none_type,),  # noqa: E501
            'display_id': (str, none_type,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'transaction_date': 'transaction_date',  # noqa: E501
        'downstream_id': 'downstream_id',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'currency_rate': 'currency_rate',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'payment_method': 'payment_method',  # noqa: E501
        'payment_method_reference': 'payment_method_reference',  # noqa: E501
        'payment_method_id': 'payment_method_id',  # noqa: E501
        'accounts_receivable_account_type': 'accounts_receivable_account_type',  # noqa: E501
        'accounts_receivable_account_id': 'accounts_receivable_account_id',  # noqa: E501
        'account': 'account',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'supplier': 'supplier',  # noqa: E501
        'reconciled': 'reconciled',  # noqa: E501
        'status': 'status',  # noqa: E501
        'type': 'type',  # noqa: E501
        'allocations': 'allocations',  # noqa: E501
        'note': 'note',  # noqa: E501
        'row_version': 'row_version',  # noqa: E501
        'display_id': 'display_id',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'downstream_id',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'created_at',  # noqa: E501
        'updated_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, total_amount, transaction_date, *args, **kwargs):  # noqa: E501
        """Payment - a model defined in OpenAPI

        Args:
            id (str): Unique identifier representing the entity
            total_amount (float): Amount of payment
            transaction_date (datetime): Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD

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
            downstream_id (str, none_type): The third-party API ID of original entity. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            currency_rate (float, none_type): Currency Exchange Rate at the time entity was recorded/generated.. [optional]  # noqa: E501
            reference (str, none_type): Optional payment reference message ie: Debit remittance detail.. [optional]  # noqa: E501
            payment_method (str, none_type): Payment method name. [optional]  # noqa: E501
            payment_method_reference (str, none_type): Optional reference message returned by payment method on processing. [optional]  # noqa: E501
            payment_method_id (str, none_type): Unique identifier for the payment method.. [optional]  # noqa: E501
            accounts_receivable_account_type (str, none_type): Type of accounts receivable account.. [optional]  # noqa: E501
            accounts_receivable_account_id (str, none_type): Unique identifier for the account to allocate payment to.. [optional]  # noqa: E501
            account (LinkedLedgerAccount): [optional]  # noqa: E501
            customer (LinkedCustomer): [optional]  # noqa: E501
            supplier (LinkedSupplier): [optional]  # noqa: E501
            reconciled (bool): Payment has been reconciled. [optional]  # noqa: E501
            status (str): Status of payment. [optional]  # noqa: E501
            type (str): Type of payment. [optional]  # noqa: E501
            allocations ([PaymentAllocations]): [optional]  # noqa: E501
            note (str, none_type): Optional note to be associated with the payment.. [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
            display_id (str, none_type): Payment id to be displayed.. [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
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
        self.total_amount = total_amount
        self.transaction_date = transaction_date
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
    def __init__(self, total_amount, transaction_date, *args, **kwargs):  # noqa: E501
        """Payment - a model defined in OpenAPI

            total_amount (float): Amount of payment
            transaction_date (datetime): Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD

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
            downstream_id (str, none_type): The third-party API ID of original entity. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            currency_rate (float, none_type): Currency Exchange Rate at the time entity was recorded/generated.. [optional]  # noqa: E501
            reference (str, none_type): Optional payment reference message ie: Debit remittance detail.. [optional]  # noqa: E501
            payment_method (str, none_type): Payment method name. [optional]  # noqa: E501
            payment_method_reference (str, none_type): Optional reference message returned by payment method on processing. [optional]  # noqa: E501
            payment_method_id (str, none_type): Unique identifier for the payment method.. [optional]  # noqa: E501
            accounts_receivable_account_type (str, none_type): Type of accounts receivable account.. [optional]  # noqa: E501
            accounts_receivable_account_id (str, none_type): Unique identifier for the account to allocate payment to.. [optional]  # noqa: E501
            account (LinkedLedgerAccount): [optional]  # noqa: E501
            customer (LinkedCustomer): [optional]  # noqa: E501
            supplier (LinkedSupplier): [optional]  # noqa: E501
            reconciled (bool): Payment has been reconciled. [optional]  # noqa: E501
            status (str): Status of payment. [optional]  # noqa: E501
            type (str): Type of payment. [optional]  # noqa: E501
            allocations ([PaymentAllocations]): [optional]  # noqa: E501
            note (str, none_type): Optional note to be associated with the payment.. [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
            display_id (str, none_type): Payment id to be displayed.. [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
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

        self.total_amount = total_amount
        self.transaction_date = transaction_date
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
