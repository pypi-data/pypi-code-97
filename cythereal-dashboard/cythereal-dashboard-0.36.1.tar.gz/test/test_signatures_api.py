# coding: utf-8

"""
    Cythereal Dashboard API

     The API used exclusively by the MAGIC Dashboard for populating charts, graphs, tables, etc... on the dashboard.  # API Conventions  **All responses** MUST be of type `APIResponse` and contain the following fields:  * `api_version` |  The current api version * `success` | Boolean value indicating if the operation succeeded. * `code` | Status code. Typically corresponds to the HTTP status code.  * `message` | A human readable message providing more details about the operation. Can be null or empty.  **Successful operations** MUST return a `SuccessResponse`, which extends `APIResponse` by adding:  * `data` | Properties containing the response object. * `success` | MUST equal True  When returning objects from a successful response, the `data` object SHOULD contain a property named after the requested object type. For example, the `/alerts` endpoint should return a response object with `data.alerts`. This property SHOULD  contain a list of the returned objects. For the `/alerts` endpoint, the `data.alerts` property contains a list of MagicAlerts objects. See the `/alerts` endpoint documentation for an example.  **Failed Operations** MUST return an `ErrorResponse`, which extends `APIResponse` by adding:  * `success` | MUST equal False.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@cythereal.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cythereal_dashboard
from cythereal_dashboard.api.signatures_api import SignaturesApi  # noqa: E501
from cythereal_dashboard.rest import ApiException


class TestSignaturesApi(unittest.TestCase):
    """SignaturesApi unit test stubs"""

    def setUp(self):
        self.api = cythereal_dashboard.api.signatures_api.SignaturesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_magic_yara(self):
        """Test case for get_magic_yara

        \"Generate a yara rule, and campaign information for  the provided binaries.\"   # noqa: E501
        """
        pass

    def test_get_procedure_signatures(self):
        """Test case for get_procedure_signatures

        Generate procedure signatures for provided binaries.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
