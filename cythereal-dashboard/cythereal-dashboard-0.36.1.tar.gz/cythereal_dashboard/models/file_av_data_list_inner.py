# coding: utf-8

"""
    Cythereal Dashboard API

     The API used exclusively by the MAGIC Dashboard for populating charts, graphs, tables, etc... on the dashboard.  # API Conventions  **All responses** MUST be of type `APIResponse` and contain the following fields:  * `api_version` |  The current api version * `success` | Boolean value indicating if the operation succeeded. * `code` | Status code. Typically corresponds to the HTTP status code.  * `message` | A human readable message providing more details about the operation. Can be null or empty.  **Successful operations** MUST return a `SuccessResponse`, which extends `APIResponse` by adding:  * `data` | Properties containing the response object. * `success` | MUST equal True  When returning objects from a successful response, the `data` object SHOULD contain a property named after the requested object type. For example, the `/alerts` endpoint should return a response object with `data.alerts`. This property SHOULD  contain a list of the returned objects. For the `/alerts` endpoint, the `data.alerts` property contains a list of MagicAlerts objects. See the `/alerts` endpoint documentation for an example.  **Failed Operations** MUST return an `ErrorResponse`, which extends `APIResponse` by adding:  * `success` | MUST equal False.   # noqa: E501

    OpenAPI spec version: 0.36.1
    Contact: support@cythereal.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileAVDataListInner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sha1': 'Sha1',
        'tokens': 'Tokens',
        'av_names': 'AvNames',
        'num_scans': 'int',
        'num_detections': 'int',
        'scan_date': 'Timestamp',
        'evasiveness': 'Evasiveness'
    }

    attribute_map = {
        'sha1': 'sha1',
        'tokens': 'tokens',
        'av_names': 'av_names',
        'num_scans': 'num_scans',
        'num_detections': 'num_detections',
        'scan_date': 'scan_date',
        'evasiveness': 'evasiveness'
    }

    def __init__(self, sha1=None, tokens=None, av_names=None, num_scans=None, num_detections=None, scan_date=None, evasiveness=None):  # noqa: E501
        """FileAVDataListInner - a model defined in Swagger"""  # noqa: E501

        self._sha1 = None
        self._tokens = None
        self._av_names = None
        self._num_scans = None
        self._num_detections = None
        self._scan_date = None
        self._evasiveness = None
        self.discriminator = None

        if sha1 is not None:
            self.sha1 = sha1
        if tokens is not None:
            self.tokens = tokens
        if av_names is not None:
            self.av_names = av_names
        if num_scans is not None:
            self.num_scans = num_scans
        if num_detections is not None:
            self.num_detections = num_detections
        if scan_date is not None:
            self.scan_date = scan_date
        if evasiveness is not None:
            self.evasiveness = evasiveness

    @property
    def sha1(self):
        """Gets the sha1 of this FileAVDataListInner.  # noqa: E501


        :return: The sha1 of this FileAVDataListInner.  # noqa: E501
        :rtype: Sha1
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileAVDataListInner.


        :param sha1: The sha1 of this FileAVDataListInner.  # noqa: E501
        :type: Sha1
        """

        self._sha1 = sha1

    @property
    def tokens(self):
        """Gets the tokens of this FileAVDataListInner.  # noqa: E501


        :return: The tokens of this FileAVDataListInner.  # noqa: E501
        :rtype: Tokens
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this FileAVDataListInner.


        :param tokens: The tokens of this FileAVDataListInner.  # noqa: E501
        :type: Tokens
        """

        self._tokens = tokens

    @property
    def av_names(self):
        """Gets the av_names of this FileAVDataListInner.  # noqa: E501


        :return: The av_names of this FileAVDataListInner.  # noqa: E501
        :rtype: AvNames
        """
        return self._av_names

    @av_names.setter
    def av_names(self, av_names):
        """Sets the av_names of this FileAVDataListInner.


        :param av_names: The av_names of this FileAVDataListInner.  # noqa: E501
        :type: AvNames
        """

        self._av_names = av_names

    @property
    def num_scans(self):
        """Gets the num_scans of this FileAVDataListInner.  # noqa: E501

        The number of virus vendors that scanned this file similar payload  # noqa: E501

        :return: The num_scans of this FileAVDataListInner.  # noqa: E501
        :rtype: int
        """
        return self._num_scans

    @num_scans.setter
    def num_scans(self, num_scans):
        """Sets the num_scans of this FileAVDataListInner.

        The number of virus vendors that scanned this file similar payload  # noqa: E501

        :param num_scans: The num_scans of this FileAVDataListInner.  # noqa: E501
        :type: int
        """

        self._num_scans = num_scans

    @property
    def num_detections(self):
        """Gets the num_detections of this FileAVDataListInner.  # noqa: E501

        The number of virus vendors that detected this file as malicious  # noqa: E501

        :return: The num_detections of this FileAVDataListInner.  # noqa: E501
        :rtype: int
        """
        return self._num_detections

    @num_detections.setter
    def num_detections(self, num_detections):
        """Sets the num_detections of this FileAVDataListInner.

        The number of virus vendors that detected this file as malicious  # noqa: E501

        :param num_detections: The num_detections of this FileAVDataListInner.  # noqa: E501
        :type: int
        """

        self._num_detections = num_detections

    @property
    def scan_date(self):
        """Gets the scan_date of this FileAVDataListInner.  # noqa: E501


        :return: The scan_date of this FileAVDataListInner.  # noqa: E501
        :rtype: Timestamp
        """
        return self._scan_date

    @scan_date.setter
    def scan_date(self, scan_date):
        """Sets the scan_date of this FileAVDataListInner.


        :param scan_date: The scan_date of this FileAVDataListInner.  # noqa: E501
        :type: Timestamp
        """

        self._scan_date = scan_date

    @property
    def evasiveness(self):
        """Gets the evasiveness of this FileAVDataListInner.  # noqa: E501


        :return: The evasiveness of this FileAVDataListInner.  # noqa: E501
        :rtype: Evasiveness
        """
        return self._evasiveness

    @evasiveness.setter
    def evasiveness(self, evasiveness):
        """Sets the evasiveness of this FileAVDataListInner.


        :param evasiveness: The evasiveness of this FileAVDataListInner.  # noqa: E501
        :type: Evasiveness
        """

        self._evasiveness = evasiveness

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FileAVDataListInner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileAVDataListInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
