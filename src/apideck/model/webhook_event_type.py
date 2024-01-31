"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.0
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



class WebhookEventType(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            '*': "*",
            'CRM.ACTIVITY.CREATED': "crm.activity.created",
            'CRM.ACTIVITY.UPDATED': "crm.activity.updated",
            'CRM.ACTIVITY.DELETED': "crm.activity.deleted",
            'CRM.COMPANY.CREATED': "crm.company.created",
            'CRM.COMPANY.UPDATED': "crm.company.updated",
            'CRM.COMPANY.DELETED': "crm.company.deleted",
            'CRM.CONTACT.CREATED': "crm.contact.created",
            'CRM.CONTACT.UPDATED': "crm.contact.updated",
            'CRM.CONTACT.DELETED': "crm.contact.deleted",
            'CRM.LEAD.CREATED': "crm.lead.created",
            'CRM.LEAD.UPDATED': "crm.lead.updated",
            'CRM.LEAD.DELETED': "crm.lead.deleted",
            'CRM.NOTE.CREATED': "crm.note.created",
            'CRM.NOTES.UPDATED': "crm.notes.updated",
            'CRM.NOTES.DELETED': "crm.notes.deleted",
            'CRM.OPPORTUNITY.CREATED': "crm.opportunity.created",
            'CRM.OPPORTUNITY.UPDATED': "crm.opportunity.updated",
            'CRM.OPPORTUNITY.DELETED': "crm.opportunity.deleted",
            'LEAD.LEAD.CREATED': "lead.lead.created",
            'LEAD.LEAD.UPDATED': "lead.lead.updated",
            'LEAD.LEAD.DELETED': "lead.lead.deleted",
            'VAULT.CONNECTION.CREATED': "vault.connection.created",
            'VAULT.CONNECTION.UPDATED': "vault.connection.updated",
            'VAULT.CONNECTION.DISABLED': "vault.connection.disabled",
            'VAULT.CONNECTION.DELETED': "vault.connection.deleted",
            'VAULT.CONNECTION.CALLABLE': "vault.connection.callable",
            'VAULT.CONNECTION.REVOKED': "vault.connection.revoked",
            'VAULT.CONNECTION.TOKEN_REFRESH.FAILED': "vault.connection.token_refresh.failed",
            'ATS.JOB.CREATED': "ats.job.created",
            'ATS.JOB.UPDATED': "ats.job.updated",
            'ATS.JOB.DELETED': "ats.job.deleted",
            'ATS.APPLICANT.CREATED': "ats.applicant.created",
            'ATS.APPLICANT.UPDATED': "ats.applicant.updated",
            'ATS.APPLICANT.DELETED': "ats.applicant.deleted",
            'ACCOUNTING.CUSTOMER.CREATED': "accounting.customer.created",
            'ACCOUNTING.CUSTOMER.UPDATED': "accounting.customer.updated",
            'ACCOUNTING.CUSTOMER.DELETED': "accounting.customer.deleted",
            'ACCOUNTING.INVOICE.CREATED': "accounting.invoice.created",
            'ACCOUNTING.INVOICE.UPDATED': "accounting.invoice.updated",
            'ACCOUNTING.INVOICE.DELETED': "accounting.invoice.deleted",
            'ACCOUNTING.INVOICE_ITEM.CREATED': "accounting.invoice_item.created",
            'ACCOUNTING.INVOICE_ITEM.UPDATED': "accounting.invoice_item.updated",
            'ACCOUNTING.INVOICE_ITEM.DELETED': "accounting.invoice_item.deleted",
            'ACCOUNTING.LEDGER_ACCOUNT.CREATED': "accounting.ledger_account.created",
            'ACCOUNTING.LEDGER_ACCOUNT.UPDATED': "accounting.ledger_account.updated",
            'ACCOUNTING.LEDGER_ACCOUNT.DELETED': "accounting.ledger_account.deleted",
            'ACCOUNTING.TAX_RATE.CREATED': "accounting.tax_rate.created",
            'ACCOUNTING.TAX_RATE.UPDATED': "accounting.tax_rate.updated",
            'ACCOUNTING.TAX_RATE.DELETED': "accounting.tax_rate.deleted",
            'ACCOUNTING.BILL.CREATED': "accounting.bill.created",
            'ACCOUNTING.BILL.UPDATED': "accounting.bill.updated",
            'ACCOUNTING.BILL.DELETED': "accounting.bill.deleted",
            'ACCOUNTING.PAYMENT.CREATED': "accounting.payment.created",
            'ACCOUNTING.PAYMENT.UPDATED': "accounting.payment.updated",
            'ACCOUNTING.PAYMENT.DELETED': "accounting.payment.deleted",
            'ACCOUNTING.SUPPLIER.CREATED': "accounting.supplier.created",
            'ACCOUNTING.SUPPLIER.UPDATED': "accounting.supplier.updated",
            'ACCOUNTING.SUPPLIER.DELETED': "accounting.supplier.deleted",
            'ACCOUNTING.PURCHASE-ORDER.CREATED': "accounting.purchase-order.created",
            'ACCOUNTING.PURCHASE-ORDER.UPDATED': "accounting.purchase-order.updated",
            'ACCOUNTING.PURCHASE-ORDER.DELETED': "accounting.purchase-order.deleted",
            'POS.ORDER.CREATED': "pos.order.created",
            'POS.ORDER.UPDATED': "pos.order.updated",
            'POS.ORDER.DELETED': "pos.order.deleted",
            'POS.PRODUCT.CREATED': "pos.product.created",
            'POS.PRODUCT.UPDATED': "pos.product.updated",
            'POS.PRODUCT.DELETED': "pos.product.deleted",
            'POS.PAYMENT.CREATED': "pos.payment.created",
            'POS.PAYMENT.UPDATED': "pos.payment.updated",
            'POS.PAYMENT.DELETED': "pos.payment.deleted",
            'POS.MERCHANT.CREATED': "pos.merchant.created",
            'POS.MERCHANT.UPDATED': "pos.merchant.updated",
            'POS.MERCHANT.DELETED': "pos.merchant.deleted",
            'POS.LOCATION.CREATED': "pos.location.created",
            'POS.LOCATION.UPDATED': "pos.location.updated",
            'POS.LOCATION.DELETED': "pos.location.deleted",
            'POS.ITEM.CREATED': "pos.item.created",
            'POS.ITEM.UPDATED': "pos.item.updated",
            'POS.ITEM.DELETED': "pos.item.deleted",
            'POS.MODIFIER.CREATED': "pos.modifier.created",
            'POS.MODIFIER.UPDATED': "pos.modifier.updated",
            'POS.MODIFIER.DELETED': "pos.modifier.deleted",
            'POS.MODIFIER-GROUP.CREATED': "pos.modifier-group.created",
            'POS.MODIFIER-GROUP.UPDATED': "pos.modifier-group.updated",
            'POS.MODIFIER-GROUP.DELETED': "pos.modifier-group.deleted",
            'HRIS.EMPLOYEE.CREATED': "hris.employee.created",
            'HRIS.EMPLOYEE.UPDATED': "hris.employee.updated",
            'HRIS.EMPLOYEE.DELETED': "hris.employee.deleted",
            'HRIS.EMPLOYEE.TERMINATED': "hris.employee.terminated",
            'HRIS.COMPANY.CREATED': "hris.company.created",
            'HRIS.COMPANY.UPDATED': "hris.company.updated",
            'HRIS.COMPANY.DELETED': "hris.company.deleted",
            'FILE-STORAGE.FILE.CREATED': "file-storage.file.created",
            'FILE-STORAGE.FILE.UPDATED': "file-storage.file.updated",
            'FILE-STORAGE.FILE.DELETED': "file-storage.file.deleted",
            'ISSUE-TRACKING.TICKET.CREATED': "issue-tracking.ticket.created",
            'ISSUE-TRACKING.TICKET.UPDATED': "issue-tracking.ticket.updated",
            'ISSUE-TRACKING.TICKET.DELETED': "issue-tracking.ticket.deleted",
            'ATS.APPLICATION.CREATED': "ats.application.created",
            'ATS.APPLICATION.UPDATED': "ats.application.updated",
            'ATS.APPLICATION.DELETED': "ats.application.deleted",
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
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """WebhookEventType - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["*", "crm.activity.created", "crm.activity.updated", "crm.activity.deleted", "crm.company.created", "crm.company.updated", "crm.company.deleted", "crm.contact.created", "crm.contact.updated", "crm.contact.deleted", "crm.lead.created", "crm.lead.updated", "crm.lead.deleted", "crm.note.created", "crm.notes.updated", "crm.notes.deleted", "crm.opportunity.created", "crm.opportunity.updated", "crm.opportunity.deleted", "lead.lead.created", "lead.lead.updated", "lead.lead.deleted", "vault.connection.created", "vault.connection.updated", "vault.connection.disabled", "vault.connection.deleted", "vault.connection.callable", "vault.connection.revoked", "vault.connection.token_refresh.failed", "ats.job.created", "ats.job.updated", "ats.job.deleted", "ats.applicant.created", "ats.applicant.updated", "ats.applicant.deleted", "accounting.customer.created", "accounting.customer.updated", "accounting.customer.deleted", "accounting.invoice.created", "accounting.invoice.updated", "accounting.invoice.deleted", "accounting.invoice_item.created", "accounting.invoice_item.updated", "accounting.invoice_item.deleted", "accounting.ledger_account.created", "accounting.ledger_account.updated", "accounting.ledger_account.deleted", "accounting.tax_rate.created", "accounting.tax_rate.updated", "accounting.tax_rate.deleted", "accounting.bill.created", "accounting.bill.updated", "accounting.bill.deleted", "accounting.payment.created", "accounting.payment.updated", "accounting.payment.deleted", "accounting.supplier.created", "accounting.supplier.updated", "accounting.supplier.deleted", "accounting.purchase-order.created", "accounting.purchase-order.updated", "accounting.purchase-order.deleted", "pos.order.created", "pos.order.updated", "pos.order.deleted", "pos.product.created", "pos.product.updated", "pos.product.deleted", "pos.payment.created", "pos.payment.updated", "pos.payment.deleted", "pos.merchant.created", "pos.merchant.updated", "pos.merchant.deleted", "pos.location.created", "pos.location.updated", "pos.location.deleted", "pos.item.created", "pos.item.updated", "pos.item.deleted", "pos.modifier.created", "pos.modifier.updated", "pos.modifier.deleted", "pos.modifier-group.created", "pos.modifier-group.updated", "pos.modifier-group.deleted", "hris.employee.created", "hris.employee.updated", "hris.employee.deleted", "hris.employee.terminated", "hris.company.created", "hris.company.updated", "hris.company.deleted", "file-storage.file.created", "file-storage.file.updated", "file-storage.file.deleted", "issue-tracking.ticket.created", "issue-tracking.ticket.updated", "issue-tracking.ticket.deleted", "ats.application.created", "ats.application.updated", "ats.application.deleted", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["*", "crm.activity.created", "crm.activity.updated", "crm.activity.deleted", "crm.company.created", "crm.company.updated", "crm.company.deleted", "crm.contact.created", "crm.contact.updated", "crm.contact.deleted", "crm.lead.created", "crm.lead.updated", "crm.lead.deleted", "crm.note.created", "crm.notes.updated", "crm.notes.deleted", "crm.opportunity.created", "crm.opportunity.updated", "crm.opportunity.deleted", "lead.lead.created", "lead.lead.updated", "lead.lead.deleted", "vault.connection.created", "vault.connection.updated", "vault.connection.disabled", "vault.connection.deleted", "vault.connection.callable", "vault.connection.revoked", "vault.connection.token_refresh.failed", "ats.job.created", "ats.job.updated", "ats.job.deleted", "ats.applicant.created", "ats.applicant.updated", "ats.applicant.deleted", "accounting.customer.created", "accounting.customer.updated", "accounting.customer.deleted", "accounting.invoice.created", "accounting.invoice.updated", "accounting.invoice.deleted", "accounting.invoice_item.created", "accounting.invoice_item.updated", "accounting.invoice_item.deleted", "accounting.ledger_account.created", "accounting.ledger_account.updated", "accounting.ledger_account.deleted", "accounting.tax_rate.created", "accounting.tax_rate.updated", "accounting.tax_rate.deleted", "accounting.bill.created", "accounting.bill.updated", "accounting.bill.deleted", "accounting.payment.created", "accounting.payment.updated", "accounting.payment.deleted", "accounting.supplier.created", "accounting.supplier.updated", "accounting.supplier.deleted", "accounting.purchase-order.created", "accounting.purchase-order.updated", "accounting.purchase-order.deleted", "pos.order.created", "pos.order.updated", "pos.order.deleted", "pos.product.created", "pos.product.updated", "pos.product.deleted", "pos.payment.created", "pos.payment.updated", "pos.payment.deleted", "pos.merchant.created", "pos.merchant.updated", "pos.merchant.deleted", "pos.location.created", "pos.location.updated", "pos.location.deleted", "pos.item.created", "pos.item.updated", "pos.item.deleted", "pos.modifier.created", "pos.modifier.updated", "pos.modifier.deleted", "pos.modifier-group.created", "pos.modifier-group.updated", "pos.modifier-group.deleted", "hris.employee.created", "hris.employee.updated", "hris.employee.deleted", "hris.employee.terminated", "hris.company.created", "hris.company.updated", "hris.company.deleted", "file-storage.file.created", "file-storage.file.updated", "file-storage.file.deleted", "issue-tracking.ticket.created", "issue-tracking.ticket.updated", "issue-tracking.ticket.deleted", "ats.application.created", "ats.application.updated", "ats.application.deleted", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """WebhookEventType - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["*", "crm.activity.created", "crm.activity.updated", "crm.activity.deleted", "crm.company.created", "crm.company.updated", "crm.company.deleted", "crm.contact.created", "crm.contact.updated", "crm.contact.deleted", "crm.lead.created", "crm.lead.updated", "crm.lead.deleted", "crm.note.created", "crm.notes.updated", "crm.notes.deleted", "crm.opportunity.created", "crm.opportunity.updated", "crm.opportunity.deleted", "lead.lead.created", "lead.lead.updated", "lead.lead.deleted", "vault.connection.created", "vault.connection.updated", "vault.connection.disabled", "vault.connection.deleted", "vault.connection.callable", "vault.connection.revoked", "vault.connection.token_refresh.failed", "ats.job.created", "ats.job.updated", "ats.job.deleted", "ats.applicant.created", "ats.applicant.updated", "ats.applicant.deleted", "accounting.customer.created", "accounting.customer.updated", "accounting.customer.deleted", "accounting.invoice.created", "accounting.invoice.updated", "accounting.invoice.deleted", "accounting.invoice_item.created", "accounting.invoice_item.updated", "accounting.invoice_item.deleted", "accounting.ledger_account.created", "accounting.ledger_account.updated", "accounting.ledger_account.deleted", "accounting.tax_rate.created", "accounting.tax_rate.updated", "accounting.tax_rate.deleted", "accounting.bill.created", "accounting.bill.updated", "accounting.bill.deleted", "accounting.payment.created", "accounting.payment.updated", "accounting.payment.deleted", "accounting.supplier.created", "accounting.supplier.updated", "accounting.supplier.deleted", "accounting.purchase-order.created", "accounting.purchase-order.updated", "accounting.purchase-order.deleted", "pos.order.created", "pos.order.updated", "pos.order.deleted", "pos.product.created", "pos.product.updated", "pos.product.deleted", "pos.payment.created", "pos.payment.updated", "pos.payment.deleted", "pos.merchant.created", "pos.merchant.updated", "pos.merchant.deleted", "pos.location.created", "pos.location.updated", "pos.location.deleted", "pos.item.created", "pos.item.updated", "pos.item.deleted", "pos.modifier.created", "pos.modifier.updated", "pos.modifier.deleted", "pos.modifier-group.created", "pos.modifier-group.updated", "pos.modifier-group.deleted", "hris.employee.created", "hris.employee.updated", "hris.employee.deleted", "hris.employee.terminated", "hris.company.created", "hris.company.updated", "hris.company.deleted", "file-storage.file.created", "file-storage.file.updated", "file-storage.file.deleted", "issue-tracking.ticket.created", "issue-tracking.ticket.updated", "issue-tracking.ticket.deleted", "ats.application.created", "ats.application.updated", "ats.application.deleted", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["*", "crm.activity.created", "crm.activity.updated", "crm.activity.deleted", "crm.company.created", "crm.company.updated", "crm.company.deleted", "crm.contact.created", "crm.contact.updated", "crm.contact.deleted", "crm.lead.created", "crm.lead.updated", "crm.lead.deleted", "crm.note.created", "crm.notes.updated", "crm.notes.deleted", "crm.opportunity.created", "crm.opportunity.updated", "crm.opportunity.deleted", "lead.lead.created", "lead.lead.updated", "lead.lead.deleted", "vault.connection.created", "vault.connection.updated", "vault.connection.disabled", "vault.connection.deleted", "vault.connection.callable", "vault.connection.revoked", "vault.connection.token_refresh.failed", "ats.job.created", "ats.job.updated", "ats.job.deleted", "ats.applicant.created", "ats.applicant.updated", "ats.applicant.deleted", "accounting.customer.created", "accounting.customer.updated", "accounting.customer.deleted", "accounting.invoice.created", "accounting.invoice.updated", "accounting.invoice.deleted", "accounting.invoice_item.created", "accounting.invoice_item.updated", "accounting.invoice_item.deleted", "accounting.ledger_account.created", "accounting.ledger_account.updated", "accounting.ledger_account.deleted", "accounting.tax_rate.created", "accounting.tax_rate.updated", "accounting.tax_rate.deleted", "accounting.bill.created", "accounting.bill.updated", "accounting.bill.deleted", "accounting.payment.created", "accounting.payment.updated", "accounting.payment.deleted", "accounting.supplier.created", "accounting.supplier.updated", "accounting.supplier.deleted", "accounting.purchase-order.created", "accounting.purchase-order.updated", "accounting.purchase-order.deleted", "pos.order.created", "pos.order.updated", "pos.order.deleted", "pos.product.created", "pos.product.updated", "pos.product.deleted", "pos.payment.created", "pos.payment.updated", "pos.payment.deleted", "pos.merchant.created", "pos.merchant.updated", "pos.merchant.deleted", "pos.location.created", "pos.location.updated", "pos.location.deleted", "pos.item.created", "pos.item.updated", "pos.item.deleted", "pos.modifier.created", "pos.modifier.updated", "pos.modifier.deleted", "pos.modifier-group.created", "pos.modifier-group.updated", "pos.modifier-group.deleted", "hris.employee.created", "hris.employee.updated", "hris.employee.deleted", "hris.employee.terminated", "hris.company.created", "hris.company.updated", "hris.company.deleted", "file-storage.file.created", "file-storage.file.updated", "file-storage.file.deleted", "issue-tracking.ticket.created", "issue-tracking.ticket.updated", "issue-tracking.ticket.deleted", "ats.application.created", "ats.application.updated", "ats.application.deleted", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
