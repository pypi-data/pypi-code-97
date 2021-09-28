# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Certificate(object):
    """
    The configuration details of a certificate bundle.
    For more information on SSL certficate configuration, see
    `Managing SSL Certificates`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingcertificates.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Certificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_name:
            The value to assign to the certificate_name property of this Certificate.
        :type certificate_name: str

        :param public_certificate:
            The value to assign to the public_certificate property of this Certificate.
        :type public_certificate: str

        :param ca_certificate:
            The value to assign to the ca_certificate property of this Certificate.
        :type ca_certificate: str

        """
        self.swagger_types = {
            'certificate_name': 'str',
            'public_certificate': 'str',
            'ca_certificate': 'str'
        }

        self.attribute_map = {
            'certificate_name': 'certificateName',
            'public_certificate': 'publicCertificate',
            'ca_certificate': 'caCertificate'
        }

        self._certificate_name = None
        self._public_certificate = None
        self._ca_certificate = None

    @property
    def certificate_name(self):
        """
        **[Required]** Gets the certificate_name of this Certificate.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.
        Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
        Certificate bundle names cannot contain spaces. Avoid entering confidential information.

        Example: `example_certificate_bundle`


        :return: The certificate_name of this Certificate.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """
        Sets the certificate_name of this Certificate.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.
        Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
        Certificate bundle names cannot contain spaces. Avoid entering confidential information.

        Example: `example_certificate_bundle`


        :param certificate_name: The certificate_name of this Certificate.
        :type: str
        """
        self._certificate_name = certificate_name

    @property
    def public_certificate(self):
        """
        **[Required]** Gets the public_certificate of this Certificate.
        The public certificate, in PEM format, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
            A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
            MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
            YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
            ...
            -----END CERTIFICATE-----


        :return: The public_certificate of this Certificate.
        :rtype: str
        """
        return self._public_certificate

    @public_certificate.setter
    def public_certificate(self, public_certificate):
        """
        Sets the public_certificate of this Certificate.
        The public certificate, in PEM format, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
            A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
            MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
            YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
            ...
            -----END CERTIFICATE-----


        :param public_certificate: The public_certificate of this Certificate.
        :type: str
        """
        self._public_certificate = public_certificate

    @property
    def ca_certificate(self):
        """
        **[Required]** Gets the ca_certificate of this Certificate.
        The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
            EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
            VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
            aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
            ...
            -----END CERTIFICATE-----


        :return: The ca_certificate of this Certificate.
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """
        Sets the ca_certificate of this Certificate.
        The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
            EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
            VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
            aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
            ...
            -----END CERTIFICATE-----


        :param ca_certificate: The ca_certificate of this Certificate.
        :type: str
        """
        self._ca_certificate = ca_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
