# coding: utf-8

"""
    DRES API

    API for DRES (Distributed Retrieval Evaluation Server), Version 1.0

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from typing import Optional

from openapi_client.models.query_event_log import QueryEventLog
from openapi_client.models.query_result_log import QueryResultLog
from openapi_client.models.success_status import SuccessStatus

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LogApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def post_api_v1_log_query(self, session : Annotated[StrictStr, Field(..., description="Session Token")], query_event_log : Optional[QueryEventLog] = None, **kwargs) -> SuccessStatus:  # noqa: E501
        """Accepts query logs from participants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_api_v1_log_query(session, query_event_log, async_req=True)
        >>> result = thread.get()

        :param session: Session Token (required)
        :type session: str
        :param query_event_log:
        :type query_event_log: QueryEventLog
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SuccessStatus
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the post_api_v1_log_query_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.post_api_v1_log_query_with_http_info(session, query_event_log, **kwargs)  # noqa: E501

    @validate_arguments
    def post_api_v1_log_query_with_http_info(self, session : Annotated[StrictStr, Field(..., description="Session Token")], query_event_log : Optional[QueryEventLog] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Accepts query logs from participants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_api_v1_log_query_with_http_info(session, query_event_log, async_req=True)
        >>> result = thread.get()

        :param session: Session Token (required)
        :type session: str
        :param query_event_log:
        :type query_event_log: QueryEventLog
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SuccessStatus, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'session',
            'query_event_log'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_api_v1_log_query" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('session') is not None:  # noqa: E501
            _query_params.append(('session', _params['session']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['query_event_log'] is not None:
            _body_params = _params['query_event_log']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "SuccessStatus",
            '400': "ErrorStatus",
            '401': "ErrorStatus",
        }

        return self.api_client.call_api(
            '/api/v1/log/query', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def post_api_v1_log_result(self, session : Annotated[StrictStr, Field(..., description="Session Token")], query_result_log : Optional[QueryResultLog] = None, **kwargs) -> SuccessStatus:  # noqa: E501
        """Accepts result logs from participants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_api_v1_log_result(session, query_result_log, async_req=True)
        >>> result = thread.get()

        :param session: Session Token (required)
        :type session: str
        :param query_result_log:
        :type query_result_log: QueryResultLog
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SuccessStatus
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the post_api_v1_log_result_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.post_api_v1_log_result_with_http_info(session, query_result_log, **kwargs)  # noqa: E501

    @validate_arguments
    def post_api_v1_log_result_with_http_info(self, session : Annotated[StrictStr, Field(..., description="Session Token")], query_result_log : Optional[QueryResultLog] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Accepts result logs from participants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_api_v1_log_result_with_http_info(session, query_result_log, async_req=True)
        >>> result = thread.get()

        :param session: Session Token (required)
        :type session: str
        :param query_result_log:
        :type query_result_log: QueryResultLog
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SuccessStatus, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'session',
            'query_result_log'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_api_v1_log_result" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('session') is not None:  # noqa: E501
            _query_params.append(('session', _params['session']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['query_result_log'] is not None:
            _body_params = _params['query_result_log']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "SuccessStatus",
            '400': "ErrorStatus",
            '401': "ErrorStatus",
        }

        return self.api_client.call_api(
            '/api/v1/log/result', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
