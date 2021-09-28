# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PbiProvisioningConfig(Model):
    """The information on how authentication needs to happen for embedded
    resources.

    :param use_client_login_for_reports: Indicates whether we need to use
     client login for Pbi Embedded
    :type use_client_login_for_reports: bool
    :param use_client_login_for_pq: Indicates whether we need to use client
     login for PQ Embedded
    :type use_client_login_for_pq: bool
    :param capacity_id: Power BI Capacity id
    :type capacity_id: str
    """

    _attribute_map = {
        'use_client_login_for_reports': {'key': 'useClientLoginForReports', 'type': 'bool'},
        'use_client_login_for_pq': {'key': 'useClientLoginForPQ', 'type': 'bool'},
        'capacity_id': {'key': 'capacityId', 'type': 'str'},
    }

    def __init__(self, *, use_client_login_for_reports: bool=None, use_client_login_for_pq: bool=None, capacity_id: str=None, **kwargs) -> None:
        super(PbiProvisioningConfig, self).__init__(**kwargs)
        self.use_client_login_for_reports = use_client_login_for_reports
        self.use_client_login_for_pq = use_client_login_for_pq
        self.capacity_id = capacity_id
