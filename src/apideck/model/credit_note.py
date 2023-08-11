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
    from apideck.model.invoice_line_item import InvoiceLineItem
    from apideck.model.linked_customer import LinkedCustomer
    from apideck.model.linked_ledger_account import LinkedLedgerAccount
    globals()['Currency'] = Currency
    globals()['InvoiceLineItem'] = InvoiceLineItem
    globals()['LinkedCustomer'] = LinkedCustomer
    globals()['LinkedLedgerAccount'] = LinkedLedgerAccount


class CreditNote(ModelNormal):
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
            'DRAFT': "draft",
            'AUTHORISED': "authorised",
            'PAID': "paid",
            'VOIDED': "voided",
            'DELETED': "deleted",
        },
        ('type',): {
            'RECEIVABLE_CREDIT': "accounts_receivable_credit",
            'PAYABLE_CREDIT': "accounts_payable_credit",
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
            'number': (str, none_type,),  # noqa: E501
            'customer': (LinkedCustomer,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'currency_rate': (float, none_type,),  # noqa: E501
            'tax_inclusive': (bool, none_type,),  # noqa: E501
            'sub_total': (float, none_type,),  # noqa: E501
            'total_tax': (float, none_type,),  # noqa: E501
            'tax_code': (str, none_type,),  # noqa: E501
            'balance': (float, none_type,),  # noqa: E501
            'remaining_credit': (float, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'reference': (str, none_type,),  # noqa: E501
            'date_issued': (datetime,),  # noqa: E501
            'date_paid': (datetime, none_type,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'account': (LinkedLedgerAccount,),  # noqa: E501
            'line_items': ([InvoiceLineItem],),  # noqa: E501
            'allocations': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'note': (str, none_type,),  # noqa: E501
            'terms': (str, none_type,),  # noqa: E501
            'row_version': (str, none_type,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'number': 'number',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'currency_rate': 'currency_rate',  # noqa: E501
        'tax_inclusive': 'tax_inclusive',  # noqa: E501
        'sub_total': 'sub_total',  # noqa: E501
        'total_tax': 'total_tax',  # noqa: E501
        'tax_code': 'tax_code',  # noqa: E501
        'balance': 'balance',  # noqa: E501
        'remaining_credit': 'remaining_credit',  # noqa: E501
        'status': 'status',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'date_issued': 'date_issued',  # noqa: E501
        'date_paid': 'date_paid',  # noqa: E501
        'type': 'type',  # noqa: E501
        'account': 'account',  # noqa: E501
        'line_items': 'line_items',  # noqa: E501
        'allocations': 'allocations',  # noqa: E501
        'note': 'note',  # noqa: E501
        'terms': 'terms',  # noqa: E501
        'row_version': 'row_version',  # noqa: E501
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
    def _from_openapi_data(cls, id, total_amount, *args, **kwargs):  # noqa: E501
        """CreditNote - a model defined in OpenAPI

        Args:
            id (str): Unique identifier representing the entity
            total_amount (float): Amount of transaction

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
            number (str, none_type): Credit note number.. [optional]  # noqa: E501
            customer (LinkedCustomer): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            currency_rate (float, none_type): Currency Exchange Rate at the time entity was recorded/generated.. [optional]  # noqa: E501
            tax_inclusive (bool, none_type): Amounts are including tax. [optional]  # noqa: E501
            sub_total (float, none_type): Sub-total amount, normally before tax.. [optional]  # noqa: E501
            total_tax (float, none_type): Total tax amount applied to this invoice.. [optional]  # noqa: E501
            tax_code (str, none_type): Applicable tax id/code override if tax is not supplied on a line item basis.. [optional]  # noqa: E501
            balance (float, none_type): The balance reflecting any payments made against the transaction.. [optional]  # noqa: E501
            remaining_credit (float, none_type): Indicates the total credit amount still available to apply towards the payment.. [optional]  # noqa: E501
            status (str): Status of credit notes. [optional]  # noqa: E501
            reference (str, none_type): Optional reference message ie: Debit remittance detail.. [optional]  # noqa: E501
            date_issued (datetime): Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD. [optional]  # noqa: E501
            date_paid (datetime, none_type): Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD. [optional]  # noqa: E501
            type (str): Type of payment. [optional]  # noqa: E501
            account (LinkedLedgerAccount): [optional]  # noqa: E501
            line_items ([InvoiceLineItem]): [optional]  # noqa: E501
            allocations ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            note (str, none_type): Optional note to be associated with the credit note.. [optional]  # noqa: E501
            terms (str, none_type): Optional terms to be associated with the credit note.. [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
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

        self.id = id
        self.total_amount = total_amount
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
    def __init__(self, total_amount, *args, **kwargs):  # noqa: E501
        """CreditNote - a model defined in OpenAPI

            total_amount (float): Amount of transaction

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
            number (str, none_type): Credit note number.. [optional]  # noqa: E501
            customer (LinkedCustomer): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            currency_rate (float, none_type): Currency Exchange Rate at the time entity was recorded/generated.. [optional]  # noqa: E501
            tax_inclusive (bool, none_type): Amounts are including tax. [optional]  # noqa: E501
            sub_total (float, none_type): Sub-total amount, normally before tax.. [optional]  # noqa: E501
            total_tax (float, none_type): Total tax amount applied to this invoice.. [optional]  # noqa: E501
            tax_code (str, none_type): Applicable tax id/code override if tax is not supplied on a line item basis.. [optional]  # noqa: E501
            balance (float, none_type): The balance reflecting any payments made against the transaction.. [optional]  # noqa: E501
            remaining_credit (float, none_type): Indicates the total credit amount still available to apply towards the payment.. [optional]  # noqa: E501
            status (str): Status of credit notes. [optional]  # noqa: E501
            reference (str, none_type): Optional reference message ie: Debit remittance detail.. [optional]  # noqa: E501
            date_issued (datetime): Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD. [optional]  # noqa: E501
            date_paid (datetime, none_type): Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD. [optional]  # noqa: E501
            type (str): Type of payment. [optional]  # noqa: E501
            account (LinkedLedgerAccount): [optional]  # noqa: E501
            line_items ([InvoiceLineItem]): [optional]  # noqa: E501
            allocations ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            note (str, none_type): Optional note to be associated with the credit note.. [optional]  # noqa: E501
            terms (str, none_type): Optional terms to be associated with the credit note.. [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
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

        self.total_amount = total_amount
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
