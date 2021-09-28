# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InstanceCreationRequest(Model):
    """InstanceCreationRequest.

    :param instance_metadata:
    :type instance_metadata:
     ~dynamics.customerinsights.api.models.InstanceMetadata
    :param byosa_resource_metadata:
    :type byosa_resource_metadata:
     ~dynamics.customerinsights.api.models.ResourceMetadata
    :param cds_resource_metadata:
    :type cds_resource_metadata:
     ~dynamics.customerinsights.api.models.ResourceMetadata
    :param is_cds_mdl_storage_enabled:
    :type is_cds_mdl_storage_enabled: bool
    :param is_ci_to_byosa_migration_enabled:
    :type is_ci_to_byosa_migration_enabled: bool
    :param bap_provisioning_type: Possible values include: 'skip', 'create',
     'attach'
    :type bap_provisioning_type: str or
     ~dynamics.customerinsights.api.models.enum
    :param is_pbi_provisioning_required:
    :type is_pbi_provisioning_required: bool
    :param is_dataverse_update_requested:
    :type is_dataverse_update_requested: bool
    """

    _attribute_map = {
        'instance_metadata': {'key': 'instanceMetadata', 'type': 'InstanceMetadata'},
        'byosa_resource_metadata': {'key': 'byosaResourceMetadata', 'type': 'ResourceMetadata'},
        'cds_resource_metadata': {'key': 'cdsResourceMetadata', 'type': 'ResourceMetadata'},
        'is_cds_mdl_storage_enabled': {'key': 'isCdsMdlStorageEnabled', 'type': 'bool'},
        'is_ci_to_byosa_migration_enabled': {'key': 'isCiToByosaMigrationEnabled', 'type': 'bool'},
        'bap_provisioning_type': {'key': 'bapProvisioningType', 'type': 'str'},
        'is_pbi_provisioning_required': {'key': 'isPbiProvisioningRequired', 'type': 'bool'},
        'is_dataverse_update_requested': {'key': 'isDataverseUpdateRequested', 'type': 'bool'},
    }

    def __init__(self, *, instance_metadata=None, byosa_resource_metadata=None, cds_resource_metadata=None, is_cds_mdl_storage_enabled: bool=None, is_ci_to_byosa_migration_enabled: bool=None, bap_provisioning_type=None, is_pbi_provisioning_required: bool=None, is_dataverse_update_requested: bool=None, **kwargs) -> None:
        super(InstanceCreationRequest, self).__init__(**kwargs)
        self.instance_metadata = instance_metadata
        self.byosa_resource_metadata = byosa_resource_metadata
        self.cds_resource_metadata = cds_resource_metadata
        self.is_cds_mdl_storage_enabled = is_cds_mdl_storage_enabled
        self.is_ci_to_byosa_migration_enabled = is_ci_to_byosa_migration_enabled
        self.bap_provisioning_type = bap_provisioning_type
        self.is_pbi_provisioning_required = is_pbi_provisioning_required
        self.is_dataverse_update_requested = is_dataverse_update_requested
