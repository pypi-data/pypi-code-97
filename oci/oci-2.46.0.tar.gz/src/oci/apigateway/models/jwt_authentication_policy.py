# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .authentication_policy import AuthenticationPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JwtAuthenticationPolicy(AuthenticationPolicy):
    """
    Validate a JWT token present in the header or query parameter. A valid
    policy must specify either tokenHeader or tokenQueryParam.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JwtAuthenticationPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.JwtAuthenticationPolicy.type` attribute
        of this class is ``JWT_AUTHENTICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_anonymous_access_allowed:
            The value to assign to the is_anonymous_access_allowed property of this JwtAuthenticationPolicy.
        :type is_anonymous_access_allowed: bool

        :param type:
            The value to assign to the type property of this JwtAuthenticationPolicy.
            Allowed values for this property are: "CUSTOM_AUTHENTICATION", "JWT_AUTHENTICATION"
        :type type: str

        :param token_header:
            The value to assign to the token_header property of this JwtAuthenticationPolicy.
        :type token_header: str

        :param token_query_param:
            The value to assign to the token_query_param property of this JwtAuthenticationPolicy.
        :type token_query_param: str

        :param token_auth_scheme:
            The value to assign to the token_auth_scheme property of this JwtAuthenticationPolicy.
        :type token_auth_scheme: str

        :param issuers:
            The value to assign to the issuers property of this JwtAuthenticationPolicy.
        :type issuers: list[str]

        :param audiences:
            The value to assign to the audiences property of this JwtAuthenticationPolicy.
        :type audiences: list[str]

        :param verify_claims:
            The value to assign to the verify_claims property of this JwtAuthenticationPolicy.
        :type verify_claims: list[oci.apigateway.models.JsonWebTokenClaim]

        :param max_clock_skew_in_seconds:
            The value to assign to the max_clock_skew_in_seconds property of this JwtAuthenticationPolicy.
        :type max_clock_skew_in_seconds: float

        :param public_keys:
            The value to assign to the public_keys property of this JwtAuthenticationPolicy.
        :type public_keys: oci.apigateway.models.PublicKeySet

        """
        self.swagger_types = {
            'is_anonymous_access_allowed': 'bool',
            'type': 'str',
            'token_header': 'str',
            'token_query_param': 'str',
            'token_auth_scheme': 'str',
            'issuers': 'list[str]',
            'audiences': 'list[str]',
            'verify_claims': 'list[JsonWebTokenClaim]',
            'max_clock_skew_in_seconds': 'float',
            'public_keys': 'PublicKeySet'
        }

        self.attribute_map = {
            'is_anonymous_access_allowed': 'isAnonymousAccessAllowed',
            'type': 'type',
            'token_header': 'tokenHeader',
            'token_query_param': 'tokenQueryParam',
            'token_auth_scheme': 'tokenAuthScheme',
            'issuers': 'issuers',
            'audiences': 'audiences',
            'verify_claims': 'verifyClaims',
            'max_clock_skew_in_seconds': 'maxClockSkewInSeconds',
            'public_keys': 'publicKeys'
        }

        self._is_anonymous_access_allowed = None
        self._type = None
        self._token_header = None
        self._token_query_param = None
        self._token_auth_scheme = None
        self._issuers = None
        self._audiences = None
        self._verify_claims = None
        self._max_clock_skew_in_seconds = None
        self._public_keys = None
        self._type = 'JWT_AUTHENTICATION'

    @property
    def token_header(self):
        """
        Gets the token_header of this JwtAuthenticationPolicy.
        The name of the header containing the authentication token.


        :return: The token_header of this JwtAuthenticationPolicy.
        :rtype: str
        """
        return self._token_header

    @token_header.setter
    def token_header(self, token_header):
        """
        Sets the token_header of this JwtAuthenticationPolicy.
        The name of the header containing the authentication token.


        :param token_header: The token_header of this JwtAuthenticationPolicy.
        :type: str
        """
        self._token_header = token_header

    @property
    def token_query_param(self):
        """
        Gets the token_query_param of this JwtAuthenticationPolicy.
        The name of the query parameter containing the authentication token.


        :return: The token_query_param of this JwtAuthenticationPolicy.
        :rtype: str
        """
        return self._token_query_param

    @token_query_param.setter
    def token_query_param(self, token_query_param):
        """
        Sets the token_query_param of this JwtAuthenticationPolicy.
        The name of the query parameter containing the authentication token.


        :param token_query_param: The token_query_param of this JwtAuthenticationPolicy.
        :type: str
        """
        self._token_query_param = token_query_param

    @property
    def token_auth_scheme(self):
        """
        Gets the token_auth_scheme of this JwtAuthenticationPolicy.
        The authentication scheme that is to be used when authenticating
        the token. This must to be provided if \"tokenHeader\" is specified.


        :return: The token_auth_scheme of this JwtAuthenticationPolicy.
        :rtype: str
        """
        return self._token_auth_scheme

    @token_auth_scheme.setter
    def token_auth_scheme(self, token_auth_scheme):
        """
        Sets the token_auth_scheme of this JwtAuthenticationPolicy.
        The authentication scheme that is to be used when authenticating
        the token. This must to be provided if \"tokenHeader\" is specified.


        :param token_auth_scheme: The token_auth_scheme of this JwtAuthenticationPolicy.
        :type: str
        """
        self._token_auth_scheme = token_auth_scheme

    @property
    def issuers(self):
        """
        **[Required]** Gets the issuers of this JwtAuthenticationPolicy.
        A list of parties that could have issued the token.


        :return: The issuers of this JwtAuthenticationPolicy.
        :rtype: list[str]
        """
        return self._issuers

    @issuers.setter
    def issuers(self, issuers):
        """
        Sets the issuers of this JwtAuthenticationPolicy.
        A list of parties that could have issued the token.


        :param issuers: The issuers of this JwtAuthenticationPolicy.
        :type: list[str]
        """
        self._issuers = issuers

    @property
    def audiences(self):
        """
        **[Required]** Gets the audiences of this JwtAuthenticationPolicy.
        The list of intended recipients for the token.


        :return: The audiences of this JwtAuthenticationPolicy.
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """
        Sets the audiences of this JwtAuthenticationPolicy.
        The list of intended recipients for the token.


        :param audiences: The audiences of this JwtAuthenticationPolicy.
        :type: list[str]
        """
        self._audiences = audiences

    @property
    def verify_claims(self):
        """
        Gets the verify_claims of this JwtAuthenticationPolicy.
        A list of claims which should be validated to consider the token valid.


        :return: The verify_claims of this JwtAuthenticationPolicy.
        :rtype: list[oci.apigateway.models.JsonWebTokenClaim]
        """
        return self._verify_claims

    @verify_claims.setter
    def verify_claims(self, verify_claims):
        """
        Sets the verify_claims of this JwtAuthenticationPolicy.
        A list of claims which should be validated to consider the token valid.


        :param verify_claims: The verify_claims of this JwtAuthenticationPolicy.
        :type: list[oci.apigateway.models.JsonWebTokenClaim]
        """
        self._verify_claims = verify_claims

    @property
    def max_clock_skew_in_seconds(self):
        """
        Gets the max_clock_skew_in_seconds of this JwtAuthenticationPolicy.
        The maximum expected time difference between the system clocks
        of the token issuer and the API Gateway.


        :return: The max_clock_skew_in_seconds of this JwtAuthenticationPolicy.
        :rtype: float
        """
        return self._max_clock_skew_in_seconds

    @max_clock_skew_in_seconds.setter
    def max_clock_skew_in_seconds(self, max_clock_skew_in_seconds):
        """
        Sets the max_clock_skew_in_seconds of this JwtAuthenticationPolicy.
        The maximum expected time difference between the system clocks
        of the token issuer and the API Gateway.


        :param max_clock_skew_in_seconds: The max_clock_skew_in_seconds of this JwtAuthenticationPolicy.
        :type: float
        """
        self._max_clock_skew_in_seconds = max_clock_skew_in_seconds

    @property
    def public_keys(self):
        """
        **[Required]** Gets the public_keys of this JwtAuthenticationPolicy.

        :return: The public_keys of this JwtAuthenticationPolicy.
        :rtype: oci.apigateway.models.PublicKeySet
        """
        return self._public_keys

    @public_keys.setter
    def public_keys(self, public_keys):
        """
        Sets the public_keys of this JwtAuthenticationPolicy.

        :param public_keys: The public_keys of this JwtAuthenticationPolicy.
        :type: oci.apigateway.models.PublicKeySet
        """
        self._public_keys = public_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
