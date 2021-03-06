# coding: utf-8




from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_client.api_client import ApiClient


class CatalogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_catalog(self, **kwargs):  # noqa: E501
        """Get product catalog  # noqa: E501

        Retrieves the entire product catalog, including all products, features, and their corresponding rate plans, charges. Products are returned in reverse chronological order on the UpdatedDate field.   With rate plans and rate plan charges, the REST API has a maximum array size.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :param int page_size: Number of rows returned per page.
        :param str zuora_version: The minor version of the Zuora REST API.   You only need to set this parameter if you use the `productRatePlans` field.
        :return: GETCatalogType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_catalog_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_catalog_with_http_info(self, **kwargs):  # noqa: E501
        """Get product catalog  # noqa: E501

        Retrieves the entire product catalog, including all products, features, and their corresponding rate plans, charges. Products are returned in reverse chronological order on the UpdatedDate field.   With rate plans and rate plan charges, the REST API has a maximum array size.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :param int page_size: Number of rows returned per page.
        :param str zuora_version: The minor version of the Zuora REST API.   You only need to set this parameter if you use the `productRatePlans` field.
        :return: GETCatalogType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zuora_entity_ids', 'page_size', 'zuora_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 40:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_catalog`, must be a value less than or equal to `40`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_version' in params:
            header_params['zuora-version'] = params['zuora_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/catalog/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCatalogType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_product(self, product_id, **kwargs):  # noqa: E501
        """Get product  # noqa: E501

        Retrieves detailed information about a specific product, including information about its product rate plans and charges.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: The unique ID of the product you want to retrieve. For example, 8a808255575bdae4015774e9602e16fe. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :param str zuora_version: The minor version of the Zuora REST API.   You only need to set this parameter if you use the `productRatePlans` field.
        :return: GETProductType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_product_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def get_product_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """Get product  # noqa: E501

        Retrieves detailed information about a specific product, including information about its product rate plans and charges.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: The unique ID of the product you want to retrieve. For example, 8a808255575bdae4015774e9602e16fe. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :param str zuora_version: The minor version of the Zuora REST API.   You only need to set this parameter if you use the `productRatePlans` field.
        :return: GETProductType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'zuora_entity_ids', 'zuora_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['product-id'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_version' in params:
            header_params['zuora-version'] = params['zuora_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/catalog/product/{product-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETProductType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_catalog(self, product_id, request, **kwargs):  # noqa: E501
        """Multi-entity: Share a product with an Entity  # noqa: E501

        **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Shares a product with a target entity. Zuora synchronizes the shared products to the target entity after sharing. For more information about product sharing, see [Products Sharing Across Entities](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/C_Business_Objects_Sharing_Across_Entities/B_Products_Sharing_Across_Entities).  Note that:  - You must finish all the [prerequisites](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/C_Business_Objects_Sharing_Across_Entities/B_Products_Sharing_Across_Entities/Share_Products) before sharing products with other entities.   - Only source entity administrators have permission to share products with other entities. You must make the call as a source entity administrator.  - Currently, you can only share a product with one entity at a time. An error occurs if you try to share a product to more than one entity.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_catalog(product_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: The unique ID of the product you want to share. For example, 8a808255575bdae4015774e9602e16fe. (required)
        :param POSTCatalogType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_catalog_with_http_info(product_id, request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_catalog_with_http_info(product_id, request, **kwargs)  # noqa: E501
            return data

    def post_catalog_with_http_info(self, product_id, request, **kwargs):  # noqa: E501
        """Multi-entity: Share a product with an Entity  # noqa: E501

        **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Shares a product with a target entity. Zuora synchronizes the shared products to the target entity after sharing. For more information about product sharing, see [Products Sharing Across Entities](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/C_Business_Objects_Sharing_Across_Entities/B_Products_Sharing_Across_Entities).  Note that:  - You must finish all the [prerequisites](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/C_Business_Objects_Sharing_Across_Entities/B_Products_Sharing_Across_Entities/Share_Products) before sharing products with other entities.   - Only source entity administrators have permission to share products with other entities. You must make the call as a source entity administrator.  - Currently, you can only share a product with one entity at a time. An error occurs if you try to share a product to more than one entity.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_catalog_with_http_info(product_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: The unique ID of the product you want to share. For example, 8a808255575bdae4015774e9602e16fe. (required)
        :param POSTCatalogType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_catalog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `post_catalog`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_catalog`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['product-id'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/catalog/products/{product-id}/share', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
