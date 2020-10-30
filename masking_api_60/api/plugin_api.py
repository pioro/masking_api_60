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


class PluginApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_plugin(self, file_reference_id, **kwargs):  # noqa: E501
        """Install plugin  # noqa: E501

        Install an uploaded plugin file onto the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_plugin(file_reference_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_reference_id: The file references ID of the uploaded plugin JAR file to install (required)
        :param str plugin_name: Override the default name of the plugin. Plugin names must be unique across all plugins on the engine.
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_plugin_with_http_info(file_reference_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_plugin_with_http_info(file_reference_id, **kwargs)  # noqa: E501
            return data

    def create_plugin_with_http_info(self, file_reference_id, **kwargs):  # noqa: E501
        """Install plugin  # noqa: E501

        Install an uploaded plugin file onto the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_plugin_with_http_info(file_reference_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_reference_id: The file references ID of the uploaded plugin JAR file to install (required)
        :param str plugin_name: Override the default name of the plugin. Plugin names must be unique across all plugins on the engine.
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_reference_id', 'plugin_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_plugin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_reference_id' is set
        if ('file_reference_id' not in params or
                params['file_reference_id'] is None):
            raise ValueError("Missing the required parameter `file_reference_id` when calling `create_plugin`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_reference_id' in params:
            query_params.append(('fileReferenceId', params['file_reference_id']))  # noqa: E501
        if 'plugin_name' in params:
            query_params.append(('pluginName', params['plugin_name']))  # noqa: E501

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
            '/plugin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Plugin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_plugin(self, plugin_id, **kwargs):  # noqa: E501
        """Delete plugin  # noqa: E501

        Delete an installed plugin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_plugin(plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int plugin_id: The ID of the plugin to delete (required)
        :param bool force: Force deletion of all dependent usage associated with the plugin, such as inventory and domain assignments of algorithms
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_plugin_with_http_info(plugin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_plugin_with_http_info(plugin_id, **kwargs)  # noqa: E501
            return data

    def delete_plugin_with_http_info(self, plugin_id, **kwargs):  # noqa: E501
        """Delete plugin  # noqa: E501

        Delete an installed plugin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_plugin_with_http_info(plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int plugin_id: The ID of the plugin to delete (required)
        :param bool force: Force deletion of all dependent usage associated with the plugin, such as inventory and domain assignments of algorithms
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_plugin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_id' is set
        if ('plugin_id' not in params or
                params['plugin_id'] is None):
            raise ValueError("Missing the required parameter `plugin_id` when calling `delete_plugin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plugin_id' in params:
            path_params['pluginId'] = params['plugin_id']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

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
            '/plugin/{pluginId}', 'DELETE',
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

    def get_all_plugins(self, **kwargs):  # noqa: E501
        """Get all plugins  # noqa: E501

        Get a detailed list of all installed plugins  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_plugins(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get algorithm plugins. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: PluginList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_plugins_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_plugins_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_plugins_with_http_info(self, **kwargs):  # noqa: E501
        """Get all plugins  # noqa: E501

        Get a detailed list of all installed plugins  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_plugins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number: The page number for which to get algorithm plugins. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: PluginList
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
                    " to method get_all_plugins" % key
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
            '/plugin', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PluginList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_plugin(self, plugin_id, **kwargs):  # noqa: E501
        """Get plugin detail by pluginId  # noqa: E501

        Get detailed information about an installed plugin by pluginId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugin(plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int plugin_id: The ID of the plugin to get (required)
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_plugin_with_http_info(plugin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_plugin_with_http_info(plugin_id, **kwargs)  # noqa: E501
            return data

    def get_plugin_with_http_info(self, plugin_id, **kwargs):  # noqa: E501
        """Get plugin detail by pluginId  # noqa: E501

        Get detailed information about an installed plugin by pluginId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugin_with_http_info(plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int plugin_id: The ID of the plugin to get (required)
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plugin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_id' is set
        if ('plugin_id' not in params or
                params['plugin_id'] is None):
            raise ValueError("Missing the required parameter `plugin_id` when calling `get_plugin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plugin_id' in params:
            path_params['pluginId'] = params['plugin_id']  # noqa: E501

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
            '/plugin/{pluginId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Plugin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_plugin(self, plugin_id, file_reference_id, **kwargs):  # noqa: E501
        """Update plugin  # noqa: E501

        Update an installed plugin to use the uploaded JAR file. The new plugin must contain all components delivered by the previous version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_plugin(plugin_id, file_reference_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int plugin_id: The ID of the plugin to update (required)
        :param str file_reference_id: The file references ID of the new uploaded plugin JAR file (required)
        :param str plugin_name: The name of the plugin
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_plugin_with_http_info(plugin_id, file_reference_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_plugin_with_http_info(plugin_id, file_reference_id, **kwargs)  # noqa: E501
            return data

    def update_plugin_with_http_info(self, plugin_id, file_reference_id, **kwargs):  # noqa: E501
        """Update plugin  # noqa: E501

        Update an installed plugin to use the uploaded JAR file. The new plugin must contain all components delivered by the previous version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_plugin_with_http_info(plugin_id, file_reference_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int plugin_id: The ID of the plugin to update (required)
        :param str file_reference_id: The file references ID of the new uploaded plugin JAR file (required)
        :param str plugin_name: The name of the plugin
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_id', 'file_reference_id', 'plugin_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_plugin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_id' is set
        if ('plugin_id' not in params or
                params['plugin_id'] is None):
            raise ValueError("Missing the required parameter `plugin_id` when calling `update_plugin`")  # noqa: E501
        # verify the required parameter 'file_reference_id' is set
        if ('file_reference_id' not in params or
                params['file_reference_id'] is None):
            raise ValueError("Missing the required parameter `file_reference_id` when calling `update_plugin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plugin_id' in params:
            path_params['pluginId'] = params['plugin_id']  # noqa: E501

        query_params = []
        if 'file_reference_id' in params:
            query_params.append(('fileReferenceId', params['file_reference_id']))  # noqa: E501
        if 'plugin_name' in params:
            query_params.append(('pluginName', params['plugin_name']))  # noqa: E501

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
            '/plugin/{pluginId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Plugin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
