# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import apm_traces_type_mapping
missing = Sentinel("Missing")


class QueryClient(object):
    """
    API for APM Trace service. Use this API to query the Traces and associated Spans.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20200630',
            'service_endpoint_template': 'https://apm-trace.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        self.base_client = BaseClient("query", config, signer, apm_traces_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def list_quick_picks(self, apm_domain_id, **kwargs):
        """
        Returns a list of predefined quick pick queries intended to assist the user
        to choose a query to run.  There is no sorting applied on the results.


        :param str apm_domain_id: (required)
            The APM Domain Id the request is intended for.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request.  If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results.
            This is usually retrieved from a previous response.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.apm_traces.models.QuickPickSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.46.0/apmtraces/list_quick_picks.py.html>`__ to see an example of how to use list_quick_picks API.
        """
        resource_path = "/queries/quickPicks"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_quick_picks got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "apmDomainId": apm_domain_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[QuickPickSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[QuickPickSummary]")

    def query(self, apm_domain_id, time_span_started_greater_than_or_equal_to, time_span_started_less_than, query_details, **kwargs):
        """
        Given a query, constructed according to the APM Defined Query Syntax, retrieves the results - selected attributes,
        and aggregations of the queried entity.  Query Results are filtered by the filter criteria specified in the where clause.
        Further query results are grouped by the attributes specified in the group by clause.  Finally,
        ordering (asc/desc) is done by the specified attributes in the order by clause.


        :param str apm_domain_id: (required)
            The APM Domain Id the request is intended for.

        :param datetime time_span_started_greater_than_or_equal_to: (required)
            Include spans that have a `spanStartTime` equal to or greater this value.

        :param datetime time_span_started_less_than: (required)
            Include spans that have a `spanStartTime`less than this value.

        :param oci.apm_traces.models.QueryDetails query_details: (required)
            Request body containing the query to be run against our repository.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request.  If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results.
            This is usually retrieved from a previous response.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_traces.models.QueryResultResponse`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.46.0/apmtraces/query.py.html>`__ to see an example of how to use query API.
        """
        resource_path = "/queries/actions/runQuery"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "query got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "apmDomainId": apm_domain_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "timeSpanStartedGreaterThanOrEqualTo": time_span_started_greater_than_or_equal_to,
            "timeSpanStartedLessThan": time_span_started_less_than
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=query_details,
                response_type="QueryResultResponse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=query_details,
                response_type="QueryResultResponse")

    def query_old(self, apm_domain_id, time_span_started_greater_than_or_equal_to, time_span_started_less_than, query_details, **kwargs):
        """
        THIS API ENDPOINT WILL BE DEPRECATED AND INSTEAD /queries/actions/runQuery as defined below WILL BE USED GOING FORWARD.  THIS EXISTS JUST
        AS A TEMPORARY PLACEHOLDER SO AS TO BE BACKWARDS COMPATIBLE WITH THE UI BETWEEN RELEASE CYCLES.
        Given a query, constructed according to the APM Defined Query Syntax, retrieves the results - selected attributes,
        and aggregations of the queried entity.  Query Results are filtered by the filter criteria specified in the where clause.
        Further query results are grouped by the attributes specified in the group by clause.  Finally,
        ordering (asc/desc) is done by the specified attributes in the order by clause.


        :param str apm_domain_id: (required)
            The APM Domain Id the request is intended for.

        :param datetime time_span_started_greater_than_or_equal_to: (required)
            Include spans that have a `spanStartTime` equal to or greater this value.

        :param datetime time_span_started_less_than: (required)
            Include spans that have a `spanStartTime`less than this value.

        :param oci.apm_traces.models.QueryDetails query_details: (required)
            Request body containing the query to be run against our repository.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request.  If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results.
            This is usually retrieved from a previous response.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_traces.models.QueryResultResponse`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/2.46.0/apmtraces/query_old.py.html>`__ to see an example of how to use query_old API.
        """
        resource_path = "/queries/action/runQuery"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "query_old got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "apmDomainId": apm_domain_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "timeSpanStartedGreaterThanOrEqualTo": time_span_started_greater_than_or_equal_to,
            "timeSpanStartedLessThan": time_span_started_less_than
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=query_details,
                response_type="QueryResultResponse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=query_details,
                response_type="QueryResultResponse")
