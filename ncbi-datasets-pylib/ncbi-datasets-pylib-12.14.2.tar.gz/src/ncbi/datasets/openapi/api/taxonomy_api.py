"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated bag](https://www.ncbi.nlm.nih.gov/datasets/docs/rehydrate/), and retrieve the individual data files at a later time.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ncbi.datasets.openapi.api_client import ApiClient, Endpoint as _Endpoint
from ncbi.datasets.openapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ncbi.datasets.openapi.model.rpc_status import RpcStatus
from ncbi.datasets.openapi.model.v1_organism_query_request_tax_rank_filter import V1OrganismQueryRequestTaxRankFilter
from ncbi.datasets.openapi.model.v1_organism_rank_type import V1OrganismRankType
from ncbi.datasets.openapi.model.v1_sci_name_and_ids import V1SciNameAndIds
from ncbi.datasets.openapi.model.v1_taxonomy_filtered_subtree_request import V1TaxonomyFilteredSubtreeRequest
from ncbi.datasets.openapi.model.v1_taxonomy_filtered_subtree_response import V1TaxonomyFilteredSubtreeResponse
from ncbi.datasets.openapi.model.v1_taxonomy_metadata_request import V1TaxonomyMetadataRequest
from ncbi.datasets.openapi.model.v1_taxonomy_metadata_request_content_type import V1TaxonomyMetadataRequestContentType
from ncbi.datasets.openapi.model.v1_taxonomy_metadata_response import V1TaxonomyMetadataResponse


class TaxonomyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.tax_name_query_endpoint = _Endpoint(
            settings={
                'response_type': (V1SciNameAndIds,),
                'auth': [
                    'ApiKeyAuthHeader'
                ],
                'endpoint_path': '/taxonomy/taxon_suggest/{taxon_query}',
                'operation_id': 'tax_name_query',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'taxon_query',
                    'tax_rank_filter',
                ],
                'required': [
                    'taxon_query',
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
                    'taxon_query':
                        (str,),
                    'tax_rank_filter':
                        (V1OrganismQueryRequestTaxRankFilter,),
                },
                'attribute_map': {
                    'taxon_query': 'taxon_query',
                    'tax_rank_filter': 'tax_rank_filter',
                },
                'location_map': {
                    'taxon_query': 'path',
                    'tax_rank_filter': 'query',
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
        self.taxonomy_filtered_subtree_endpoint = _Endpoint(
            settings={
                'response_type': (V1TaxonomyFilteredSubtreeResponse,),
                'auth': [
                    'ApiKeyAuthHeader'
                ],
                'endpoint_path': '/taxonomy/taxon/{taxons}/filtered_subtree',
                'operation_id': 'taxonomy_filtered_subtree',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'taxons',
                    'specified_limit',
                    'rank_limits',
                ],
                'required': [
                    'taxons',
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
                    'taxons':
                        ([str],),
                    'specified_limit':
                        (bool,),
                    'rank_limits':
                        ([V1OrganismRankType],),
                },
                'attribute_map': {
                    'taxons': 'taxons',
                    'specified_limit': 'specified_limit',
                    'rank_limits': 'rank_limits',
                },
                'location_map': {
                    'taxons': 'path',
                    'specified_limit': 'query',
                    'rank_limits': 'query',
                },
                'collection_format_map': {
                    'taxons': 'csv',
                    'rank_limits': 'multi',
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
        self.taxonomy_filtered_subtree_post_endpoint = _Endpoint(
            settings={
                'response_type': (V1TaxonomyFilteredSubtreeResponse,),
                'auth': [
                    'ApiKeyAuthHeader'
                ],
                'endpoint_path': '/taxonomy/filtered_subtree',
                'operation_id': 'taxonomy_filtered_subtree_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'v1_taxonomy_filtered_subtree_request',
                ],
                'required': [
                    'v1_taxonomy_filtered_subtree_request',
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
                    'v1_taxonomy_filtered_subtree_request':
                        (V1TaxonomyFilteredSubtreeRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'v1_taxonomy_filtered_subtree_request': 'body',
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
        self.taxonomy_metadata_endpoint = _Endpoint(
            settings={
                'response_type': (V1TaxonomyMetadataResponse,),
                'auth': [
                    'ApiKeyAuthHeader'
                ],
                'endpoint_path': '/taxonomy/taxon/{taxons}',
                'operation_id': 'taxonomy_metadata',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'taxons',
                    'returned_content',
                ],
                'required': [
                    'taxons',
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
                    'taxons':
                        ([str],),
                    'returned_content':
                        (V1TaxonomyMetadataRequestContentType,),
                },
                'attribute_map': {
                    'taxons': 'taxons',
                    'returned_content': 'returned_content',
                },
                'location_map': {
                    'taxons': 'path',
                    'returned_content': 'query',
                },
                'collection_format_map': {
                    'taxons': 'csv',
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
        self.taxonomy_metadata_post_endpoint = _Endpoint(
            settings={
                'response_type': (V1TaxonomyMetadataResponse,),
                'auth': [
                    'ApiKeyAuthHeader'
                ],
                'endpoint_path': '/taxonomy',
                'operation_id': 'taxonomy_metadata_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'v1_taxonomy_metadata_request',
                ],
                'required': [
                    'v1_taxonomy_metadata_request',
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
                    'v1_taxonomy_metadata_request':
                        (V1TaxonomyMetadataRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'v1_taxonomy_metadata_request': 'body',
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

    def tax_name_query(
        self,
        taxon_query,
        accept=None,
        **kwargs
    ):
        """Get a list of taxonomy names and IDs given a partial taxonomic name  # noqa: E501

        This endpoint retrieves a list of taxonomy names and IDs given a partial taxonomic name of any rank.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.tax_name_query(taxon_query, async_req=True)
        >>> result = thread.get()

        Args:
            taxon_query (str): NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank

        Keyword Args:
            tax_rank_filter (V1OrganismQueryRequestTaxRankFilter): Set the scope of searched tax ranks. [optional]
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            V1SciNameAndIds
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['taxon_query'] = \
            taxon_query
        if accept and self.tax_name_query_endpoint.headers_map:
            updated_header_maps = self.tax_name_query_endpoint.headers_map.copy()
            if accept in updated_header_maps:
                updated_header_maps['accept'] = [accept]
                self.tax_name_query_endpoint.headers_map = updated_header_maps

        return self.tax_name_query_endpoint.call_with_http_info(**kwargs)

    def taxonomy_filtered_subtree(
        self,
        taxons,
        accept=None,
        **kwargs
    ):
        """Use taxonomic identifiers to get a filtered taxonomic subtree  # noqa: E501

        Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get a filtered taxonomic subtree that includes the full parent lineage and all immediate children from the selected taxonomic ranks in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.taxonomy_filtered_subtree(taxons, async_req=True)
        >>> result = thread.get()

        Args:
            taxons ([str]):

        Keyword Args:
            specified_limit (bool): Limit to specified species. [optional]
            rank_limits ([V1OrganismRankType]): Limit to the provided ranks.  If empty, accept any rank.. [optional]
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            V1TaxonomyFilteredSubtreeResponse
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['taxons'] = \
            taxons
        if accept and self.taxonomy_filtered_subtree_endpoint.headers_map:
            updated_header_maps = self.taxonomy_filtered_subtree_endpoint.headers_map.copy()
            if accept in updated_header_maps:
                updated_header_maps['accept'] = [accept]
                self.taxonomy_filtered_subtree_endpoint.headers_map = updated_header_maps

        return self.taxonomy_filtered_subtree_endpoint.call_with_http_info(**kwargs)

    def taxonomy_filtered_subtree_post(
        self,
        v1_taxonomy_filtered_subtree_request,
        accept=None,
        **kwargs
    ):
        """Use taxonomic identifiers to get a filtered taxonomic subtree by post  # noqa: E501

        Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get a filtered taxonomic subtree that includes the full parent lineage and all immediate children from the selected taxonomic ranks in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.taxonomy_filtered_subtree_post(v1_taxonomy_filtered_subtree_request, async_req=True)
        >>> result = thread.get()

        Args:
            v1_taxonomy_filtered_subtree_request (V1TaxonomyFilteredSubtreeRequest):

        Keyword Args:
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            V1TaxonomyFilteredSubtreeResponse
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['v1_taxonomy_filtered_subtree_request'] = \
            v1_taxonomy_filtered_subtree_request
        if accept and self.taxonomy_filtered_subtree_post_endpoint.headers_map:
            updated_header_maps = self.taxonomy_filtered_subtree_post_endpoint.headers_map.copy()
            if accept in updated_header_maps:
                updated_header_maps['accept'] = [accept]
                self.taxonomy_filtered_subtree_post_endpoint.headers_map = updated_header_maps

        return self.taxonomy_filtered_subtree_post_endpoint.call_with_http_info(**kwargs)

    def taxonomy_metadata(
        self,
        taxons,
        accept=None,
        **kwargs
    ):
        """Use taxonomic identifiers to get taxonomic metadata  # noqa: E501

        Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about a taxonomic node including taxonomic identifiers, lineage information, child nodes, and gene and genome counts in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.taxonomy_metadata(taxons, async_req=True)
        >>> result = thread.get()

        Args:
            taxons ([str]):

        Keyword Args:
            returned_content (V1TaxonomyMetadataRequestContentType): Return either tax-ids alone, or entire taxononmy-metadata records. [optional]
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            V1TaxonomyMetadataResponse
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['taxons'] = \
            taxons
        if accept and self.taxonomy_metadata_endpoint.headers_map:
            updated_header_maps = self.taxonomy_metadata_endpoint.headers_map.copy()
            if accept in updated_header_maps:
                updated_header_maps['accept'] = [accept]
                self.taxonomy_metadata_endpoint.headers_map = updated_header_maps

        return self.taxonomy_metadata_endpoint.call_with_http_info(**kwargs)

    def taxonomy_metadata_post(
        self,
        v1_taxonomy_metadata_request,
        accept=None,
        **kwargs
    ):
        """Use taxonomic identifiers to get taxonomic metadata by post  # noqa: E501

        Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about a taxonomic node including taxonomic identifiers, lineage information, child nodes, and gene and genome counts in JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.taxonomy_metadata_post(v1_taxonomy_metadata_request, async_req=True)
        >>> result = thread.get()

        Args:
            v1_taxonomy_metadata_request (V1TaxonomyMetadataRequest):

        Keyword Args:
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            V1TaxonomyMetadataResponse
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['v1_taxonomy_metadata_request'] = \
            v1_taxonomy_metadata_request
        if accept and self.taxonomy_metadata_post_endpoint.headers_map:
            updated_header_maps = self.taxonomy_metadata_post_endpoint.headers_map.copy()
            if accept in updated_header_maps:
                updated_header_maps['accept'] = [accept]
                self.taxonomy_metadata_post_endpoint.headers_map = updated_header_maps

        return self.taxonomy_metadata_post_endpoint.call_with_http_info(**kwargs)

