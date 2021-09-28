# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RelatedEventSummary(object):
    """
    Event occurrence on managed instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RelatedEventSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RelatedEventSummary.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this RelatedEventSummary.
        :type instance_id: str

        :param timestamp:
            The value to assign to the timestamp property of this RelatedEventSummary.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'instance_id': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_id': 'instanceId',
            'timestamp': 'timestamp'
        }

        self._id = None
        self._instance_id = None
        self._timestamp = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RelatedEventSummary.
        OCID identifier of the event


        :return: The id of this RelatedEventSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RelatedEventSummary.
        OCID identifier of the event


        :param id: The id of this RelatedEventSummary.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this RelatedEventSummary.
        OCID identifier of the instance


        :return: The instance_id of this RelatedEventSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this RelatedEventSummary.
        OCID identifier of the instance


        :param instance_id: The instance_id of this RelatedEventSummary.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this RelatedEventSummary.
        time occurence


        :return: The timestamp of this RelatedEventSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this RelatedEventSummary.
        time occurence


        :param timestamp: The timestamp of this RelatedEventSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
