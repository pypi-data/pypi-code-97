# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SessionPersistenceConfigurationDetails(object):
    """
    The configuration details for implementing session persistence based on a user-specified cookie name (application
    cookie stickiness).

    Session persistence enables the Load Balancing service to direct any number of requests that originate from a single
    logical client to a single backend web server. For more information, see
    `Session Persistence`__.

    With application cookie stickiness, the load balancer enables session persistence only when the response from a backend
    application server includes a `Set-cookie` header with the user-specified cookie name.

    To disable application cookie stickiness on a running load balancer, use the
    :func:`update_backend_set` operation and specify `null` for the
    `SessionPersistenceConfigurationDetails` object.

    Example: `SessionPersistenceConfigurationDetails: null`

    **Note:** `SessionPersistenceConfigurationDetails` (application cookie stickiness) and `LBCookieSessionPersistenceConfigurationDetails`
    (LB cookie stickiness) are mutually exclusive. An error results if you try to enable both types of session persistence.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Reference/sessionpersistence.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SessionPersistenceConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cookie_name:
            The value to assign to the cookie_name property of this SessionPersistenceConfigurationDetails.
        :type cookie_name: str

        :param disable_fallback:
            The value to assign to the disable_fallback property of this SessionPersistenceConfigurationDetails.
        :type disable_fallback: bool

        """
        self.swagger_types = {
            'cookie_name': 'str',
            'disable_fallback': 'bool'
        }

        self.attribute_map = {
            'cookie_name': 'cookieName',
            'disable_fallback': 'disableFallback'
        }

        self._cookie_name = None
        self._disable_fallback = None

    @property
    def cookie_name(self):
        """
        **[Required]** Gets the cookie_name of this SessionPersistenceConfigurationDetails.
        The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
        that any cookie set by the backend causes the session to persist.

        Example: `example_cookie`


        :return: The cookie_name of this SessionPersistenceConfigurationDetails.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """
        Sets the cookie_name of this SessionPersistenceConfigurationDetails.
        The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
        that any cookie set by the backend causes the session to persist.

        Example: `example_cookie`


        :param cookie_name: The cookie_name of this SessionPersistenceConfigurationDetails.
        :type: str
        """
        self._cookie_name = cookie_name

    @property
    def disable_fallback(self):
        """
        Gets the disable_fallback of this SessionPersistenceConfigurationDetails.
        Whether the load balancer is prevented from directing traffic from a persistent session client to
        a different backend server if the original server is unavailable. Defaults to false.

        Example: `false`


        :return: The disable_fallback of this SessionPersistenceConfigurationDetails.
        :rtype: bool
        """
        return self._disable_fallback

    @disable_fallback.setter
    def disable_fallback(self, disable_fallback):
        """
        Sets the disable_fallback of this SessionPersistenceConfigurationDetails.
        Whether the load balancer is prevented from directing traffic from a persistent session client to
        a different backend server if the original server is unavailable. Defaults to false.

        Example: `false`


        :param disable_fallback: The disable_fallback of this SessionPersistenceConfigurationDetails.
        :type: bool
        """
        self._disable_fallback = disable_fallback

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
