"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.2.2
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
    from apideck.model.log_operation import LogOperation
    from apideck.model.log_service import LogService
    globals()['LogOperation'] = LogOperation
    globals()['LogService'] = LogService


class Log(ModelNormal):
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
        ('unified_api',): {
            'CRM': "crm",
            'LEAD': "lead",
            'PROXY': "proxy",
            'VAULT': "vault",
            'ACCOUNTING': "accounting",
            'HRIS': "hris",
            'ATS': "ats",
            'ECOMMERCE': "ecommerce",
            'ISSUE-TRACKING': "issue-tracking",
            'POS': "pos",
            'FILE-STORAGE': "file-storage",
            'SMS': "sms",
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
            'api_style': (str,),  # noqa: E501
            'base_url': (str,),  # noqa: E501
            'child_request': (bool,),  # noqa: E501
            'consumer_id': (str,),  # noqa: E501
            'duration': (float,),  # noqa: E501
            'execution': (int,),  # noqa: E501
            'has_children': (bool,),  # noqa: E501
            'http_method': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'latency': (float,),  # noqa: E501
            'operation': (LogOperation,),  # noqa: E501
            'parent_id': (str, none_type,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'sandbox': (bool,),  # noqa: E501
            'service': (LogService,),  # noqa: E501
            'status_code': (int,),  # noqa: E501
            'success': (bool,),  # noqa: E501
            'timestamp': (str,),  # noqa: E501
            'unified_api': (str,),  # noqa: E501
            'error_message': (str, none_type,),  # noqa: E501
            'source_ip': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'api_style': 'api_style',  # noqa: E501
        'base_url': 'base_url',  # noqa: E501
        'child_request': 'child_request',  # noqa: E501
        'consumer_id': 'consumer_id',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'execution': 'execution',  # noqa: E501
        'has_children': 'has_children',  # noqa: E501
        'http_method': 'http_method',  # noqa: E501
        'id': 'id',  # noqa: E501
        'latency': 'latency',  # noqa: E501
        'operation': 'operation',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'path': 'path',  # noqa: E501
        'sandbox': 'sandbox',  # noqa: E501
        'service': 'service',  # noqa: E501
        'status_code': 'status_code',  # noqa: E501
        'success': 'success',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'unified_api': 'unified_api',  # noqa: E501
        'error_message': 'error_message',  # noqa: E501
        'source_ip': 'source_ip',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, api_style, base_url, child_request, consumer_id, duration, execution, has_children, http_method, id, latency, operation, parent_id, path, sandbox, service, status_code, success, timestamp, unified_api, *args, **kwargs):  # noqa: E501
        """Log - a model defined in OpenAPI

        Args:
            api_style (str): Indicates if the request was made via REST or Graphql endpoint.
            base_url (str): The Apideck base URL the request was made to.
            child_request (bool): Indicates whether or not this is a child or parent request.
            consumer_id (str): The consumer Id associated with the request.
            duration (float): The entire execution time in milliseconds it took to call the Apideck service provider.
            execution (int): The entire execution time in milliseconds it took to make the request.
            has_children (bool): When request is a parent request, this indicates if there are child requests associated.
            http_method (str): HTTP Method of request.
            id (str): UUID acting as Request Identifier.
            latency (float): Latency added by making this request via Unified Api.
            operation (LogOperation):
            parent_id (str, none_type): When request is a child request, this UUID indicates it's parent request.
            path (str): The path component of the URI the request was made to.
            sandbox (bool): Indicates whether the request was made using Apidecks sandbox credentials or not.
            service (LogService):
            status_code (int): HTTP Status code that was returned.
            success (bool): Whether or not the request was successful.
            timestamp (str): ISO Date and time when the request was made.
            unified_api (str): Which Unified Api request was made to.

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
            error_message (str, none_type): If error occurred, this is brief explanation. [optional]  # noqa: E501
            source_ip (str, none_type): The IP address of the source of the request.. [optional]  # noqa: E501
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

        self.api_style = api_style
        self.base_url = base_url
        self.child_request = child_request
        self.consumer_id = consumer_id
        self.duration = duration
        self.execution = execution
        self.has_children = has_children
        self.http_method = http_method
        self.id = id
        self.latency = latency
        self.operation = operation
        self.parent_id = parent_id
        self.path = path
        self.sandbox = sandbox
        self.service = service
        self.status_code = status_code
        self.success = success
        self.timestamp = timestamp
        self.unified_api = unified_api
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
    def __init__(self, api_style, base_url, child_request, consumer_id, duration, execution, has_children, http_method, id, latency, operation, parent_id, path, sandbox, service, status_code, success, timestamp, unified_api, *args, **kwargs):  # noqa: E501
        """Log - a model defined in OpenAPI

        Args:
            api_style (str): Indicates if the request was made via REST or Graphql endpoint.
            base_url (str): The Apideck base URL the request was made to.
            child_request (bool): Indicates whether or not this is a child or parent request.
            consumer_id (str): The consumer Id associated with the request.
            duration (float): The entire execution time in milliseconds it took to call the Apideck service provider.
            execution (int): The entire execution time in milliseconds it took to make the request.
            has_children (bool): When request is a parent request, this indicates if there are child requests associated.
            http_method (str): HTTP Method of request.
            id (str): UUID acting as Request Identifier.
            latency (float): Latency added by making this request via Unified Api.
            operation (LogOperation):
            parent_id (str, none_type): When request is a child request, this UUID indicates it's parent request.
            path (str): The path component of the URI the request was made to.
            sandbox (bool): Indicates whether the request was made using Apidecks sandbox credentials or not.
            service (LogService):
            status_code (int): HTTP Status code that was returned.
            success (bool): Whether or not the request was successful.
            timestamp (str): ISO Date and time when the request was made.
            unified_api (str): Which Unified Api request was made to.

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
            error_message (str, none_type): If error occurred, this is brief explanation. [optional]  # noqa: E501
            source_ip (str, none_type): The IP address of the source of the request.. [optional]  # noqa: E501
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

        self.api_style = api_style
        self.base_url = base_url
        self.child_request = child_request
        self.consumer_id = consumer_id
        self.duration = duration
        self.execution = execution
        self.has_children = has_children
        self.http_method = http_method
        self.id = id
        self.latency = latency
        self.operation = operation
        self.parent_id = parent_id
        self.path = path
        self.sandbox = sandbox
        self.service = service
        self.status_code = status_code
        self.success = success
        self.timestamp = timestamp
        self.unified_api = unified_api
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
