"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 8.85.1
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
from apideck.model.create_lead_response import CreateLeadResponse
from apideck.model.delete_lead_response import DeleteLeadResponse
from apideck.model.get_lead_response import GetLeadResponse
from apideck.model.get_leads_response import GetLeadsResponse
from apideck.model.lead import Lead
from apideck.model.leads_filter import LeadsFilter
from apideck.model.leads_sort import LeadsSort
from apideck.model.not_found_response import NotFoundResponse
from apideck.model.payment_required_response import PaymentRequiredResponse
from apideck.model.unauthorized_response import UnauthorizedResponse
from apideck.model.unexpected_error_response import UnexpectedErrorResponse
from apideck.model.unprocessable_response import UnprocessableResponse
from apideck.model.update_lead_response import UpdateLeadResponse


class LeadApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.leads_add_endpoint = _Endpoint(
            settings={
                'response_type': (CreateLeadResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/lead/leads',
                'operation_id': 'leads_add',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead',
                    'raw',
                    'consumer_id',
                    'app_id',
                    'service_id',
                ],
                'required': [
                    'lead',
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
                    'lead':
                        (Lead,),
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
                    'lead': 'body',
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
        self.leads_all_endpoint = _Endpoint(
            settings={
                'response_type': (GetLeadsResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/lead/leads',
                'operation_id': 'leads_all',
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
                    'filter',
                    'sort',
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
                    'filter':
                        (LeadsFilter,),
                    'sort':
                        (LeadsSort,),
                },
                'attribute_map': {
                    'raw': 'raw',
                    'consumer_id': 'x-apideck-consumer-id',
                    'app_id': 'x-apideck-app-id',
                    'service_id': 'x-apideck-service-id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'filter': 'filter',
                    'sort': 'sort',
                },
                'location_map': {
                    'raw': 'query',
                    'consumer_id': 'header',
                    'app_id': 'header',
                    'service_id': 'header',
                    'cursor': 'query',
                    'limit': 'query',
                    'filter': 'query',
                    'sort': 'query',
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
        self.leads_delete_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteLeadResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/lead/leads/{id}',
                'operation_id': 'leads_delete',
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
        self.leads_one_endpoint = _Endpoint(
            settings={
                'response_type': (GetLeadResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/lead/leads/{id}',
                'operation_id': 'leads_one',
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
        self.leads_update_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateLeadResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/lead/leads/{id}',
                'operation_id': 'leads_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'lead',
                    'consumer_id',
                    'app_id',
                    'service_id',
                    'raw',
                ],
                'required': [
                    'id',
                    'lead',
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
                    'lead':
                        (Lead,),
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
                    'lead': 'body',
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

    def leads_add(
        self,
        lead,
        **kwargs
    ):
        """Create lead  # noqa: E501

        Create lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_add(lead, async_req=True)
        >>> result = thread.get()

        Args:
            lead (Lead):

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
            CreateLeadResponse
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
        kwargs['lead'] = \
            lead
        return self.leads_add_endpoint.call_with_http_info(**kwargs)

    def leads_all(
        self,
        **kwargs
    ):
        """List leads  # noqa: E501

        List leads  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_all(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            raw (bool): Include raw response. Mostly used for debugging purposes. [optional] if omitted the server will use the default value of False
            consumer_id (str): ID of the consumer which you want to get or push data from. [optional]
            app_id (str): The ID of your Unify application. [optional]
            service_id (str): Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.. [optional]
            cursor (str, none_type): Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.. [optional]
            limit (int): Number of records to return. [optional] if omitted the server will use the default value of 20
            filter (LeadsFilter): Apply filters. [optional]
            sort (LeadsSort): Apply sorting. [optional]
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
            GetLeadsResponse
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
        return self.leads_all_endpoint.call_with_http_info(**kwargs)

    def leads_delete(
        self,
        id,
        **kwargs
    ):
        """Delete lead  # noqa: E501

        Delete lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_delete(id, async_req=True)
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
            DeleteLeadResponse
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
        return self.leads_delete_endpoint.call_with_http_info(**kwargs)

    def leads_one(
        self,
        id,
        **kwargs
    ):
        """Get lead  # noqa: E501

        Get lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_one(id, async_req=True)
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
            GetLeadResponse
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
        return self.leads_one_endpoint.call_with_http_info(**kwargs)

    def leads_update(
        self,
        id,
        lead,
        **kwargs
    ):
        """Update lead  # noqa: E501

        Update lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_update(id, lead, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): ID of the record you are acting upon.
            lead (Lead):

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
            UpdateLeadResponse
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
        kwargs['lead'] = \
            lead
        return self.leads_update_endpoint.call_with_http_info(**kwargs)

