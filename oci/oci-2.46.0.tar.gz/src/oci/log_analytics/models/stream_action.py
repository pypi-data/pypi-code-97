# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamAction(Action):
    """
    Stream action for scheduled task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamAction object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.StreamAction.type` attribute
        of this class is ``STREAM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StreamAction.
            Allowed values for this property are: "STREAM", "PURGE"
        :type type: str

        :param saved_search_id:
            The value to assign to the saved_search_id property of this StreamAction.
        :type saved_search_id: str

        :param metric_extraction:
            The value to assign to the metric_extraction property of this StreamAction.
        :type metric_extraction: oci.log_analytics.models.MetricExtraction

        :param saved_search_duration:
            The value to assign to the saved_search_duration property of this StreamAction.
        :type saved_search_duration: str

        """
        self.swagger_types = {
            'type': 'str',
            'saved_search_id': 'str',
            'metric_extraction': 'MetricExtraction',
            'saved_search_duration': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'saved_search_id': 'savedSearchId',
            'metric_extraction': 'metricExtraction',
            'saved_search_duration': 'savedSearchDuration'
        }

        self._type = None
        self._saved_search_id = None
        self._metric_extraction = None
        self._saved_search_duration = None
        self._type = 'STREAM'

    @property
    def saved_search_id(self):
        """
        Gets the saved_search_id of this StreamAction.
        The ManagementSavedSearch id [OCID] utilized in the action.


        :return: The saved_search_id of this StreamAction.
        :rtype: str
        """
        return self._saved_search_id

    @saved_search_id.setter
    def saved_search_id(self, saved_search_id):
        """
        Sets the saved_search_id of this StreamAction.
        The ManagementSavedSearch id [OCID] utilized in the action.


        :param saved_search_id: The saved_search_id of this StreamAction.
        :type: str
        """
        self._saved_search_id = saved_search_id

    @property
    def metric_extraction(self):
        """
        Gets the metric_extraction of this StreamAction.

        :return: The metric_extraction of this StreamAction.
        :rtype: oci.log_analytics.models.MetricExtraction
        """
        return self._metric_extraction

    @metric_extraction.setter
    def metric_extraction(self, metric_extraction):
        """
        Sets the metric_extraction of this StreamAction.

        :param metric_extraction: The metric_extraction of this StreamAction.
        :type: oci.log_analytics.models.MetricExtraction
        """
        self._metric_extraction = metric_extraction

    @property
    def saved_search_duration(self):
        """
        Gets the saved_search_duration of this StreamAction.
        The duration of data to be searched for SAVED_SEARCH tasks,
        used when the task fires to calculate the query time range.

        Duration in ISO 8601 extended format as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The value should be positive.
        The largest supported unit (as opposed to value) is D, e.g.  P14D (not P2W).

        There are restrictions on the maximum duration value relative to the task schedule
        value as specified in the following table.
           Schedule Interval Range          | Maximum Duration
        ----------------------------------- | -----------------
          5 Minutes     to 30 Minutes       |   1 hour  \"PT60M\"
         31 Minutes     to  1 Hour          |  12 hours \"PT720M\"
         1 Hour+1Minute to  1 Day           |   1 day   \"P1D\"
         1 Day+1Minute  to  1 Week-1Minute  |   7 days  \"P7D\"
         1 Week         to  2 Weeks         |  14 days  \"P14D\"
         greater than 2 Weeks               |  30 days  \"P30D\"

        If not specified, the duration will be based on the schedule. For example,
        if the schedule is every 5 minutes then the savedSearchDuration will be \"PT5M\";
        if the schedule is every 3 weeks then the savedSearchDuration will be \"P21D\".


        :return: The saved_search_duration of this StreamAction.
        :rtype: str
        """
        return self._saved_search_duration

    @saved_search_duration.setter
    def saved_search_duration(self, saved_search_duration):
        """
        Sets the saved_search_duration of this StreamAction.
        The duration of data to be searched for SAVED_SEARCH tasks,
        used when the task fires to calculate the query time range.

        Duration in ISO 8601 extended format as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The value should be positive.
        The largest supported unit (as opposed to value) is D, e.g.  P14D (not P2W).

        There are restrictions on the maximum duration value relative to the task schedule
        value as specified in the following table.
           Schedule Interval Range          | Maximum Duration
        ----------------------------------- | -----------------
          5 Minutes     to 30 Minutes       |   1 hour  \"PT60M\"
         31 Minutes     to  1 Hour          |  12 hours \"PT720M\"
         1 Hour+1Minute to  1 Day           |   1 day   \"P1D\"
         1 Day+1Minute  to  1 Week-1Minute  |   7 days  \"P7D\"
         1 Week         to  2 Weeks         |  14 days  \"P14D\"
         greater than 2 Weeks               |  30 days  \"P30D\"

        If not specified, the duration will be based on the schedule. For example,
        if the schedule is every 5 minutes then the savedSearchDuration will be \"PT5M\";
        if the schedule is every 3 weeks then the savedSearchDuration will be \"P21D\".


        :param saved_search_duration: The saved_search_duration of this StreamAction.
        :type: str
        """
        self._saved_search_duration = saved_search_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
