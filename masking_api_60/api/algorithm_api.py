# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from masking_api_60.api_client import ApiClient


class AlgorithmApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_algorithm(self, body, **kwargs):  # noqa: E501
        """Create algorithm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_algorithm(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Algorithm body: The algorithm to create (required)
        :return: AsyncTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_algorithm_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_algorithm_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_algorithm_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create algorithm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_algorithm_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Algorithm body: The algorithm to create (required)
        :return: AsyncTask
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
                    " to method create_algorithm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_algorithm`")  # noqa: E501

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
            '/algorithms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_algorithm(self, algorithm_name, **kwargs):  # noqa: E501
        """Delete algorithm by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_algorithm(algorithm_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_algorithm_with_http_info(algorithm_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_algorithm_with_http_info(algorithm_name, **kwargs)  # noqa: E501
            return data

    def delete_algorithm_with_http_info(self, algorithm_name, **kwargs):  # noqa: E501
        """Delete algorithm by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_algorithm_with_http_info(algorithm_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['algorithm_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_algorithm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'algorithm_name' is set
        if ('algorithm_name' not in params or
                params['algorithm_name'] is None):
            raise ValueError("Missing the required parameter `algorithm_name` when calling `delete_algorithm`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'algorithm_name' in params:
            path_params['algorithmName'] = params['algorithm_name']  # noqa: E501

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
            '/algorithms/{algorithmName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_algorithm(self, algorithm_name, **kwargs):  # noqa: E501
        """Get algorithm by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_algorithm(algorithm_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm to get (required)
        :return: Algorithm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_algorithm_with_http_info(algorithm_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_algorithm_with_http_info(algorithm_name, **kwargs)  # noqa: E501
            return data

    def get_algorithm_with_http_info(self, algorithm_name, **kwargs):  # noqa: E501
        """Get algorithm by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_algorithm_with_http_info(algorithm_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm to get (required)
        :return: Algorithm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['algorithm_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_algorithm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'algorithm_name' is set
        if ('algorithm_name' not in params or
                params['algorithm_name'] is None):
            raise ValueError("Missing the required parameter `algorithm_name` when calling `get_algorithm`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'algorithm_name' in params:
            path_params['algorithmName'] = params['algorithm_name']  # noqa: E501

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
            '/algorithms/{algorithmName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Algorithm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_algorithms(self, **kwargs):  # noqa: E501
        """Get all algorithms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_algorithms(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get algorithms. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: AlgorithmList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_algorithms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_algorithms_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_algorithms_with_http_info(self, **kwargs):  # noqa: E501
        """Get all algorithms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_algorithms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get algorithms. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: AlgorithmList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_algorithms" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/algorithms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlgorithmList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def randomize_algorithm_key(self, algorithm_name, **kwargs):  # noqa: E501
        """Randomize algorithm key by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.randomize_algorithm_key(algorithm_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm who's key should be randomized (required)
        :return: Algorithm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.randomize_algorithm_key_with_http_info(algorithm_name, **kwargs)  # noqa: E501
        else:
            (data) = self.randomize_algorithm_key_with_http_info(algorithm_name, **kwargs)  # noqa: E501
            return data

    def randomize_algorithm_key_with_http_info(self, algorithm_name, **kwargs):  # noqa: E501
        """Randomize algorithm key by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.randomize_algorithm_key_with_http_info(algorithm_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm who's key should be randomized (required)
        :return: Algorithm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['algorithm_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method randomize_algorithm_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'algorithm_name' is set
        if ('algorithm_name' not in params or
                params['algorithm_name'] is None):
            raise ValueError("Missing the required parameter `algorithm_name` when calling `randomize_algorithm_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'algorithm_name' in params:
            path_params['algorithmName'] = params['algorithm_name']  # noqa: E501

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
            '/algorithms/{algorithmName}/randomize-key', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Algorithm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_algorithm(self, algorithm_name, body, **kwargs):  # noqa: E501
        """Update algorithm by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_algorithm(algorithm_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm to update (required)
        :param Algorithm body: The updated algorithm (required)
        :return: AsyncTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_algorithm_with_http_info(algorithm_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_algorithm_with_http_info(algorithm_name, body, **kwargs)  # noqa: E501
            return data

    def update_algorithm_with_http_info(self, algorithm_name, body, **kwargs):  # noqa: E501
        """Update algorithm by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_algorithm_with_http_info(algorithm_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str algorithm_name: The name of the algorithm to update (required)
        :param Algorithm body: The updated algorithm (required)
        :return: AsyncTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['algorithm_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_algorithm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'algorithm_name' is set
        if ('algorithm_name' not in params or
                params['algorithm_name'] is None):
            raise ValueError("Missing the required parameter `algorithm_name` when calling `update_algorithm`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_algorithm`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'algorithm_name' in params:
            path_params['algorithmName'] = params['algorithm_name']  # noqa: E501

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
            '/algorithms/{algorithmName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
