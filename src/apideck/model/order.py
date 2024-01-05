"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.2.0
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
    from apideck.model.order_customers import OrderCustomers
    from apideck.model.order_discounts import OrderDiscounts
    from apideck.model.order_fulfillments import OrderFulfillments
    from apideck.model.order_line_items import OrderLineItems
    from apideck.model.order_payments import OrderPayments
    from apideck.model.order_refunds import OrderRefunds
    from apideck.model.order_tenders import OrderTenders
    from apideck.model.service_charges import ServiceCharges
    globals()['Currency'] = Currency
    globals()['IdempotencyKey'] = IdempotencyKey
    globals()['OrderCustomers'] = OrderCustomers
    globals()['OrderDiscounts'] = OrderDiscounts
    globals()['OrderFulfillments'] = OrderFulfillments
    globals()['OrderLineItems'] = OrderLineItems
    globals()['OrderPayments'] = OrderPayments
    globals()['OrderRefunds'] = OrderRefunds
    globals()['OrderTenders'] = OrderTenders
    globals()['ServiceCharges'] = ServiceCharges


class Order(ModelNormal):
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
            'OPEN': "open",
            'DRAFT': "draft",
            'DELIVERED': "delivered",
            'DELAYED': "delayed",
            'VOIDED': "voided",
            'COMPLETED': "completed",
            'HIDDEN': "hidden",
        },
        ('payment_status',): {
            'OPEN': "open",
            'PAID': "paid",
            'REFUNDED': "refunded",
            'CREDITED': "credited",
            'PARTIALLY_PAID': "partially_paid",
            'PARTIALLY_REFUNDED': "partially_refunded",
            'UNKNOWN': "unknown",
        },
        ('source',): {
            'None': None,
            'IN-STORE': "in-store",
            'ONLINE': "online",
            'OPT': "opt",
            'API': "api",
            'KIOSK': "kiosk",
            'CALLER-ID': "caller-id",
            'GOOGLE': "google",
            'INVOICE': "invoice",
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
            'merchant_id': (str,),  # noqa: E501
            'location_id': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'idempotency_key': (IdempotencyKey,),  # noqa: E501
            'order_number': (str,),  # noqa: E501
            'order_date': (date, none_type,),  # noqa: E501
            'closed_date': (date, none_type,),  # noqa: E501
            'reference_id': (str, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'payment_status': (str,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'note': (str,),  # noqa: E501
            'customer_id': (str,),  # noqa: E501
            'employee_id': (str,),  # noqa: E501
            'order_type_id': (str,),  # noqa: E501
            'table': (str,),  # noqa: E501
            'seat': (str,),  # noqa: E501
            'total_amount': (int, none_type,),  # noqa: E501
            'total_tip': (int, none_type,),  # noqa: E501
            'total_tax': (int, none_type,),  # noqa: E501
            'total_discount': (int, none_type,),  # noqa: E501
            'total_refund': (int, none_type,),  # noqa: E501
            'total_service_charge': (int, none_type,),  # noqa: E501
            'refunded': (bool,),  # noqa: E501
            'customers': ([OrderCustomers],),  # noqa: E501
            'fulfillments': ([OrderFulfillments],),  # noqa: E501
            'line_items': ([OrderLineItems],),  # noqa: E501
            'payments': ([OrderPayments],),  # noqa: E501
            'service_charges': (ServiceCharges,),  # noqa: E501
            'refunds': ([OrderRefunds],),  # noqa: E501
            'taxes': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'discounts': ([OrderDiscounts],),  # noqa: E501
            'tenders': ([OrderTenders],),  # noqa: E501
            'source': (str, none_type,),  # noqa: E501
            'voided': (bool,),  # noqa: E501
            'voided_at': (datetime,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'version': (str, none_type,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'merchant_id': 'merchant_id',  # noqa: E501
        'location_id': 'location_id',  # noqa: E501
        'id': 'id',  # noqa: E501
        'idempotency_key': 'idempotency_key',  # noqa: E501
        'order_number': 'order_number',  # noqa: E501
        'order_date': 'order_date',  # noqa: E501
        'closed_date': 'closed_date',  # noqa: E501
        'reference_id': 'reference_id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'payment_status': 'payment_status',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'title': 'title',  # noqa: E501
        'note': 'note',  # noqa: E501
        'customer_id': 'customer_id',  # noqa: E501
        'employee_id': 'employee_id',  # noqa: E501
        'order_type_id': 'order_type_id',  # noqa: E501
        'table': 'table',  # noqa: E501
        'seat': 'seat',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'total_tip': 'total_tip',  # noqa: E501
        'total_tax': 'total_tax',  # noqa: E501
        'total_discount': 'total_discount',  # noqa: E501
        'total_refund': 'total_refund',  # noqa: E501
        'total_service_charge': 'total_service_charge',  # noqa: E501
        'refunded': 'refunded',  # noqa: E501
        'customers': 'customers',  # noqa: E501
        'fulfillments': 'fulfillments',  # noqa: E501
        'line_items': 'line_items',  # noqa: E501
        'payments': 'payments',  # noqa: E501
        'service_charges': 'service_charges',  # noqa: E501
        'refunds': 'refunds',  # noqa: E501
        'taxes': 'taxes',  # noqa: E501
        'discounts': 'discounts',  # noqa: E501
        'tenders': 'tenders',  # noqa: E501
        'source': 'source',  # noqa: E501
        'voided': 'voided',  # noqa: E501
        'voided_at': 'voided_at',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'version': 'version',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'source',  # noqa: E501
        'voided_at',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, merchant_id, location_id, *args, **kwargs):  # noqa: E501
        """Order - a model defined in OpenAPI

        Args:
            merchant_id (str):
            location_id (str):

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
            idempotency_key (IdempotencyKey): [optional]  # noqa: E501
            order_number (str): [optional]  # noqa: E501
            order_date (date, none_type): [optional]  # noqa: E501
            closed_date (date, none_type): [optional]  # noqa: E501
            reference_id (str, none_type): An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system.. [optional]  # noqa: E501
            status (str): Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to 'open'. More info [https://docs.clover.com/reference/orderupdateorder](). [optional]  # noqa: E501
            payment_status (str): Is this order paid or not?. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            note (str): A note with information about this order, may be printed on the order receipt and displayed in apps. [optional]  # noqa: E501
            customer_id (str): [optional]  # noqa: E501
            employee_id (str): [optional]  # noqa: E501
            order_type_id (str): [optional]  # noqa: E501
            table (str): [optional]  # noqa: E501
            seat (str): [optional]  # noqa: E501
            total_amount (int, none_type): [optional]  # noqa: E501
            total_tip (int, none_type): [optional]  # noqa: E501
            total_tax (int, none_type): [optional]  # noqa: E501
            total_discount (int, none_type): [optional]  # noqa: E501
            total_refund (int, none_type): [optional]  # noqa: E501
            total_service_charge (int, none_type): [optional]  # noqa: E501
            refunded (bool): [optional]  # noqa: E501
            customers ([OrderCustomers]): [optional]  # noqa: E501
            fulfillments ([OrderFulfillments]): [optional]  # noqa: E501
            line_items ([OrderLineItems]): [optional]  # noqa: E501
            payments ([OrderPayments]): [optional]  # noqa: E501
            service_charges (ServiceCharges): [optional]  # noqa: E501
            refunds ([OrderRefunds]): [optional]  # noqa: E501
            taxes ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            discounts ([OrderDiscounts]): [optional]  # noqa: E501
            tenders ([OrderTenders]): [optional]  # noqa: E501
            source (str, none_type): Source of order. Indicates the way that the order was placed.. [optional]  # noqa: E501
            voided (bool): [optional]  # noqa: E501
            voided_at (datetime): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            version (str, none_type): [optional]  # noqa: E501
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

        self.merchant_id = merchant_id
        self.location_id = location_id
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
    def __init__(self, merchant_id, location_id, *args, **kwargs):  # noqa: E501
        """Order - a model defined in OpenAPI

        Args:
            merchant_id (str):
            location_id (str):

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
            idempotency_key (IdempotencyKey): [optional]  # noqa: E501
            order_number (str): [optional]  # noqa: E501
            order_date (date, none_type): [optional]  # noqa: E501
            closed_date (date, none_type): [optional]  # noqa: E501
            reference_id (str, none_type): An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system.. [optional]  # noqa: E501
            status (str): Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to 'open'. More info [https://docs.clover.com/reference/orderupdateorder](). [optional]  # noqa: E501
            payment_status (str): Is this order paid or not?. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            note (str): A note with information about this order, may be printed on the order receipt and displayed in apps. [optional]  # noqa: E501
            customer_id (str): [optional]  # noqa: E501
            employee_id (str): [optional]  # noqa: E501
            order_type_id (str): [optional]  # noqa: E501
            table (str): [optional]  # noqa: E501
            seat (str): [optional]  # noqa: E501
            total_amount (int, none_type): [optional]  # noqa: E501
            total_tip (int, none_type): [optional]  # noqa: E501
            total_tax (int, none_type): [optional]  # noqa: E501
            total_discount (int, none_type): [optional]  # noqa: E501
            total_refund (int, none_type): [optional]  # noqa: E501
            total_service_charge (int, none_type): [optional]  # noqa: E501
            refunded (bool): [optional]  # noqa: E501
            customers ([OrderCustomers]): [optional]  # noqa: E501
            fulfillments ([OrderFulfillments]): [optional]  # noqa: E501
            line_items ([OrderLineItems]): [optional]  # noqa: E501
            payments ([OrderPayments]): [optional]  # noqa: E501
            service_charges (ServiceCharges): [optional]  # noqa: E501
            refunds ([OrderRefunds]): [optional]  # noqa: E501
            taxes ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            discounts ([OrderDiscounts]): [optional]  # noqa: E501
            tenders ([OrderTenders]): [optional]  # noqa: E501
            source (str, none_type): Source of order. Indicates the way that the order was placed.. [optional]  # noqa: E501
            voided (bool): [optional]  # noqa: E501
            voided_at (datetime): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            version (str, none_type): [optional]  # noqa: E501
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

        self.merchant_id = merchant_id
        self.location_id = location_id
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
