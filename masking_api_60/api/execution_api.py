# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from masking_api_60.api_client import ApiClient


class ExecutionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_execution(self, execution_id, **kwargs):  # noqa: E501
        """Cancel execution by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_execution(execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: The ID of the execution to cancel (required)
        :param str expected_status: The expected status of the execution to cancel to prevent cancelling a queued job that has transitioned to a running state since the request was issued.
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_execution_with_http_info(execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_execution_with_http_info(execution_id, **kwargs)  # noqa: E501
            return data

    def cancel_execution_with_http_info(self, execution_id, **kwargs):  # noqa: E501
        """Cancel execution by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_execution_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: The ID of the execution to cancel (required)
        :param str expected_status: The expected status of the execution to cancel to prevent cancelling a queued job that has transitioned to a running state since the request was issued.
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['execution_id', 'expected_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'execution_id' is set
        if ('execution_id' not in params or
                params['execution_id'] is None):
            raise ValueError("Missing the required parameter `execution_id` when calling `cancel_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execution_id' in params:
            path_params['executionId'] = params['execution_id']  # noqa: E501

        query_params = []
        if 'expected_status' in params:
            query_params.append(('expectedStatus', params['expected_status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/executions/{executionId}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Execution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_execution(self, body, **kwargs):  # noqa: E501
        """Create execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_execution(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Execution body: The execution to create (required)
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_execution_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_execution_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_execution_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_execution_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Execution body: The execution to create (required)
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/executions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Execution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_executions(self, **kwargs):  # noqa: E501
        """Get all executions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_executions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int job_id: The ID of the job to get all executions for
        :param int page_number: The page number for which to get executions. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: ExecutionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_executions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_executions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_executions_with_http_info(self, **kwargs):  # noqa: E501
        """Get all executions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_executions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int job_id: The ID of the job to get all executions for
        :param int page_number: The page number for which to get executions. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: ExecutionList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_executions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('job_id', params['job_id']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/executions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExecutionList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_execution_by_id(self, execution_id, **kwargs):  # noqa: E501
        """Get execution by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_by_id(execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: The ID of the execution to get (required)
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_execution_by_id_with_http_info(execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_execution_by_id_with_http_info(execution_id, **kwargs)  # noqa: E501
            return data

    def get_execution_by_id_with_http_info(self, execution_id, **kwargs):  # noqa: E501
        """Get execution by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_by_id_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: The ID of the execution to get (required)
        :return: Execution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_execution_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'execution_id' is set
        if ('execution_id' not in params or
                params['execution_id'] is None):
            raise ValueError("Missing the required parameter `execution_id` when calling `get_execution_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'execution_id' in params:
            path_params['executionId'] = params['execution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/executions/{executionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Execution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
