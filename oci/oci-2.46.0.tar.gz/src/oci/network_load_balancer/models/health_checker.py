# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HealthChecker(object):
    """
    The health check policy configuration.
    For more information, see `Editing Health Check Policies`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/editinghealthcheck.htm
    """

    #: A constant which can be used with the protocol property of a HealthChecker.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a HealthChecker.
    #: This constant has a value of "HTTPS"
    PROTOCOL_HTTPS = "HTTPS"

    #: A constant which can be used with the protocol property of a HealthChecker.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a HealthChecker.
    #: This constant has a value of "UDP"
    PROTOCOL_UDP = "UDP"

    def __init__(self, **kwargs):
        """
        Initializes a new HealthChecker object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this HealthChecker.
            Allowed values for this property are: "HTTP", "HTTPS", "TCP", "UDP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param port:
            The value to assign to the port property of this HealthChecker.
        :type port: int

        :param retries:
            The value to assign to the retries property of this HealthChecker.
        :type retries: int

        :param timeout_in_millis:
            The value to assign to the timeout_in_millis property of this HealthChecker.
        :type timeout_in_millis: int

        :param interval_in_millis:
            The value to assign to the interval_in_millis property of this HealthChecker.
        :type interval_in_millis: int

        :param url_path:
            The value to assign to the url_path property of this HealthChecker.
        :type url_path: str

        :param response_body_regex:
            The value to assign to the response_body_regex property of this HealthChecker.
        :type response_body_regex: str

        :param return_code:
            The value to assign to the return_code property of this HealthChecker.
        :type return_code: int

        :param request_data:
            The value to assign to the request_data property of this HealthChecker.
        :type request_data: str

        :param response_data:
            The value to assign to the response_data property of this HealthChecker.
        :type response_data: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'port': 'int',
            'retries': 'int',
            'timeout_in_millis': 'int',
            'interval_in_millis': 'int',
            'url_path': 'str',
            'response_body_regex': 'str',
            'return_code': 'int',
            'request_data': 'str',
            'response_data': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'port': 'port',
            'retries': 'retries',
            'timeout_in_millis': 'timeoutInMillis',
            'interval_in_millis': 'intervalInMillis',
            'url_path': 'urlPath',
            'response_body_regex': 'responseBodyRegex',
            'return_code': 'returnCode',
            'request_data': 'requestData',
            'response_data': 'responseData'
        }

        self._protocol = None
        self._port = None
        self._retries = None
        self._timeout_in_millis = None
        self._interval_in_millis = None
        self._url_path = None
        self._response_body_regex = None
        self._return_code = None
        self._request_data = None
        self._response_data = None

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this HealthChecker.
        The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP.

        Example: `HTTP`

        Allowed values for this property are: "HTTP", "HTTPS", "TCP", "UDP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this HealthChecker.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this HealthChecker.
        The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP.

        Example: `HTTP`


        :param protocol: The protocol of this HealthChecker.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS", "TCP", "UDP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def port(self):
        """
        Gets the port of this HealthChecker.
        The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the
        port information from the `Backend` object. The port must be specified if the backend port is 0.

        Example: `8080`


        :return: The port of this HealthChecker.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this HealthChecker.
        The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the
        port information from the `Backend` object. The port must be specified if the backend port is 0.

        Example: `8080`


        :param port: The port of this HealthChecker.
        :type: int
        """
        self._port = port

    @property
    def retries(self):
        """
        Gets the retries of this HealthChecker.
        The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies
        when recovering a server to the \"healthy\" state. The default value is 3.

        Example: `3`


        :return: The retries of this HealthChecker.
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """
        Sets the retries of this HealthChecker.
        The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies
        when recovering a server to the \"healthy\" state. The default value is 3.

        Example: `3`


        :param retries: The retries of this HealthChecker.
        :type: int
        """
        self._retries = retries

    @property
    def timeout_in_millis(self):
        """
        Gets the timeout_in_millis of this HealthChecker.
        The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
        returns within this timeout period. The default value is 3000 (3 seconds).

        Example: `3000`


        :return: The timeout_in_millis of this HealthChecker.
        :rtype: int
        """
        return self._timeout_in_millis

    @timeout_in_millis.setter
    def timeout_in_millis(self, timeout_in_millis):
        """
        Sets the timeout_in_millis of this HealthChecker.
        The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
        returns within this timeout period. The default value is 3000 (3 seconds).

        Example: `3000`


        :param timeout_in_millis: The timeout_in_millis of this HealthChecker.
        :type: int
        """
        self._timeout_in_millis = timeout_in_millis

    @property
    def interval_in_millis(self):
        """
        Gets the interval_in_millis of this HealthChecker.
        The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).

        Example: `10000`


        :return: The interval_in_millis of this HealthChecker.
        :rtype: int
        """
        return self._interval_in_millis

    @interval_in_millis.setter
    def interval_in_millis(self, interval_in_millis):
        """
        Sets the interval_in_millis of this HealthChecker.
        The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).

        Example: `10000`


        :param interval_in_millis: The interval_in_millis of this HealthChecker.
        :type: int
        """
        self._interval_in_millis = interval_in_millis

    @property
    def url_path(self):
        """
        Gets the url_path of this HealthChecker.
        The path against which to run the health check.

        Example: `/healthcheck`


        :return: The url_path of this HealthChecker.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """
        Sets the url_path of this HealthChecker.
        The path against which to run the health check.

        Example: `/healthcheck`


        :param url_path: The url_path of this HealthChecker.
        :type: str
        """
        self._url_path = url_path

    @property
    def response_body_regex(self):
        """
        Gets the response_body_regex of this HealthChecker.
        A regular expression for parsing the response body from the backend server.

        Example: `^((?!false).|\\s)*$`


        :return: The response_body_regex of this HealthChecker.
        :rtype: str
        """
        return self._response_body_regex

    @response_body_regex.setter
    def response_body_regex(self, response_body_regex):
        """
        Sets the response_body_regex of this HealthChecker.
        A regular expression for parsing the response body from the backend server.

        Example: `^((?!false).|\\s)*$`


        :param response_body_regex: The response_body_regex of this HealthChecker.
        :type: str
        """
        self._response_body_regex = response_body_regex

    @property
    def return_code(self):
        """
        Gets the return_code of this HealthChecker.
        The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
        then you can use common HTTP status codes such as \"200\".

        Example: `200`


        :return: The return_code of this HealthChecker.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """
        Sets the return_code of this HealthChecker.
        The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
        then you can use common HTTP status codes such as \"200\".

        Example: `200`


        :param return_code: The return_code of this HealthChecker.
        :type: int
        """
        self._return_code = return_code

    @property
    def request_data(self):
        """
        Gets the request_data of this HealthChecker.
        Base64 encoded pattern to be sent as UDP or TCP health check probe.


        :return: The request_data of this HealthChecker.
        :rtype: str
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """
        Sets the request_data of this HealthChecker.
        Base64 encoded pattern to be sent as UDP or TCP health check probe.


        :param request_data: The request_data of this HealthChecker.
        :type: str
        """
        self._request_data = request_data

    @property
    def response_data(self):
        """
        Gets the response_data of this HealthChecker.
        Base64 encoded pattern to be validated as UDP or TCP health check probe response.


        :return: The response_data of this HealthChecker.
        :rtype: str
        """
        return self._response_data

    @response_data.setter
    def response_data(self, response_data):
        """
        Sets the response_data of this HealthChecker.
        Base64 encoded pattern to be validated as UDP or TCP health check probe response.


        :param response_data: The response_data of this HealthChecker.
        :type: str
        """
        self._response_data = response_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
