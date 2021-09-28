# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAssessmentComparisonPerTarget(object):
    """
    The results of the comparison between two security assessment resources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAssessmentComparisonPerTarget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param baseline_target_id:
            The value to assign to the baseline_target_id property of this SecurityAssessmentComparisonPerTarget.
        :type baseline_target_id: str

        :param current_target_id:
            The value to assign to the current_target_id property of this SecurityAssessmentComparisonPerTarget.
        :type current_target_id: str

        :param auditing:
            The value to assign to the auditing property of this SecurityAssessmentComparisonPerTarget.
        :type auditing: list[oci.data_safe.models.Diffs]

        :param authorization_control:
            The value to assign to the authorization_control property of this SecurityAssessmentComparisonPerTarget.
        :type authorization_control: list[oci.data_safe.models.Diffs]

        :param data_encryption:
            The value to assign to the data_encryption property of this SecurityAssessmentComparisonPerTarget.
        :type data_encryption: list[oci.data_safe.models.Diffs]

        :param db_configuration:
            The value to assign to the db_configuration property of this SecurityAssessmentComparisonPerTarget.
        :type db_configuration: list[oci.data_safe.models.Diffs]

        :param fine_grained_access_control:
            The value to assign to the fine_grained_access_control property of this SecurityAssessmentComparisonPerTarget.
        :type fine_grained_access_control: list[oci.data_safe.models.Diffs]

        :param privileges_and_roles:
            The value to assign to the privileges_and_roles property of this SecurityAssessmentComparisonPerTarget.
        :type privileges_and_roles: list[oci.data_safe.models.Diffs]

        :param user_accounts:
            The value to assign to the user_accounts property of this SecurityAssessmentComparisonPerTarget.
        :type user_accounts: list[oci.data_safe.models.Diffs]

        """
        self.swagger_types = {
            'baseline_target_id': 'str',
            'current_target_id': 'str',
            'auditing': 'list[Diffs]',
            'authorization_control': 'list[Diffs]',
            'data_encryption': 'list[Diffs]',
            'db_configuration': 'list[Diffs]',
            'fine_grained_access_control': 'list[Diffs]',
            'privileges_and_roles': 'list[Diffs]',
            'user_accounts': 'list[Diffs]'
        }

        self.attribute_map = {
            'baseline_target_id': 'baselineTargetId',
            'current_target_id': 'currentTargetId',
            'auditing': 'auditing',
            'authorization_control': 'authorizationControl',
            'data_encryption': 'dataEncryption',
            'db_configuration': 'dbConfiguration',
            'fine_grained_access_control': 'fineGrainedAccessControl',
            'privileges_and_roles': 'privilegesAndRoles',
            'user_accounts': 'userAccounts'
        }

        self._baseline_target_id = None
        self._current_target_id = None
        self._auditing = None
        self._authorization_control = None
        self._data_encryption = None
        self._db_configuration = None
        self._fine_grained_access_control = None
        self._privileges_and_roles = None
        self._user_accounts = None

    @property
    def baseline_target_id(self):
        """
        Gets the baseline_target_id of this SecurityAssessmentComparisonPerTarget.
        The OCID of the target that is used as a baseline in this comparison.


        :return: The baseline_target_id of this SecurityAssessmentComparisonPerTarget.
        :rtype: str
        """
        return self._baseline_target_id

    @baseline_target_id.setter
    def baseline_target_id(self, baseline_target_id):
        """
        Sets the baseline_target_id of this SecurityAssessmentComparisonPerTarget.
        The OCID of the target that is used as a baseline in this comparison.


        :param baseline_target_id: The baseline_target_id of this SecurityAssessmentComparisonPerTarget.
        :type: str
        """
        self._baseline_target_id = baseline_target_id

    @property
    def current_target_id(self):
        """
        Gets the current_target_id of this SecurityAssessmentComparisonPerTarget.
        The OCID of the target to be compared against the baseline target.


        :return: The current_target_id of this SecurityAssessmentComparisonPerTarget.
        :rtype: str
        """
        return self._current_target_id

    @current_target_id.setter
    def current_target_id(self, current_target_id):
        """
        Sets the current_target_id of this SecurityAssessmentComparisonPerTarget.
        The OCID of the target to be compared against the baseline target.


        :param current_target_id: The current_target_id of this SecurityAssessmentComparisonPerTarget.
        :type: str
        """
        self._current_target_id = current_target_id

    @property
    def auditing(self):
        """
        Gets the auditing of this SecurityAssessmentComparisonPerTarget.
        A comparison between findings belonging to Auditing category.


        :return: The auditing of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._auditing

    @auditing.setter
    def auditing(self, auditing):
        """
        Sets the auditing of this SecurityAssessmentComparisonPerTarget.
        A comparison between findings belonging to Auditing category.


        :param auditing: The auditing of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._auditing = auditing

    @property
    def authorization_control(self):
        """
        Gets the authorization_control of this SecurityAssessmentComparisonPerTarget.
        A comparison between findings belonging to Authorization Control category.


        :return: The authorization_control of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._authorization_control

    @authorization_control.setter
    def authorization_control(self, authorization_control):
        """
        Sets the authorization_control of this SecurityAssessmentComparisonPerTarget.
        A comparison between findings belonging to Authorization Control category.


        :param authorization_control: The authorization_control of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._authorization_control = authorization_control

    @property
    def data_encryption(self):
        """
        Gets the data_encryption of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Data Encryption category.


        :return: The data_encryption of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._data_encryption

    @data_encryption.setter
    def data_encryption(self, data_encryption):
        """
        Sets the data_encryption of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Data Encryption category.


        :param data_encryption: The data_encryption of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._data_encryption = data_encryption

    @property
    def db_configuration(self):
        """
        Gets the db_configuration of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Database Configuration category.


        :return: The db_configuration of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._db_configuration

    @db_configuration.setter
    def db_configuration(self, db_configuration):
        """
        Sets the db_configuration of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Database Configuration category.


        :param db_configuration: The db_configuration of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._db_configuration = db_configuration

    @property
    def fine_grained_access_control(self):
        """
        Gets the fine_grained_access_control of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Fine-Grained Access Control category.


        :return: The fine_grained_access_control of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._fine_grained_access_control

    @fine_grained_access_control.setter
    def fine_grained_access_control(self, fine_grained_access_control):
        """
        Sets the fine_grained_access_control of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Fine-Grained Access Control category.


        :param fine_grained_access_control: The fine_grained_access_control of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._fine_grained_access_control = fine_grained_access_control

    @property
    def privileges_and_roles(self):
        """
        Gets the privileges_and_roles of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Privileges and Roles category.


        :return: The privileges_and_roles of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._privileges_and_roles

    @privileges_and_roles.setter
    def privileges_and_roles(self, privileges_and_roles):
        """
        Sets the privileges_and_roles of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to Privileges and Roles category.


        :param privileges_and_roles: The privileges_and_roles of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._privileges_and_roles = privileges_and_roles

    @property
    def user_accounts(self):
        """
        Gets the user_accounts of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to User Accounts category.


        :return: The user_accounts of this SecurityAssessmentComparisonPerTarget.
        :rtype: list[oci.data_safe.models.Diffs]
        """
        return self._user_accounts

    @user_accounts.setter
    def user_accounts(self, user_accounts):
        """
        Sets the user_accounts of this SecurityAssessmentComparisonPerTarget.
        Comparison between findings belonging to User Accounts category.


        :param user_accounts: The user_accounts of this SecurityAssessmentComparisonPerTarget.
        :type: list[oci.data_safe.models.Diffs]
        """
        self._user_accounts = user_accounts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
