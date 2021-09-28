# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PerSignalDetails(object):
    """
    Detailed information like statistics, metrics and status for a signal
    """

    #: A constant which can be used with the status property of a PerSignalDetails.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a PerSignalDetails.
    #: This constant has a value of "DROPPED"
    STATUS_DROPPED = "DROPPED"

    #: A constant which can be used with the status property of a PerSignalDetails.
    #: This constant has a value of "OTHER"
    STATUS_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new PerSignalDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param signal_name:
            The value to assign to the signal_name property of this PerSignalDetails.
        :type signal_name: str

        :param mvi_ratio:
            The value to assign to the mvi_ratio property of this PerSignalDetails.
        :type mvi_ratio: float

        :param is_quantized:
            The value to assign to the is_quantized property of this PerSignalDetails.
        :type is_quantized: bool

        :param fap:
            The value to assign to the fap property of this PerSignalDetails.
        :type fap: float

        :param min:
            The value to assign to the min property of this PerSignalDetails.
        :type min: float

        :param max:
            The value to assign to the max property of this PerSignalDetails.
        :type max: float

        :param std:
            The value to assign to the std property of this PerSignalDetails.
        :type std: float

        :param status:
            The value to assign to the status property of this PerSignalDetails.
            Allowed values for this property are: "ACCEPTED", "DROPPED", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param details:
            The value to assign to the details property of this PerSignalDetails.
        :type details: str

        """
        self.swagger_types = {
            'signal_name': 'str',
            'mvi_ratio': 'float',
            'is_quantized': 'bool',
            'fap': 'float',
            'min': 'float',
            'max': 'float',
            'std': 'float',
            'status': 'str',
            'details': 'str'
        }

        self.attribute_map = {
            'signal_name': 'signalName',
            'mvi_ratio': 'mviRatio',
            'is_quantized': 'isQuantized',
            'fap': 'fap',
            'min': 'min',
            'max': 'max',
            'std': 'std',
            'status': 'status',
            'details': 'details'
        }

        self._signal_name = None
        self._mvi_ratio = None
        self._is_quantized = None
        self._fap = None
        self._min = None
        self._max = None
        self._std = None
        self._status = None
        self._details = None

    @property
    def signal_name(self):
        """
        **[Required]** Gets the signal_name of this PerSignalDetails.
        The name of a signal.


        :return: The signal_name of this PerSignalDetails.
        :rtype: str
        """
        return self._signal_name

    @signal_name.setter
    def signal_name(self, signal_name):
        """
        Sets the signal_name of this PerSignalDetails.
        The name of a signal.


        :param signal_name: The signal_name of this PerSignalDetails.
        :type: str
        """
        self._signal_name = signal_name

    @property
    def mvi_ratio(self):
        """
        Gets the mvi_ratio of this PerSignalDetails.
        The ratio of missing values in a signal filled/imputed by the IDP algorithm.


        :return: The mvi_ratio of this PerSignalDetails.
        :rtype: float
        """
        return self._mvi_ratio

    @mvi_ratio.setter
    def mvi_ratio(self, mvi_ratio):
        """
        Sets the mvi_ratio of this PerSignalDetails.
        The ratio of missing values in a signal filled/imputed by the IDP algorithm.


        :param mvi_ratio: The mvi_ratio of this PerSignalDetails.
        :type: float
        """
        self._mvi_ratio = mvi_ratio

    @property
    def is_quantized(self):
        """
        Gets the is_quantized of this PerSignalDetails.
        A boolean value to indicate if a signal is quantized or not.


        :return: The is_quantized of this PerSignalDetails.
        :rtype: bool
        """
        return self._is_quantized

    @is_quantized.setter
    def is_quantized(self, is_quantized):
        """
        Sets the is_quantized of this PerSignalDetails.
        A boolean value to indicate if a signal is quantized or not.


        :param is_quantized: The is_quantized of this PerSignalDetails.
        :type: bool
        """
        self._is_quantized = is_quantized

    @property
    def fap(self):
        """
        Gets the fap of this PerSignalDetails.
        Accuracy metric for a signal.


        :return: The fap of this PerSignalDetails.
        :rtype: float
        """
        return self._fap

    @fap.setter
    def fap(self, fap):
        """
        Sets the fap of this PerSignalDetails.
        Accuracy metric for a signal.


        :param fap: The fap of this PerSignalDetails.
        :type: float
        """
        self._fap = fap

    @property
    def min(self):
        """
        **[Required]** Gets the min of this PerSignalDetails.
        Min value within a signal.


        :return: The min of this PerSignalDetails.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this PerSignalDetails.
        Min value within a signal.


        :param min: The min of this PerSignalDetails.
        :type: float
        """
        self._min = min

    @property
    def max(self):
        """
        **[Required]** Gets the max of this PerSignalDetails.
        Max value within a signal.


        :return: The max of this PerSignalDetails.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this PerSignalDetails.
        Max value within a signal.


        :param max: The max of this PerSignalDetails.
        :type: float
        """
        self._max = max

    @property
    def std(self):
        """
        **[Required]** Gets the std of this PerSignalDetails.
        Standard deviation of values within a signal.


        :return: The std of this PerSignalDetails.
        :rtype: float
        """
        return self._std

    @std.setter
    def std(self, std):
        """
        Sets the std of this PerSignalDetails.
        Standard deviation of values within a signal.


        :param std: The std of this PerSignalDetails.
        :type: float
        """
        self._std = std

    @property
    def status(self):
        """
        **[Required]** Gets the status of this PerSignalDetails.
        Status of the signal:
         * ACCEPTED - the signal is used for training the model
         * DROPPED - the signal does not meet requirement, and is dropped before training the model.
         * OTHER - placeholder for other status

        Allowed values for this property are: "ACCEPTED", "DROPPED", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this PerSignalDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PerSignalDetails.
        Status of the signal:
         * ACCEPTED - the signal is used for training the model
         * DROPPED - the signal does not meet requirement, and is dropped before training the model.
         * OTHER - placeholder for other status


        :param status: The status of this PerSignalDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "DROPPED", "OTHER"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def details(self):
        """
        Gets the details of this PerSignalDetails.
        detailed information for a signal.


        :return: The details of this PerSignalDetails.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this PerSignalDetails.
        detailed information for a signal.


        :param details: The details of this PerSignalDetails.
        :type: str
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
