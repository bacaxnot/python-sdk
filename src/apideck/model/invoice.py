"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.3
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
    from apideck.model.bank_account import BankAccount
    from apideck.model.currency import Currency
    from apideck.model.custom_field import CustomField
    from apideck.model.invoice_line_item import InvoiceLineItem
    from apideck.model.linked_customer import LinkedCustomer
    from apideck.model.linked_ledger_account import LinkedLedgerAccount
    from apideck.model.linked_tracking_category import LinkedTrackingCategory
    from apideck.model.pass_through_body import PassThroughBody
    globals()['Address'] = Address
    globals()['BankAccount'] = BankAccount
    globals()['Currency'] = Currency
    globals()['CustomField'] = CustomField
    globals()['InvoiceLineItem'] = InvoiceLineItem
    globals()['LinkedCustomer'] = LinkedCustomer
    globals()['LinkedLedgerAccount'] = LinkedLedgerAccount
    globals()['LinkedTrackingCategory'] = LinkedTrackingCategory
    globals()['PassThroughBody'] = PassThroughBody


class Invoice(ModelNormal):
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
        ('type',): {
            'None': None,
            'STANDARD': "standard",
            'CREDIT': "credit",
            'SERVICE': "service",
            'PRODUCT': "product",
            'SUPPLIER': "supplier",
            'OTHER': "other",
        },
        ('status',): {
            'None': None,
            'DRAFT': "draft",
            'SUBMITTED': "submitted",
            'AUTHORISED': "authorised",
            'PARTIALLY_PAID': "partially_paid",
            'PAID': "paid",
            'VOID': "void",
            'CREDIT': "credit",
            'DELETED': "deleted",
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
            'downstream_id': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'number': (str, none_type,),  # noqa: E501
            'customer': (LinkedCustomer,),  # noqa: E501
            'company_id': (str, none_type,),  # noqa: E501
            'invoice_date': (date, none_type,),  # noqa: E501
            'due_date': (date, none_type,),  # noqa: E501
            'terms': (str, none_type,),  # noqa: E501
            'po_number': (str, none_type,),  # noqa: E501
            'reference': (str, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'invoice_sent': (bool,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'currency_rate': (float, none_type,),  # noqa: E501
            'tax_inclusive': (bool, none_type,),  # noqa: E501
            'sub_total': (float, none_type,),  # noqa: E501
            'total_tax': (float, none_type,),  # noqa: E501
            'tax_code': (str, none_type,),  # noqa: E501
            'discount_percentage': (float, none_type,),  # noqa: E501
            'discount_amount': (float, none_type,),  # noqa: E501
            'total': (float, none_type,),  # noqa: E501
            'balance': (float, none_type,),  # noqa: E501
            'deposit': (float, none_type,),  # noqa: E501
            'customer_memo': (str, none_type,),  # noqa: E501
            'tracking_category': (LinkedTrackingCategory,),  # noqa: E501
            'line_items': ([InvoiceLineItem],),  # noqa: E501
            'billing_address': (Address,),  # noqa: E501
            'shipping_address': (Address,),  # noqa: E501
            'template_id': (str, none_type,),  # noqa: E501
            'source_document_url': (str, none_type,),  # noqa: E501
            'payment_method': (str, none_type,),  # noqa: E501
            'channel': (str, none_type,),  # noqa: E501
            'language': (str, none_type,),  # noqa: E501
            'accounting_by_row': (bool, none_type,),  # noqa: E501
            'bank_account': (BankAccount,),  # noqa: E501
            'ledger_account': (LinkedLedgerAccount,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'custom_fields': ([CustomField],),  # noqa: E501
            'row_version': (str, none_type,),  # noqa: E501
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
        'id': 'id',  # noqa: E501
        'downstream_id': 'downstream_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'number': 'number',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'company_id': 'company_id',  # noqa: E501
        'invoice_date': 'invoice_date',  # noqa: E501
        'due_date': 'due_date',  # noqa: E501
        'terms': 'terms',  # noqa: E501
        'po_number': 'po_number',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'status': 'status',  # noqa: E501
        'invoice_sent': 'invoice_sent',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'currency_rate': 'currency_rate',  # noqa: E501
        'tax_inclusive': 'tax_inclusive',  # noqa: E501
        'sub_total': 'sub_total',  # noqa: E501
        'total_tax': 'total_tax',  # noqa: E501
        'tax_code': 'tax_code',  # noqa: E501
        'discount_percentage': 'discount_percentage',  # noqa: E501
        'discount_amount': 'discount_amount',  # noqa: E501
        'total': 'total',  # noqa: E501
        'balance': 'balance',  # noqa: E501
        'deposit': 'deposit',  # noqa: E501
        'customer_memo': 'customer_memo',  # noqa: E501
        'tracking_category': 'tracking_category',  # noqa: E501
        'line_items': 'line_items',  # noqa: E501
        'billing_address': 'billing_address',  # noqa: E501
        'shipping_address': 'shipping_address',  # noqa: E501
        'template_id': 'template_id',  # noqa: E501
        'source_document_url': 'source_document_url',  # noqa: E501
        'payment_method': 'payment_method',  # noqa: E501
        'channel': 'channel',  # noqa: E501
        'language': 'language',  # noqa: E501
        'accounting_by_row': 'accounting_by_row',  # noqa: E501
        'bank_account': 'bank_account',  # noqa: E501
        'ledger_account': 'ledger_account',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'row_version': 'row_version',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'pass_through': 'pass_through',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'downstream_id',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Invoice - a model defined in OpenAPI

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
            downstream_id (str, none_type): The third-party API ID of original entity. [optional]  # noqa: E501
            type (str, none_type): Invoice type. [optional]  # noqa: E501
            number (str, none_type): Invoice number.. [optional]  # noqa: E501
            customer (LinkedCustomer): [optional]  # noqa: E501
            company_id (str, none_type): The company or subsidiary id the transaction belongs to. [optional]  # noqa: E501
            invoice_date (date, none_type): Date invoice was issued - YYYY-MM-DD.. [optional]  # noqa: E501
            due_date (date, none_type): The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.. [optional]  # noqa: E501
            terms (str, none_type): Terms of payment.. [optional]  # noqa: E501
            po_number (str, none_type): A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.. [optional]  # noqa: E501
            reference (str, none_type): Optional invoice reference.. [optional]  # noqa: E501
            status (str, none_type): Invoice status. [optional]  # noqa: E501
            invoice_sent (bool): Invoice sent to contact/customer.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            currency_rate (float, none_type): Currency Exchange Rate at the time entity was recorded/generated.. [optional]  # noqa: E501
            tax_inclusive (bool, none_type): Amounts are including tax. [optional]  # noqa: E501
            sub_total (float, none_type): Sub-total amount, normally before tax.. [optional]  # noqa: E501
            total_tax (float, none_type): Total tax amount applied to this invoice.. [optional]  # noqa: E501
            tax_code (str, none_type): Applicable tax id/code override if tax is not supplied on a line item basis.. [optional]  # noqa: E501
            discount_percentage (float, none_type): Discount percentage applied to this invoice.. [optional]  # noqa: E501
            discount_amount (float, none_type): Discount amount applied to this invoice.. [optional]  # noqa: E501
            total (float, none_type): Total amount of invoice, including tax.. [optional]  # noqa: E501
            balance (float, none_type): Balance of invoice due.. [optional]  # noqa: E501
            deposit (float, none_type): Amount of deposit made to this invoice.. [optional]  # noqa: E501
            customer_memo (str, none_type): Customer memo. [optional]  # noqa: E501
            tracking_category (LinkedTrackingCategory): [optional]  # noqa: E501
            line_items ([InvoiceLineItem]): [optional]  # noqa: E501
            billing_address (Address): [optional]  # noqa: E501
            shipping_address (Address): [optional]  # noqa: E501
            template_id (str, none_type): Optional invoice template. [optional]  # noqa: E501
            source_document_url (str, none_type): URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.. [optional]  # noqa: E501
            payment_method (str, none_type): Payment method used for the transaction, such as cash, credit card, bank transfer, or check. [optional]  # noqa: E501
            channel (str, none_type): The channel through which the transaction is processed.. [optional]  # noqa: E501
            language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            accounting_by_row (bool, none_type): Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.. [optional]  # noqa: E501
            bank_account (BankAccount): [optional]  # noqa: E501
            ledger_account (LinkedLedgerAccount): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
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
        """Invoice - a model defined in OpenAPI

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
            downstream_id (str, none_type): The third-party API ID of original entity. [optional]  # noqa: E501
            type (str, none_type): Invoice type. [optional]  # noqa: E501
            number (str, none_type): Invoice number.. [optional]  # noqa: E501
            customer (LinkedCustomer): [optional]  # noqa: E501
            company_id (str, none_type): The company or subsidiary id the transaction belongs to. [optional]  # noqa: E501
            invoice_date (date, none_type): Date invoice was issued - YYYY-MM-DD.. [optional]  # noqa: E501
            due_date (date, none_type): The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.. [optional]  # noqa: E501
            terms (str, none_type): Terms of payment.. [optional]  # noqa: E501
            po_number (str, none_type): A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.. [optional]  # noqa: E501
            reference (str, none_type): Optional invoice reference.. [optional]  # noqa: E501
            status (str, none_type): Invoice status. [optional]  # noqa: E501
            invoice_sent (bool): Invoice sent to contact/customer.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            currency_rate (float, none_type): Currency Exchange Rate at the time entity was recorded/generated.. [optional]  # noqa: E501
            tax_inclusive (bool, none_type): Amounts are including tax. [optional]  # noqa: E501
            sub_total (float, none_type): Sub-total amount, normally before tax.. [optional]  # noqa: E501
            total_tax (float, none_type): Total tax amount applied to this invoice.. [optional]  # noqa: E501
            tax_code (str, none_type): Applicable tax id/code override if tax is not supplied on a line item basis.. [optional]  # noqa: E501
            discount_percentage (float, none_type): Discount percentage applied to this invoice.. [optional]  # noqa: E501
            discount_amount (float, none_type): Discount amount applied to this invoice.. [optional]  # noqa: E501
            total (float, none_type): Total amount of invoice, including tax.. [optional]  # noqa: E501
            balance (float, none_type): Balance of invoice due.. [optional]  # noqa: E501
            deposit (float, none_type): Amount of deposit made to this invoice.. [optional]  # noqa: E501
            customer_memo (str, none_type): Customer memo. [optional]  # noqa: E501
            tracking_category (LinkedTrackingCategory): [optional]  # noqa: E501
            line_items ([InvoiceLineItem]): [optional]  # noqa: E501
            billing_address (Address): [optional]  # noqa: E501
            shipping_address (Address): [optional]  # noqa: E501
            template_id (str, none_type): Optional invoice template. [optional]  # noqa: E501
            source_document_url (str, none_type): URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.. [optional]  # noqa: E501
            payment_method (str, none_type): Payment method used for the transaction, such as cash, credit card, bank transfer, or check. [optional]  # noqa: E501
            channel (str, none_type): The channel through which the transaction is processed.. [optional]  # noqa: E501
            language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            accounting_by_row (bool, none_type): Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.. [optional]  # noqa: E501
            bank_account (BankAccount): [optional]  # noqa: E501
            ledger_account (LinkedLedgerAccount): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
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
