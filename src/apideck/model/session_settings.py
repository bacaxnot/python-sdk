"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.9.3
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
    globals()['UnifiedApiId'] = UnifiedApiId


class SessionSettings(ModelNormal):
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
        ('allow_actions',): {
            'DELETE': "delete",
            'DISCONNECT': "disconnect",
            'REAUTHORIZE': "reauthorize",
            'DISABLE': "disable",
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
            'unified_apis': ([UnifiedApiId],),  # noqa: E501
            'hide_resource_settings': (bool,),  # noqa: E501
            'sandbox_mode': (bool,),  # noqa: E501
            'isolation_mode': (bool,),  # noqa: E501
            'session_length': (str,),  # noqa: E501
            'show_logs': (bool,),  # noqa: E501
            'show_suggestions': (bool,),  # noqa: E501
            'show_sidebar': (bool,),  # noqa: E501
            'auto_redirect': (bool,),  # noqa: E501
            'hide_guides': (bool,),  # noqa: E501
            'allow_actions': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'unified_apis': 'unified_apis',  # noqa: E501
        'hide_resource_settings': 'hide_resource_settings',  # noqa: E501
        'sandbox_mode': 'sandbox_mode',  # noqa: E501
        'isolation_mode': 'isolation_mode',  # noqa: E501
        'session_length': 'session_length',  # noqa: E501
        'show_logs': 'show_logs',  # noqa: E501
        'show_suggestions': 'show_suggestions',  # noqa: E501
        'show_sidebar': 'show_sidebar',  # noqa: E501
        'auto_redirect': 'auto_redirect',  # noqa: E501
        'hide_guides': 'hide_guides',  # noqa: E501
        'allow_actions': 'allow_actions',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SessionSettings - a model defined in OpenAPI

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
            unified_apis ([UnifiedApiId]): Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs.. [optional]  # noqa: E501
            hide_resource_settings (bool): A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user.. [optional] if omitted the server will use the default value of False  # noqa: E501
            sandbox_mode (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment.. [optional] if omitted the server will use the default value of False  # noqa: E501
            isolation_mode (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items.. [optional] if omitted the server will use the default value of False  # noqa: E501
            session_length (str): The duration of time the session is valid for (maximum 1 week).. [optional] if omitted the server will use the default value of "1h"  # noqa: E501
            show_logs (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to `true`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            show_suggestions (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_sidebar (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to `true`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            auto_redirect (bool): Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            hide_guides (bool): Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            allow_actions ([str]): Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in `allow_actions` will be shown on a connection in Vault. Available actions are: `delete`, `disconnect`, `reauthorize` and `disable`. Empty array will hide all actions. By default all actions are visible.. [optional]  # noqa: E501
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
        """SessionSettings - a model defined in OpenAPI

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
            unified_apis ([UnifiedApiId]): Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs.. [optional]  # noqa: E501
            hide_resource_settings (bool): A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user.. [optional] if omitted the server will use the default value of False  # noqa: E501
            sandbox_mode (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment.. [optional] if omitted the server will use the default value of False  # noqa: E501
            isolation_mode (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items.. [optional] if omitted the server will use the default value of False  # noqa: E501
            session_length (str): The duration of time the session is valid for (maximum 1 week).. [optional] if omitted the server will use the default value of "1h"  # noqa: E501
            show_logs (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to `true`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            show_suggestions (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_sidebar (bool): Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to `true`.. [optional] if omitted the server will use the default value of True  # noqa: E501
            auto_redirect (bool): Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            hide_guides (bool): Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            allow_actions ([str]): Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in `allow_actions` will be shown on a connection in Vault. Available actions are: `delete`, `disconnect`, `reauthorize` and `disable`. Empty array will hide all actions. By default all actions are visible.. [optional]  # noqa: E501
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
