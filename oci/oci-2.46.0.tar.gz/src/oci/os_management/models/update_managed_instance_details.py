# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateManagedInstanceDetails(object):
    """
    Information to update a managed instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param notification_topic_id:
            The value to assign to the notification_topic_id property of this UpdateManagedInstanceDetails.
        :type notification_topic_id: str

        :param is_data_collection_authorized:
            The value to assign to the is_data_collection_authorized property of this UpdateManagedInstanceDetails.
        :type is_data_collection_authorized: bool

        """
        self.swagger_types = {
            'notification_topic_id': 'str',
            'is_data_collection_authorized': 'bool'
        }

        self.attribute_map = {
            'notification_topic_id': 'notificationTopicId',
            'is_data_collection_authorized': 'isDataCollectionAuthorized'
        }

        self._notification_topic_id = None
        self._is_data_collection_authorized = None

    @property
    def notification_topic_id(self):
        """
        Gets the notification_topic_id of this UpdateManagedInstanceDetails.
        OCID of the ONS topic used to send notification to users


        :return: The notification_topic_id of this UpdateManagedInstanceDetails.
        :rtype: str
        """
        return self._notification_topic_id

    @notification_topic_id.setter
    def notification_topic_id(self, notification_topic_id):
        """
        Sets the notification_topic_id of this UpdateManagedInstanceDetails.
        OCID of the ONS topic used to send notification to users


        :param notification_topic_id: The notification_topic_id of this UpdateManagedInstanceDetails.
        :type: str
        """
        self._notification_topic_id = notification_topic_id

    @property
    def is_data_collection_authorized(self):
        """
        Gets the is_data_collection_authorized of this UpdateManagedInstanceDetails.
        True if user allow data collection for this instance


        :return: The is_data_collection_authorized of this UpdateManagedInstanceDetails.
        :rtype: bool
        """
        return self._is_data_collection_authorized

    @is_data_collection_authorized.setter
    def is_data_collection_authorized(self, is_data_collection_authorized):
        """
        Sets the is_data_collection_authorized of this UpdateManagedInstanceDetails.
        True if user allow data collection for this instance


        :param is_data_collection_authorized: The is_data_collection_authorized of this UpdateManagedInstanceDetails.
        :type: bool
        """
        self._is_data_collection_authorized = is_data_collection_authorized

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
