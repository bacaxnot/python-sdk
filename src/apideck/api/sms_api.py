"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.3.6
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from apideck.api_client import ApiClient, Endpoint as _Endpoint
from apideck.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from apideck.model.bad_request_response import BadRequestResponse
from apideck.model.create_message_response import CreateMessageResponse
from apideck.model.delete_message_response import DeleteMessageResponse
from apideck.model.get_message_response import GetMessageResponse
from apideck.model.get_messages_response import GetMessagesResponse
from apideck.model.message import Message
from apideck.model.not_found_response import NotFoundResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.update_message_response import UpdateMessageResponse


class SmsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.messages_add_endpoint = _Endpoint(
            settings={
                'response_type': (CreateMessageResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/sms/messages',
                'operation_id': 'messages_add',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'message',
                    'raw',
                    'consumer_id',
                    'app_id',
                    'service_id',
                ],
                'required': [
                    'message',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'message':
                        (Message,),
                    'raw':
                        (bool,),
                    'consumer_id':
                        (str,),
                    'app_id':
                        (str,),
                    'service_id':
                        (str,),
                },
                'attribute_map': {
                    'raw': 'raw',
                    'consumer_id': 'x-apideck-consumer-id',
                    'app_id': 'x-apideck-app-id',
                    'service_id': 'x-apideck-service-id',
                },
                'location_map': {
                    'message': 'body',
                    'raw': 'query',
                    'consumer_id': 'header',
                    'app_id': 'header',
                    'service_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.messages_all_endpoint = _Endpoint(
            settings={
                'response_type': (GetMessagesResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/sms/messages',
                'operation_id': 'messages_all',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'raw',
                    'consumer_id',
                    'app_id',
                    'service_id',
                    'cursor',
                    'limit',
                    'fields',
                ],
                'required': [],
                'nullable': [
                    'cursor',
                    'fields',
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 200,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'raw':
                        (bool,),
                    'consumer_id':
                        (str,),
                    'app_id':
                        (str,),
                    'service_id':
                        (str,),
                    'cursor':
                        (str, none_type,),
                    'limit':
                        (int,),
                    'fields':
                        (str, none_type,),
                },
                'attribute_map': {
                    'raw': 'raw',
                    'consumer_id': 'x-apideck-consumer-id',
                    'app_id': 'x-apideck-app-id',
                    'service_id': 'x-apideck-service-id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'fields': 'fields',
                },
                'location_map': {
                    'raw': 'query',
                    'consumer_id': 'header',
                    'app_id': 'header',
                    'service_id': 'header',
                    'cursor': 'query',
                    'limit': 'query',
                    'fields': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.messages_delete_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteMessageResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/sms/messages/{id}',
                'operation_id': 'messages_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'consumer_id',
                    'app_id',
                    'service_id',
                    'raw',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'consumer_id':
                        (str,),
                    'app_id':
                        (str,),
                    'service_id':
                        (str,),
                    'raw':
                        (bool,),
                },
                'attribute_map': {
                    'id': 'id',
                    'consumer_id': 'x-apideck-consumer-id',
                    'app_id': 'x-apideck-app-id',
                    'service_id': 'x-apideck-service-id',
                    'raw': 'raw',
                },
                'location_map': {
                    'id': 'path',
                    'consumer_id': 'header',
                    'app_id': 'header',
                    'service_id': 'header',
                    'raw': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.messages_one_endpoint = _Endpoint(
            settings={
                'response_type': (GetMessageResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/sms/messages/{id}',
                'operation_id': 'messages_one',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'consumer_id',
                    'app_id',
                    'service_id',
                    'raw',
                    'fields',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                    'fields',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'consumer_id':
                        (str,),
                    'app_id':
                        (str,),
                    'service_id':
                        (str,),
                    'raw':
                        (bool,),
                    'fields':
                        (str, none_type,),
                },
                'attribute_map': {
                    'id': 'id',
                    'consumer_id': 'x-apideck-consumer-id',
                    'app_id': 'x-apideck-app-id',
                    'service_id': 'x-apideck-service-id',
                    'raw': 'raw',
                    'fields': 'fields',
                },
                'location_map': {
                    'id': 'path',
                    'consumer_id': 'header',
                    'app_id': 'header',
                    'service_id': 'header',
                    'raw': 'query',
                    'fields': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.messages_update_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateMessageResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/sms/messages/{id}',
                'operation_id': 'messages_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'message',
                    'consumer_id',
                    'app_id',
                    'service_id',
                    'raw',
                ],
                'required': [
                    'id',
                    'message',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'message':
                        (Message,),
                    'consumer_id':
                        (str,),
                    'app_id':
                        (str,),
                    'service_id':
                        (str,),
                    'raw':
                        (bool,),
                },
                'attribute_map': {
                    'id': 'id',
                    'consumer_id': 'x-apideck-consumer-id',
                    'app_id': 'x-apideck-app-id',
                    'service_id': 'x-apideck-service-id',
                    'raw': 'raw',
                },
                'location_map': {
                    'id': 'path',
                    'message': 'body',
                    'consumer_id': 'header',
                    'app_id': 'header',
                    'service_id': 'header',
                    'raw': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def messages_add(
        self,
        message,
        **kwargs
    ):
        """Create Message  # noqa: E501

        Create Message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messages_add(message, async_req=True)
        >>> result = thread.get()

        Args:
            message (Message):

        Keyword Args:
            raw (bool): Include raw response. Mostly used for debugging purposes. [optional] if omitted the server will use the default value of False
            consumer_id (str): ID of the consumer which you want to get or push data from. [optional]
            app_id (str): The ID of your Unify application. [optional]
            service_id (str): Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateMessageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['message'] = \
            message
        return self.messages_add_endpoint.call_with_http_info(**kwargs)

    def messages_all(
        self,
        **kwargs
    ):
        """List Messages  # noqa: E501

        List Messages  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messages_all(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            raw (bool): Include raw response. Mostly used for debugging purposes. [optional] if omitted the server will use the default value of False
            consumer_id (str): ID of the consumer which you want to get or push data from. [optional]
            app_id (str): The ID of your Unify application. [optional]
            service_id (str): Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.. [optional]
            cursor (str, none_type): Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.. [optional]
            limit (int): Number of results to return. Minimum 1, Maximum 200, Default 20. [optional] if omitted the server will use the default value of 20
            fields (str, none_type): The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetMessagesResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.messages_all_endpoint.call_with_http_info(**kwargs)

    def messages_delete(
        self,
        id,
        **kwargs
    ):
        """Delete Message  # noqa: E501

        Delete Message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messages_delete(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): ID of the record you are acting upon.

        Keyword Args:
            consumer_id (str): ID of the consumer which you want to get or push data from. [optional]
            app_id (str): The ID of your Unify application. [optional]
            service_id (str): Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.. [optional]
            raw (bool): Include raw response. Mostly used for debugging purposes. [optional] if omitted the server will use the default value of False
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DeleteMessageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.messages_delete_endpoint.call_with_http_info(**kwargs)

    def messages_one(
        self,
        id,
        **kwargs
    ):
        """Get Message  # noqa: E501

        Get Message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messages_one(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): ID of the record you are acting upon.

        Keyword Args:
            consumer_id (str): ID of the consumer which you want to get or push data from. [optional]
            app_id (str): The ID of your Unify application. [optional]
            service_id (str): Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.. [optional]
            raw (bool): Include raw response. Mostly used for debugging purposes. [optional] if omitted the server will use the default value of False
            fields (str, none_type): The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetMessageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.messages_one_endpoint.call_with_http_info(**kwargs)

    def messages_update(
        self,
        id,
        message,
        **kwargs
    ):
        """Update Message  # noqa: E501

        Update Message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messages_update(id, message, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): ID of the record you are acting upon.
            message (Message):

        Keyword Args:
            consumer_id (str): ID of the consumer which you want to get or push data from. [optional]
            app_id (str): The ID of your Unify application. [optional]
            service_id (str): Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.. [optional]
            raw (bool): Include raw response. Mostly used for debugging purposes. [optional] if omitted the server will use the default value of False
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UpdateMessageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        kwargs['message'] = \
            message
        return self.messages_update_endpoint.call_with_http_info(**kwargs)

