# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterMetadata(object):
    """
    The properties that define meta data for a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this ClusterMetadata.
        :type time_created: datetime

        :param created_by_user_id:
            The value to assign to the created_by_user_id property of this ClusterMetadata.
        :type created_by_user_id: str

        :param created_by_work_request_id:
            The value to assign to the created_by_work_request_id property of this ClusterMetadata.
        :type created_by_work_request_id: str

        :param time_deleted:
            The value to assign to the time_deleted property of this ClusterMetadata.
        :type time_deleted: datetime

        :param deleted_by_user_id:
            The value to assign to the deleted_by_user_id property of this ClusterMetadata.
        :type deleted_by_user_id: str

        :param deleted_by_work_request_id:
            The value to assign to the deleted_by_work_request_id property of this ClusterMetadata.
        :type deleted_by_work_request_id: str

        :param time_updated:
            The value to assign to the time_updated property of this ClusterMetadata.
        :type time_updated: datetime

        :param updated_by_user_id:
            The value to assign to the updated_by_user_id property of this ClusterMetadata.
        :type updated_by_user_id: str

        :param updated_by_work_request_id:
            The value to assign to the updated_by_work_request_id property of this ClusterMetadata.
        :type updated_by_work_request_id: str

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'created_by_user_id': 'str',
            'created_by_work_request_id': 'str',
            'time_deleted': 'datetime',
            'deleted_by_user_id': 'str',
            'deleted_by_work_request_id': 'str',
            'time_updated': 'datetime',
            'updated_by_user_id': 'str',
            'updated_by_work_request_id': 'str'
        }

        self.attribute_map = {
            'time_created': 'timeCreated',
            'created_by_user_id': 'createdByUserId',
            'created_by_work_request_id': 'createdByWorkRequestId',
            'time_deleted': 'timeDeleted',
            'deleted_by_user_id': 'deletedByUserId',
            'deleted_by_work_request_id': 'deletedByWorkRequestId',
            'time_updated': 'timeUpdated',
            'updated_by_user_id': 'updatedByUserId',
            'updated_by_work_request_id': 'updatedByWorkRequestId'
        }

        self._time_created = None
        self._created_by_user_id = None
        self._created_by_work_request_id = None
        self._time_deleted = None
        self._deleted_by_user_id = None
        self._deleted_by_work_request_id = None
        self._time_updated = None
        self._updated_by_user_id = None
        self._updated_by_work_request_id = None

    @property
    def time_created(self):
        """
        Gets the time_created of this ClusterMetadata.
        The time the cluster was created.


        :return: The time_created of this ClusterMetadata.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ClusterMetadata.
        The time the cluster was created.


        :param time_created: The time_created of this ClusterMetadata.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def created_by_user_id(self):
        """
        Gets the created_by_user_id of this ClusterMetadata.
        The user who created the cluster.


        :return: The created_by_user_id of this ClusterMetadata.
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """
        Sets the created_by_user_id of this ClusterMetadata.
        The user who created the cluster.


        :param created_by_user_id: The created_by_user_id of this ClusterMetadata.
        :type: str
        """
        self._created_by_user_id = created_by_user_id

    @property
    def created_by_work_request_id(self):
        """
        Gets the created_by_work_request_id of this ClusterMetadata.
        The OCID of the work request which created the cluster.


        :return: The created_by_work_request_id of this ClusterMetadata.
        :rtype: str
        """
        return self._created_by_work_request_id

    @created_by_work_request_id.setter
    def created_by_work_request_id(self, created_by_work_request_id):
        """
        Sets the created_by_work_request_id of this ClusterMetadata.
        The OCID of the work request which created the cluster.


        :param created_by_work_request_id: The created_by_work_request_id of this ClusterMetadata.
        :type: str
        """
        self._created_by_work_request_id = created_by_work_request_id

    @property
    def time_deleted(self):
        """
        Gets the time_deleted of this ClusterMetadata.
        The time the cluster was deleted.


        :return: The time_deleted of this ClusterMetadata.
        :rtype: datetime
        """
        return self._time_deleted

    @time_deleted.setter
    def time_deleted(self, time_deleted):
        """
        Sets the time_deleted of this ClusterMetadata.
        The time the cluster was deleted.


        :param time_deleted: The time_deleted of this ClusterMetadata.
        :type: datetime
        """
        self._time_deleted = time_deleted

    @property
    def deleted_by_user_id(self):
        """
        Gets the deleted_by_user_id of this ClusterMetadata.
        The user who deleted the cluster.


        :return: The deleted_by_user_id of this ClusterMetadata.
        :rtype: str
        """
        return self._deleted_by_user_id

    @deleted_by_user_id.setter
    def deleted_by_user_id(self, deleted_by_user_id):
        """
        Sets the deleted_by_user_id of this ClusterMetadata.
        The user who deleted the cluster.


        :param deleted_by_user_id: The deleted_by_user_id of this ClusterMetadata.
        :type: str
        """
        self._deleted_by_user_id = deleted_by_user_id

    @property
    def deleted_by_work_request_id(self):
        """
        Gets the deleted_by_work_request_id of this ClusterMetadata.
        The OCID of the work request which deleted the cluster.


        :return: The deleted_by_work_request_id of this ClusterMetadata.
        :rtype: str
        """
        return self._deleted_by_work_request_id

    @deleted_by_work_request_id.setter
    def deleted_by_work_request_id(self, deleted_by_work_request_id):
        """
        Sets the deleted_by_work_request_id of this ClusterMetadata.
        The OCID of the work request which deleted the cluster.


        :param deleted_by_work_request_id: The deleted_by_work_request_id of this ClusterMetadata.
        :type: str
        """
        self._deleted_by_work_request_id = deleted_by_work_request_id

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ClusterMetadata.
        The time the cluster was updated.


        :return: The time_updated of this ClusterMetadata.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ClusterMetadata.
        The time the cluster was updated.


        :param time_updated: The time_updated of this ClusterMetadata.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def updated_by_user_id(self):
        """
        Gets the updated_by_user_id of this ClusterMetadata.
        The user who updated the cluster.


        :return: The updated_by_user_id of this ClusterMetadata.
        :rtype: str
        """
        return self._updated_by_user_id

    @updated_by_user_id.setter
    def updated_by_user_id(self, updated_by_user_id):
        """
        Sets the updated_by_user_id of this ClusterMetadata.
        The user who updated the cluster.


        :param updated_by_user_id: The updated_by_user_id of this ClusterMetadata.
        :type: str
        """
        self._updated_by_user_id = updated_by_user_id

    @property
    def updated_by_work_request_id(self):
        """
        Gets the updated_by_work_request_id of this ClusterMetadata.
        The OCID of the work request which updated the cluster.


        :return: The updated_by_work_request_id of this ClusterMetadata.
        :rtype: str
        """
        return self._updated_by_work_request_id

    @updated_by_work_request_id.setter
    def updated_by_work_request_id(self, updated_by_work_request_id):
        """
        Sets the updated_by_work_request_id of this ClusterMetadata.
        The OCID of the work request which updated the cluster.


        :param updated_by_work_request_id: The updated_by_work_request_id of this ClusterMetadata.
        :type: str
        """
        self._updated_by_work_request_id = updated_by_work_request_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
