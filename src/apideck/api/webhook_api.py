"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.6.2
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
from apideck.model.create_webhook_request import CreateWebhookRequest
from apideck.model.create_webhook_response import CreateWebhookResponse
from apideck.model.delete_webhook_response import DeleteWebhookResponse
from apideck.model.get_webhook_event_logs_response import GetWebhookEventLogsResponse
from apideck.model.get_webhook_response import GetWebhookResponse
from apideck.model.get_webhooks_response import GetWebhooksResponse
from apideck.model.not_found_response import NotFoundResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.update_webhook_request import UpdateWebhookRequest
from apideck.model.update_webhook_response import UpdateWebhookResponse
from apideck.model.webhook_event_logs_filter import WebhookEventLogsFilter


class WebhookApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.event_logs_all_endpoint = _Endpoint(
            settings={
                'response_type': (GetWebhookEventLogsResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/webhook/logs',
                'operation_id': 'event_logs_all',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_id',
                    'cursor',
                    'limit',
                    'filter',
                ],
                'required': [],
                'nullable': [
                    'cursor',
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
                    'app_id':
                        (str,),
                    'cursor':
                        (str, none_type,),
                    'limit':
                        (int,),
                    'filter':
                        (WebhookEventLogsFilter,),
                },
                'attribute_map': {
                    'app_id': 'x-apideck-app-id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'filter': 'filter',
                },
                'location_map': {
                    'app_id': 'header',
                    'cursor': 'query',
                    'limit': 'query',
                    'filter': 'query',
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
        self.webhooks_add_endpoint = _Endpoint(
            settings={
                'response_type': (CreateWebhookResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/webhook/webhooks',
                'operation_id': 'webhooks_add',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_webhook_request',
                    'app_id',
                ],
                'required': [
                    'create_webhook_request',
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
                    'create_webhook_request':
                        (CreateWebhookRequest,),
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'app_id': 'x-apideck-app-id',
                },
                'location_map': {
                    'create_webhook_request': 'body',
                    'app_id': 'header',
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
        self.webhooks_all_endpoint = _Endpoint(
            settings={
                'response_type': (GetWebhooksResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/webhook/webhooks',
                'operation_id': 'webhooks_all',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_id',
                    'cursor',
                    'limit',
                ],
                'required': [],
                'nullable': [
                    'cursor',
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
                    'app_id':
                        (str,),
                    'cursor':
                        (str, none_type,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'app_id': 'x-apideck-app-id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                },
                'location_map': {
                    'app_id': 'header',
                    'cursor': 'query',
                    'limit': 'query',
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
        self.webhooks_delete_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteWebhookResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/webhook/webhooks/{id}',
                'operation_id': 'webhooks_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'app_id',
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
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'app_id': 'x-apideck-app-id',
                },
                'location_map': {
                    'id': 'path',
                    'app_id': 'header',
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
        self.webhooks_one_endpoint = _Endpoint(
            settings={
                'response_type': (GetWebhookResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/webhook/webhooks/{id}',
                'operation_id': 'webhooks_one',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'app_id',
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
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'app_id': 'x-apideck-app-id',
                },
                'location_map': {
                    'id': 'path',
                    'app_id': 'header',
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
        self.webhooks_update_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateWebhookResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/webhook/webhooks/{id}',
                'operation_id': 'webhooks_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'update_webhook_request',
                    'app_id',
                ],
                'required': [
                    'id',
                    'update_webhook_request',
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
                    'update_webhook_request':
                        (UpdateWebhookRequest,),
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'app_id': 'x-apideck-app-id',
                },
                'location_map': {
                    'id': 'path',
                    'update_webhook_request': 'body',
                    'app_id': 'header',
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

    def event_logs_all(
        self,
        **kwargs
    ):
        """List event logs  # noqa: E501

        List event logs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.event_logs_all(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            app_id (str): The ID of your Unify application. [optional]
            cursor (str, none_type): Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.. [optional]
            limit (int): Number of results to return. Minimum 1, Maximum 200, Default 20. [optional] if omitted the server will use the default value of 20
            filter (WebhookEventLogsFilter): Filter results. [optional]
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
            GetWebhookEventLogsResponse
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
        return self.event_logs_all_endpoint.call_with_http_info(**kwargs)

    def webhooks_add(
        self,
        create_webhook_request,
        **kwargs
    ):
        """Create webhook subscription  # noqa: E501

        Create a webhook subscription to receive events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhooks_add(create_webhook_request, async_req=True)
        >>> result = thread.get()

        Args:
            create_webhook_request (CreateWebhookRequest):

        Keyword Args:
            app_id (str): The ID of your Unify application. [optional]
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
            CreateWebhookResponse
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
        kwargs['create_webhook_request'] = \
            create_webhook_request
        return self.webhooks_add_endpoint.call_with_http_info(**kwargs)

    def webhooks_all(
        self,
        **kwargs
    ):
        """List webhook subscriptions  # noqa: E501

        List all webhook subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhooks_all(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            app_id (str): The ID of your Unify application. [optional]
            cursor (str, none_type): Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.. [optional]
            limit (int): Number of results to return. Minimum 1, Maximum 200, Default 20. [optional] if omitted the server will use the default value of 20
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
            GetWebhooksResponse
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
        return self.webhooks_all_endpoint.call_with_http_info(**kwargs)

    def webhooks_delete(
        self,
        id,
        **kwargs
    ):
        """Delete webhook subscription  # noqa: E501

        Delete a webhook subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhooks_delete(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        Keyword Args:
            app_id (str): The ID of your Unify application. [optional]
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
            DeleteWebhookResponse
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
        return self.webhooks_delete_endpoint.call_with_http_info(**kwargs)

    def webhooks_one(
        self,
        id,
        **kwargs
    ):
        """Get webhook subscription  # noqa: E501

        Get the webhook subscription details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhooks_one(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        Keyword Args:
            app_id (str): The ID of your Unify application. [optional]
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
            GetWebhookResponse
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
        return self.webhooks_one_endpoint.call_with_http_info(**kwargs)

    def webhooks_update(
        self,
        id,
        update_webhook_request,
        **kwargs
    ):
        """Update webhook subscription  # noqa: E501

        Update a webhook subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhooks_update(id, update_webhook_request, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
            update_webhook_request (UpdateWebhookRequest):

        Keyword Args:
            app_id (str): The ID of your Unify application. [optional]
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
            UpdateWebhookResponse
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
        kwargs['update_webhook_request'] = \
            update_webhook_request
        return self.webhooks_update_endpoint.call_with_http_info(**kwargs)

