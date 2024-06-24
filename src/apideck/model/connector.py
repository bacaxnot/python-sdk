"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.1
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
    from apideck.model.connector_doc import ConnectorDoc
    from apideck.model.connector_event import ConnectorEvent
    from apideck.model.connector_oauth_scopes import ConnectorOauthScopes
    from apideck.model.connector_setting import ConnectorSetting
    from apideck.model.connector_status import ConnectorStatus
    from apideck.model.connector_tls_support import ConnectorTlsSupport
    from apideck.model.connector_unified_apis import ConnectorUnifiedApis
    from apideck.model.linked_connector_resource import LinkedConnectorResource
    from apideck.model.schema_support import SchemaSupport
    from apideck.model.webhook_support import WebhookSupport
    globals()['ConnectorDoc'] = ConnectorDoc
    globals()['ConnectorEvent'] = ConnectorEvent
    globals()['ConnectorOauthScopes'] = ConnectorOauthScopes
    globals()['ConnectorSetting'] = ConnectorSetting
    globals()['ConnectorStatus'] = ConnectorStatus
    globals()['ConnectorTlsSupport'] = ConnectorTlsSupport
    globals()['ConnectorUnifiedApis'] = ConnectorUnifiedApis
    globals()['LinkedConnectorResource'] = LinkedConnectorResource
    globals()['SchemaSupport'] = SchemaSupport
    globals()['WebhookSupport'] = WebhookSupport


class Connector(ModelNormal):
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
        ('auth_type',): {
            'OAUTH2': "oauth2",
            'APIKEY': "apiKey",
            'BASIC': "basic",
            'CUSTOM': "custom",
            'NONE': "none",
        },
        ('oauth_grant_type',): {
            'AUTHORIZATION_CODE': "authorization_code",
            'CLIENT_CREDENTIALS': "client_credentials",
            'PASSWORD': "password",
        },
        ('oauth_credentials_source',): {
            'INTEGRATION': "integration",
            'CONNECTION': "connection",
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
            'name': (str,),  # noqa: E501
            'status': (ConnectorStatus,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'icon_url': (str,),  # noqa: E501
            'logo_url': (str,),  # noqa: E501
            'website_url': (str,),  # noqa: E501
            'signup_url': (str,),  # noqa: E501
            'partner_signup_url': (str,),  # noqa: E501
            'free_trial_available': (bool,),  # noqa: E501
            'auth_type': (str,),  # noqa: E501
            'auth_only': (bool,),  # noqa: E501
            'blind_mapped': (bool,),  # noqa: E501
            'oauth_grant_type': (str,),  # noqa: E501
            'oauth_credentials_source': (str,),  # noqa: E501
            'oauth_scopes': ([ConnectorOauthScopes],),  # noqa: E501
            'custom_scopes': (bool,),  # noqa: E501
            'has_sandbox_credentials': (bool,),  # noqa: E501
            'settings': ([ConnectorSetting],),  # noqa: E501
            'service_id': (str,),  # noqa: E501
            'unified_apis': ([ConnectorUnifiedApis],),  # noqa: E501
            'supported_resources': ([LinkedConnectorResource],),  # noqa: E501
            'configurable_resources': ([str],),  # noqa: E501
            'supported_events': ([ConnectorEvent],),  # noqa: E501
            'webhook_support': (WebhookSupport,),  # noqa: E501
            'schema_support': (SchemaSupport,),  # noqa: E501
            'docs': ([ConnectorDoc],),  # noqa: E501
            'tls_support': (ConnectorTlsSupport,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'status': 'status',  # noqa: E501
        'description': 'description',  # noqa: E501
        'icon_url': 'icon_url',  # noqa: E501
        'logo_url': 'logo_url',  # noqa: E501
        'website_url': 'website_url',  # noqa: E501
        'signup_url': 'signup_url',  # noqa: E501
        'partner_signup_url': 'partner_signup_url',  # noqa: E501
        'free_trial_available': 'free_trial_available',  # noqa: E501
        'auth_type': 'auth_type',  # noqa: E501
        'auth_only': 'auth_only',  # noqa: E501
        'blind_mapped': 'blind_mapped',  # noqa: E501
        'oauth_grant_type': 'oauth_grant_type',  # noqa: E501
        'oauth_credentials_source': 'oauth_credentials_source',  # noqa: E501
        'oauth_scopes': 'oauth_scopes',  # noqa: E501
        'custom_scopes': 'custom_scopes',  # noqa: E501
        'has_sandbox_credentials': 'has_sandbox_credentials',  # noqa: E501
        'settings': 'settings',  # noqa: E501
        'service_id': 'service_id',  # noqa: E501
        'unified_apis': 'unified_apis',  # noqa: E501
        'supported_resources': 'supported_resources',  # noqa: E501
        'configurable_resources': 'configurable_resources',  # noqa: E501
        'supported_events': 'supported_events',  # noqa: E501
        'webhook_support': 'webhook_support',  # noqa: E501
        'schema_support': 'schema_support',  # noqa: E501
        'docs': 'docs',  # noqa: E501
        'tls_support': 'tls_support',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'auth_type',  # noqa: E501
        'auth_only',  # noqa: E501
        'blind_mapped',  # noqa: E501
        'oauth_grant_type',  # noqa: E501
        'oauth_credentials_source',  # noqa: E501
        'custom_scopes',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Connector - a model defined in OpenAPI

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
            id (str): ID of the connector.. [optional]  # noqa: E501
            name (str): Name of the connector.. [optional]  # noqa: E501
            status (ConnectorStatus): [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            icon_url (str): Link to a small square icon for the connector.. [optional]  # noqa: E501
            logo_url (str): Link to the full logo for the connector.. [optional]  # noqa: E501
            website_url (str): Link to the connector's website.. [optional]  # noqa: E501
            signup_url (str): Link to the connector's signup page.. [optional]  # noqa: E501
            partner_signup_url (str): Link to the connector's partner program signup page.. [optional]  # noqa: E501
            free_trial_available (bool): Set to `true` when the connector offers a free trial. Use `signup_url` to sign up for a free trial. [optional]  # noqa: E501
            auth_type (str): Type of authorization used by the connector. [optional]  # noqa: E501
            auth_only (bool): Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API. [optional]  # noqa: E501
            blind_mapped (bool): Set to `true` when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality.. [optional]  # noqa: E501
            oauth_grant_type (str): OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types. [optional]  # noqa: E501
            oauth_credentials_source (str): Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.. [optional]  # noqa: E501
            oauth_scopes ([ConnectorOauthScopes]): List of OAuth Scopes available for this connector.. [optional]  # noqa: E501
            custom_scopes (bool): Set to `true` when connector allows the definition of custom scopes.. [optional]  # noqa: E501
            has_sandbox_credentials (bool): Indicates whether Apideck Sandbox OAuth credentials are available.. [optional]  # noqa: E501
            settings ([ConnectorSetting]): [optional]  # noqa: E501
            service_id (str): Service provider identifier. [optional]  # noqa: E501
            unified_apis ([ConnectorUnifiedApis]): List of Unified APIs that feature this connector.. [optional]  # noqa: E501
            supported_resources ([LinkedConnectorResource]): List of resources that are supported on the connector.. [optional]  # noqa: E501
            configurable_resources ([str]): List of resources that have settings that can be configured.. [optional]  # noqa: E501
            supported_events ([ConnectorEvent]): List of events that are supported on the connector across all Unified APIs.. [optional]  # noqa: E501
            webhook_support (WebhookSupport): [optional]  # noqa: E501
            schema_support (SchemaSupport): [optional]  # noqa: E501
            docs ([ConnectorDoc]): [optional]  # noqa: E501
            tls_support (ConnectorTlsSupport): [optional]  # noqa: E501
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
        """Connector - a model defined in OpenAPI

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
            id (str): ID of the connector.. [optional]  # noqa: E501
            name (str): Name of the connector.. [optional]  # noqa: E501
            status (ConnectorStatus): [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            icon_url (str): Link to a small square icon for the connector.. [optional]  # noqa: E501
            logo_url (str): Link to the full logo for the connector.. [optional]  # noqa: E501
            website_url (str): Link to the connector's website.. [optional]  # noqa: E501
            signup_url (str): Link to the connector's signup page.. [optional]  # noqa: E501
            partner_signup_url (str): Link to the connector's partner program signup page.. [optional]  # noqa: E501
            free_trial_available (bool): Set to `true` when the connector offers a free trial. Use `signup_url` to sign up for a free trial. [optional]  # noqa: E501
            auth_type (str): Type of authorization used by the connector. [optional]  # noqa: E501
            auth_only (bool): Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API. [optional]  # noqa: E501
            blind_mapped (bool): Set to `true` when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality.. [optional]  # noqa: E501
            oauth_grant_type (str): OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types. [optional]  # noqa: E501
            oauth_credentials_source (str): Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.. [optional]  # noqa: E501
            oauth_scopes ([ConnectorOauthScopes]): List of OAuth Scopes available for this connector.. [optional]  # noqa: E501
            custom_scopes (bool): Set to `true` when connector allows the definition of custom scopes.. [optional]  # noqa: E501
            has_sandbox_credentials (bool): Indicates whether Apideck Sandbox OAuth credentials are available.. [optional]  # noqa: E501
            settings ([ConnectorSetting]): [optional]  # noqa: E501
            service_id (str): Service provider identifier. [optional]  # noqa: E501
            unified_apis ([ConnectorUnifiedApis]): List of Unified APIs that feature this connector.. [optional]  # noqa: E501
            supported_resources ([LinkedConnectorResource]): List of resources that are supported on the connector.. [optional]  # noqa: E501
            configurable_resources ([str]): List of resources that have settings that can be configured.. [optional]  # noqa: E501
            supported_events ([ConnectorEvent]): List of events that are supported on the connector across all Unified APIs.. [optional]  # noqa: E501
            webhook_support (WebhookSupport): [optional]  # noqa: E501
            schema_support (SchemaSupport): [optional]  # noqa: E501
            docs ([ConnectorDoc]): [optional]  # noqa: E501
            tls_support (ConnectorTlsSupport): [optional]  # noqa: E501
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
