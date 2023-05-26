"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.5.0
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
    from apideck.model.unified_api_id import UnifiedApiId
    from apideck.model.webhook_event_log_attempts import WebhookEventLogAttempts
    from apideck.model.webhook_event_log_service import WebhookEventLogService
    globals()['UnifiedApiId'] = UnifiedApiId
    globals()['WebhookEventLogAttempts'] = WebhookEventLogAttempts
    globals()['WebhookEventLogService'] = WebhookEventLogService


class WebhookEventLog(ModelNormal):
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
    }

    validations = {
        ('endpoint',): {
            'regex': {
                'pattern': r'^(https?):\/\/',  # noqa: E501
            },
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
            'id': (str,),  # noqa: E501
            'status_code': (int,),  # noqa: E501
            'success': (bool,),  # noqa: E501
            'application_id': (str,),  # noqa: E501
            'consumer_id': (str,),  # noqa: E501
            'unified_api': (UnifiedApiId,),  # noqa: E501
            'service': (WebhookEventLogService,),  # noqa: E501
            'endpoint': (str,),  # noqa: E501
            'event_type': (str,),  # noqa: E501
            'execution_attempt': (float,),  # noqa: E501
            'http_method': (str,),  # noqa: E501
            'timestamp': (str,),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'request_body': (str,),  # noqa: E501
            'response_body': (str,),  # noqa: E501
            'retry_scheduled': (bool,),  # noqa: E501
            'attempts': ([WebhookEventLogAttempts],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'status_code': 'status_code',  # noqa: E501
        'success': 'success',  # noqa: E501
        'application_id': 'application_id',  # noqa: E501
        'consumer_id': 'consumer_id',  # noqa: E501
        'unified_api': 'unified_api',  # noqa: E501
        'service': 'service',  # noqa: E501
        'endpoint': 'endpoint',  # noqa: E501
        'event_type': 'event_type',  # noqa: E501
        'execution_attempt': 'execution_attempt',  # noqa: E501
        'http_method': 'http_method',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'entity_type': 'entity_type',  # noqa: E501
        'request_body': 'request_body',  # noqa: E501
        'response_body': 'response_body',  # noqa: E501
        'retry_scheduled': 'retry_scheduled',  # noqa: E501
        'attempts': 'attempts',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """WebhookEventLog - a model defined in OpenAPI

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
            status_code (int): HTTP Status code that was returned.. [optional]  # noqa: E501
            success (bool): Whether or not the request was successful.. [optional]  # noqa: E501
            application_id (str): ID of your Apideck Application. [optional]  # noqa: E501
            consumer_id (str): Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn't exist yet, Vault will upsert a consumer based on your ID.. [optional]  # noqa: E501
            unified_api (UnifiedApiId): [optional]  # noqa: E501
            service (WebhookEventLogService): [optional]  # noqa: E501
            endpoint (str): The URL of the webhook endpoint.. [optional]  # noqa: E501
            event_type (str): Name of source event that webhook is subscribed to.. [optional]  # noqa: E501
            execution_attempt (float): Number of attempts webhook endpoint was called before a success was returned or eventually failed. [optional]  # noqa: E501
            http_method (str): HTTP Method of request to endpoint.. [optional]  # noqa: E501
            timestamp (str): ISO Date and time when the request was made.. [optional]  # noqa: E501
            entity_type (str): Name of the Entity described by the attributes delivered within payload. [optional]  # noqa: E501
            request_body (str): The JSON stringified payload that was delivered to the webhook endpoint.. [optional]  # noqa: E501
            response_body (str): The JSON stringified response that was returned from the webhook endpoint.. [optional]  # noqa: E501
            retry_scheduled (bool): If the request has not hit the max retry limit and will be retried.. [optional]  # noqa: E501
            attempts ([WebhookEventLogAttempts]): record of each attempt to call webhook endpoint. [optional]  # noqa: E501
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
        """WebhookEventLog - a model defined in OpenAPI

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
            status_code (int): HTTP Status code that was returned.. [optional]  # noqa: E501
            success (bool): Whether or not the request was successful.. [optional]  # noqa: E501
            application_id (str): ID of your Apideck Application. [optional]  # noqa: E501
            consumer_id (str): Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn't exist yet, Vault will upsert a consumer based on your ID.. [optional]  # noqa: E501
            unified_api (UnifiedApiId): [optional]  # noqa: E501
            service (WebhookEventLogService): [optional]  # noqa: E501
            endpoint (str): The URL of the webhook endpoint.. [optional]  # noqa: E501
            event_type (str): Name of source event that webhook is subscribed to.. [optional]  # noqa: E501
            execution_attempt (float): Number of attempts webhook endpoint was called before a success was returned or eventually failed. [optional]  # noqa: E501
            http_method (str): HTTP Method of request to endpoint.. [optional]  # noqa: E501
            timestamp (str): ISO Date and time when the request was made.. [optional]  # noqa: E501
            entity_type (str): Name of the Entity described by the attributes delivered within payload. [optional]  # noqa: E501
            request_body (str): The JSON stringified payload that was delivered to the webhook endpoint.. [optional]  # noqa: E501
            response_body (str): The JSON stringified response that was returned from the webhook endpoint.. [optional]  # noqa: E501
            retry_scheduled (bool): If the request has not hit the max retry limit and will be retried.. [optional]  # noqa: E501
            attempts ([WebhookEventLogAttempts]): record of each attempt to call webhook endpoint. [optional]  # noqa: E501
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
