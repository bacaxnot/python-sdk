"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.2
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
    from apideck.model.bank_account import BankAccount
    from apideck.model.currency import Currency
    from apideck.model.ledger_account_categories import LedgerAccountCategories
    from apideck.model.ledger_account_parent_account import LedgerAccountParentAccount
    from apideck.model.linked_tax_rate import LinkedTaxRate
    globals()['BankAccount'] = BankAccount
    globals()['Currency'] = Currency
    globals()['LedgerAccountCategories'] = LedgerAccountCategories
    globals()['LedgerAccountParentAccount'] = LedgerAccountParentAccount
    globals()['LinkedTaxRate'] = LinkedTaxRate


class LedgerAccount(ModelNormal):
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
        ('classification',): {
            'None': None,
            'ASSET': "asset",
            'EQUITY': "equity",
            'EXPENSE': "expense",
            'LIABILITY': "liability",
            'REVENUE': "revenue",
            'INCOME': "income",
            'OTHER_INCOME': "other_income",
            'OTHER_EXPENSE': "other_expense",
            'COSTS_OF_SALES': "costs_of_sales",
        },
        ('type',): {
            'ACCOUNTS_RECEIVABLE': "accounts_receivable",
            'REVENUE': "revenue",
            'SALES': "sales",
            'OTHER_INCOME': "other_income",
            'BANK': "bank",
            'CURRENT_ASSET': "current_asset",
            'FIXED_ASSET': "fixed_asset",
            'NON_CURRENT_ASSET': "non_current_asset",
            'OTHER_ASSET': "other_asset",
            'BALANCESHEET': "balancesheet",
            'EQUITY': "equity",
            'EXPENSE': "expense",
            'OTHER_EXPENSE': "other_expense",
            'COSTS_OF_SALES': "costs_of_sales",
            'ACCOUNTS_PAYABLE': "accounts_payable",
            'CREDIT_CARD': "credit_card",
            'CURRENT_LIABILITY': "current_liability",
            'NON_CURRENT_LIABILITY': "non_current_liability",
            'OTHER_LIABILITY': "other_liability",
            'OTHER': "other",
        },
        ('status',): {
            'None': None,
            'ACTIVE': "active",
            'INACTIVE': "inactive",
            'ARCHIVED': "archived",
        },
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
            'id': (str,),  # noqa: E501
            'display_id': (str,),  # noqa: E501
            'nominal_code': (str, none_type,),  # noqa: E501
            'code': (str, none_type,),  # noqa: E501
            'classification': (str, none_type,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'sub_type': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'fully_qualified_name': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'opening_balance': (float, none_type,),  # noqa: E501
            'current_balance': (float, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'tax_type': (str, none_type,),  # noqa: E501
            'tax_rate': (LinkedTaxRate,),  # noqa: E501
            'level': (float, none_type,),  # noqa: E501
            'active': (bool, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'header': (bool, none_type,),  # noqa: E501
            'bank_account': (BankAccount,),  # noqa: E501
            'categories': ([LedgerAccountCategories],),  # noqa: E501
            'parent_account': (LedgerAccountParentAccount,),  # noqa: E501
            'sub_account': (bool, none_type,),  # noqa: E501
            'sub_accounts': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'last_reconciliation_date': (date, none_type,),  # noqa: E501
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
        'display_id': 'display_id',  # noqa: E501
        'nominal_code': 'nominal_code',  # noqa: E501
        'code': 'code',  # noqa: E501
        'classification': 'classification',  # noqa: E501
        'type': 'type',  # noqa: E501
        'sub_type': 'sub_type',  # noqa: E501
        'name': 'name',  # noqa: E501
        'fully_qualified_name': 'fully_qualified_name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'opening_balance': 'opening_balance',  # noqa: E501
        'current_balance': 'current_balance',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'tax_type': 'tax_type',  # noqa: E501
        'tax_rate': 'tax_rate',  # noqa: E501
        'level': 'level',  # noqa: E501
        'active': 'active',  # noqa: E501
        'status': 'status',  # noqa: E501
        'header': 'header',  # noqa: E501
        'bank_account': 'bank_account',  # noqa: E501
        'categories': 'categories',  # noqa: E501
        'parent_account': 'parent_account',  # noqa: E501
        'sub_account': 'sub_account',  # noqa: E501
        'sub_accounts': 'sub_accounts',  # noqa: E501
        'last_reconciliation_date': 'last_reconciliation_date',  # noqa: E501
        'row_version': 'row_version',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'categories',  # noqa: E501
        'sub_accounts',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LedgerAccount - a model defined in OpenAPI

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
            display_id (str): The human readable display ID used when displaying the account. [optional]  # noqa: E501
            nominal_code (str, none_type): The nominal code of the ledger account.. [optional]  # noqa: E501
            code (str, none_type): The code assigned to the account.. [optional]  # noqa: E501
            classification (str, none_type): The classification of account.. [optional]  # noqa: E501
            type (str): The type of account.. [optional]  # noqa: E501
            sub_type (str, none_type): The sub type of account.. [optional]  # noqa: E501
            name (str, none_type): The name of the account.. [optional]  # noqa: E501
            fully_qualified_name (str, none_type): The fully qualified name of the account.. [optional]  # noqa: E501
            description (str, none_type): The description of the account.. [optional]  # noqa: E501
            opening_balance (float, none_type): The opening balance of the account.. [optional]  # noqa: E501
            current_balance (float, none_type): The current balance of the account.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            tax_type (str, none_type): The tax type of the account.. [optional]  # noqa: E501
            tax_rate (LinkedTaxRate): [optional]  # noqa: E501
            level (float, none_type): [optional]  # noqa: E501
            active (bool, none_type): Whether the account is active or not.. [optional]  # noqa: E501
            status (str, none_type): The status of the account.. [optional]  # noqa: E501
            header (bool, none_type): Whether the account is a header or not.. [optional]  # noqa: E501
            bank_account (BankAccount): [optional]  # noqa: E501
            categories ([LedgerAccountCategories]): The categories of the account.. [optional]  # noqa: E501
            parent_account (LedgerAccountParentAccount): [optional]  # noqa: E501
            sub_account (bool, none_type): Whether the account is a sub account or not.. [optional]  # noqa: E501
            sub_accounts ([bool, date, datetime, dict, float, int, list, str, none_type]): The sub accounts of the account.. [optional]  # noqa: E501
            last_reconciliation_date (date, none_type): Reconciliation Date means the last calendar day of each Reconciliation Period.. [optional]  # noqa: E501
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
        """LedgerAccount - a model defined in OpenAPI

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
            display_id (str): The human readable display ID used when displaying the account. [optional]  # noqa: E501
            nominal_code (str, none_type): The nominal code of the ledger account.. [optional]  # noqa: E501
            code (str, none_type): The code assigned to the account.. [optional]  # noqa: E501
            classification (str, none_type): The classification of account.. [optional]  # noqa: E501
            type (str): The type of account.. [optional]  # noqa: E501
            sub_type (str, none_type): The sub type of account.. [optional]  # noqa: E501
            name (str, none_type): The name of the account.. [optional]  # noqa: E501
            fully_qualified_name (str, none_type): The fully qualified name of the account.. [optional]  # noqa: E501
            description (str, none_type): The description of the account.. [optional]  # noqa: E501
            opening_balance (float, none_type): The opening balance of the account.. [optional]  # noqa: E501
            current_balance (float, none_type): The current balance of the account.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            tax_type (str, none_type): The tax type of the account.. [optional]  # noqa: E501
            tax_rate (LinkedTaxRate): [optional]  # noqa: E501
            level (float, none_type): [optional]  # noqa: E501
            active (bool, none_type): Whether the account is active or not.. [optional]  # noqa: E501
            status (str, none_type): The status of the account.. [optional]  # noqa: E501
            header (bool, none_type): Whether the account is a header or not.. [optional]  # noqa: E501
            bank_account (BankAccount): [optional]  # noqa: E501
            categories ([LedgerAccountCategories]): The categories of the account.. [optional]  # noqa: E501
            parent_account (LedgerAccountParentAccount): [optional]  # noqa: E501
            sub_account (bool, none_type): Whether the account is a sub account or not.. [optional]  # noqa: E501
            sub_accounts ([bool, date, datetime, dict, float, int, list, str, none_type]): The sub accounts of the account.. [optional]  # noqa: E501
            last_reconciliation_date (date, none_type): Reconciliation Date means the last calendar day of each Reconciliation Period.. [optional]  # noqa: E501
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
