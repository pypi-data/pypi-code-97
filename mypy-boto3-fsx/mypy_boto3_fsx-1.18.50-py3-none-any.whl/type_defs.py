"""
Type annotations for fsx service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef

    data: ActiveDirectoryBackupAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence

from .literals import (
    AdministrativeActionTypeType,
    AliasLifecycleType,
    AutoImportPolicyTypeType,
    BackupLifecycleType,
    BackupTypeType,
    DataCompressionTypeType,
    DataRepositoryLifecycleType,
    DataRepositoryTaskFilterNameType,
    DataRepositoryTaskLifecycleType,
    DiskIopsConfigurationModeType,
    DriveCacheTypeType,
    FileSystemLifecycleType,
    FileSystemMaintenanceOperationType,
    FileSystemTypeType,
    FilterNameType,
    FlexCacheEndpointTypeType,
    LustreDeploymentTypeType,
    OntapVolumeTypeType,
    ResourceTypeType,
    SecurityStyleType,
    StatusType,
    StorageTypeType,
    StorageVirtualMachineLifecycleType,
    StorageVirtualMachineRootVolumeSecurityStyleType,
    StorageVirtualMachineSubtypeType,
    TieringPolicyNameType,
    VolumeFilterNameType,
    VolumeLifecycleType,
    WindowsAccessAuditLogLevelType,
    WindowsDeploymentTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionTypeDef",
    "AliasTypeDef",
    "AssociateFileSystemAliasesRequestRequestTypeDef",
    "AssociateFileSystemAliasesResponseTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupRequestRequestTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryTaskRequestRequestTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileSystemFromBackupRequestRequestTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemOntapConfigurationTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "CreateOntapVolumeConfigurationTypeDef",
    "CreateStorageVirtualMachineRequestRequestTypeDef",
    "CreateStorageVirtualMachineResponseTypeDef",
    "CreateSvmActiveDirectoryConfigurationTypeDef",
    "CreateVolumeFromBackupRequestRequestTypeDef",
    "CreateVolumeFromBackupResponseTypeDef",
    "CreateVolumeRequestRequestTypeDef",
    "CreateVolumeResponseTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DeleteStorageVirtualMachineRequestRequestTypeDef",
    "DeleteStorageVirtualMachineResponseTypeDef",
    "DeleteVolumeOntapConfigurationTypeDef",
    "DeleteVolumeOntapResponseTypeDef",
    "DeleteVolumeRequestRequestTypeDef",
    "DeleteVolumeResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileSystemAliasesRequestRequestTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeStorageVirtualMachinesRequestRequestTypeDef",
    "DescribeStorageVirtualMachinesResponseTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVolumesResponseTypeDef",
    "DisassociateFileSystemAliasesRequestRequestTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "DiskIopsConfigurationTypeDef",
    "FileSystemEndpointTypeDef",
    "FileSystemEndpointsTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "LifecycleTransitionReasonTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "OntapFileSystemConfigurationTypeDef",
    "OntapVolumeConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "StorageVirtualMachineFilterTypeDef",
    "StorageVirtualMachineTypeDef",
    "SvmActiveDirectoryConfigurationTypeDef",
    "SvmEndpointTypeDef",
    "SvmEndpointsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TieringPolicyTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemOntapConfigurationTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
    "UpdateOntapVolumeConfigurationTypeDef",
    "UpdateStorageVirtualMachineRequestRequestTypeDef",
    "UpdateStorageVirtualMachineResponseTypeDef",
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    "UpdateVolumeRequestRequestTypeDef",
    "UpdateVolumeResponseTypeDef",
    "VolumeFilterTypeDef",
    "VolumeTypeDef",
    "WindowsAuditLogConfigurationTypeDef",
    "WindowsAuditLogCreateConfigurationTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
)

ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {
        "DomainName": str,
        "ActiveDirectoryId": str,
        "ResourceARN": str,
    },
    total=False,
)

AdministrativeActionFailureDetailsTypeDef = TypedDict(
    "AdministrativeActionFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

AdministrativeActionTypeDef = TypedDict(
    "AdministrativeActionTypeDef",
    {
        "AdministrativeActionType": AdministrativeActionTypeType,
        "ProgressPercent": int,
        "RequestTime": datetime,
        "Status": StatusType,
        "TargetFileSystemValues": Dict[str, Any],
        "FailureDetails": "AdministrativeActionFailureDetailsTypeDef",
        "TargetVolumeValues": "VolumeTypeDef",
    },
    total=False,
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": str,
        "Lifecycle": AliasLifecycleType,
    },
    total=False,
)

_RequiredAssociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": Sequence[str],
    },
)
_OptionalAssociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateFileSystemAliasesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class AssociateFileSystemAliasesRequestRequestTypeDef(
    _RequiredAssociateFileSystemAliasesRequestRequestTypeDef,
    _OptionalAssociateFileSystemAliasesRequestRequestTypeDef,
):
    pass


AssociateFileSystemAliasesResponseTypeDef = TypedDict(
    "AssociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "Type": BackupTypeType,
        "CreationTime": datetime,
        "FileSystem": "FileSystemTypeDef",
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "FailureDetails": "BackupFailureDetailsTypeDef",
        "ProgressPercent": int,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "DirectoryInformation": "ActiveDirectoryBackupAttributesTypeDef",
        "OwnerId": str,
        "SourceBackupId": str,
        "SourceBackupRegion": str,
        "ResourceType": ResourceTypeType,
        "Volume": "VolumeTypeDef",
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


CancelDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)

CancelDataRepositoryTaskResponseTypeDef = TypedDict(
    "CancelDataRepositoryTaskResponseTypeDef",
    {
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "TaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompletionReportTypeDef = TypedDict(
    "_RequiredCompletionReportTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCompletionReportTypeDef = TypedDict(
    "_OptionalCompletionReportTypeDef",
    {
        "Path": str,
        "Format": Literal["REPORT_CSV_20191124"],
        "Scope": Literal["FAILED_FILES_ONLY"],
    },
    total=False,
)


class CompletionReportTypeDef(_RequiredCompletionReportTypeDef, _OptionalCompletionReportTypeDef):
    pass


_RequiredCopyBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCopyBackupRequestRequestTypeDef",
    {
        "SourceBackupId": str,
    },
)
_OptionalCopyBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCopyBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SourceRegion": str,
        "KmsKeyId": str,
        "CopyTags": bool,
        "Tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CopyBackupRequestRequestTypeDef(
    _RequiredCopyBackupRequestRequestTypeDef, _OptionalCopyBackupRequestRequestTypeDef
):
    pass


CopyBackupResponseTypeDef = TypedDict(
    "CopyBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackupRequestRequestTypeDef = TypedDict(
    "CreateBackupRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ClientRequestToken": str,
        "Tags": Sequence["TagTypeDef"],
        "VolumeId": str,
    },
    total=False,
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataRepositoryTaskRequestRequestTypeDef",
    {
        "Type": Literal["EXPORT_TO_REPOSITORY"],
        "FileSystemId": str,
        "Report": "CompletionReportTypeDef",
    },
)
_OptionalCreateDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataRepositoryTaskRequestRequestTypeDef",
    {
        "Paths": Sequence[str],
        "ClientRequestToken": str,
        "Tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateDataRepositoryTaskRequestRequestTypeDef(
    _RequiredCreateDataRepositoryTaskRequestRequestTypeDef,
    _OptionalCreateDataRepositoryTaskRequestRequestTypeDef,
):
    pass


CreateDataRepositoryTaskResponseTypeDef = TypedDict(
    "CreateDataRepositoryTaskResponseTypeDef",
    {
        "DataRepositoryTask": "DataRepositoryTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileSystemFromBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemFromBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "SubnetIds": Sequence[str],
    },
)
_OptionalCreateFileSystemFromBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemFromBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SecurityGroupIds": Sequence[str],
        "Tags": Sequence["TagTypeDef"],
        "WindowsConfiguration": "CreateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "CreateFileSystemLustreConfigurationTypeDef",
        "StorageType": StorageTypeType,
        "KmsKeyId": str,
    },
    total=False,
)


class CreateFileSystemFromBackupRequestRequestTypeDef(
    _RequiredCreateFileSystemFromBackupRequestRequestTypeDef,
    _OptionalCreateFileSystemFromBackupRequestRequestTypeDef,
):
    pass


CreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "CreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "DeploymentType": LustreDeploymentTypeType,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "PerUnitStorageThroughput": int,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheTypeType,
        "DataCompressionType": DataCompressionTypeType,
    },
    total=False,
)

_RequiredCreateFileSystemOntapConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemOntapConfigurationTypeDef",
    {
        "DeploymentType": Literal["MULTI_AZ_1"],
        "ThroughputCapacity": int,
    },
)
_OptionalCreateFileSystemOntapConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemOntapConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "DailyAutomaticBackupStartTime": str,
        "EndpointIpAddressRange": str,
        "FsxAdminPassword": str,
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "PreferredSubnetId": str,
        "RouteTableIds": Sequence[str],
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)


class CreateFileSystemOntapConfigurationTypeDef(
    _RequiredCreateFileSystemOntapConfigurationTypeDef,
    _OptionalCreateFileSystemOntapConfigurationTypeDef,
):
    pass


_RequiredCreateFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemRequestRequestTypeDef",
    {
        "FileSystemType": FileSystemTypeType,
        "StorageCapacity": int,
        "SubnetIds": Sequence[str],
    },
)
_OptionalCreateFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "StorageType": StorageTypeType,
        "SecurityGroupIds": Sequence[str],
        "Tags": Sequence["TagTypeDef"],
        "KmsKeyId": str,
        "WindowsConfiguration": "CreateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "CreateFileSystemLustreConfigurationTypeDef",
        "OntapConfiguration": "CreateFileSystemOntapConfigurationTypeDef",
    },
    total=False,
)


class CreateFileSystemRequestRequestTypeDef(
    _RequiredCreateFileSystemRequestRequestTypeDef, _OptionalCreateFileSystemRequestRequestTypeDef
):
    pass


CreateFileSystemResponseTypeDef = TypedDict(
    "CreateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ThroughputCapacity": int,
    },
)
_OptionalCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationTypeDef",
        "DeploymentType": WindowsDeploymentTypeType,
        "PreferredSubnetId": str,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": Sequence[str],
        "AuditLogConfiguration": "WindowsAuditLogCreateConfigurationTypeDef",
    },
    total=False,
)


class CreateFileSystemWindowsConfigurationTypeDef(
    _RequiredCreateFileSystemWindowsConfigurationTypeDef,
    _OptionalCreateFileSystemWindowsConfigurationTypeDef,
):
    pass


_RequiredCreateOntapVolumeConfigurationTypeDef = TypedDict(
    "_RequiredCreateOntapVolumeConfigurationTypeDef",
    {
        "JunctionPath": str,
        "SizeInMegabytes": int,
        "StorageEfficiencyEnabled": bool,
        "StorageVirtualMachineId": str,
    },
)
_OptionalCreateOntapVolumeConfigurationTypeDef = TypedDict(
    "_OptionalCreateOntapVolumeConfigurationTypeDef",
    {
        "SecurityStyle": SecurityStyleType,
        "TieringPolicy": "TieringPolicyTypeDef",
    },
    total=False,
)


class CreateOntapVolumeConfigurationTypeDef(
    _RequiredCreateOntapVolumeConfigurationTypeDef, _OptionalCreateOntapVolumeConfigurationTypeDef
):
    pass


_RequiredCreateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStorageVirtualMachineRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Name": str,
    },
)
_OptionalCreateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStorageVirtualMachineRequestRequestTypeDef",
    {
        "ActiveDirectoryConfiguration": "CreateSvmActiveDirectoryConfigurationTypeDef",
        "ClientRequestToken": str,
        "SvmAdminPassword": str,
        "Tags": Sequence["TagTypeDef"],
        "RootVolumeSecurityStyle": StorageVirtualMachineRootVolumeSecurityStyleType,
    },
    total=False,
)


class CreateStorageVirtualMachineRequestRequestTypeDef(
    _RequiredCreateStorageVirtualMachineRequestRequestTypeDef,
    _OptionalCreateStorageVirtualMachineRequestRequestTypeDef,
):
    pass


CreateStorageVirtualMachineResponseTypeDef = TypedDict(
    "CreateStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachine": "StorageVirtualMachineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredCreateSvmActiveDirectoryConfigurationTypeDef",
    {
        "NetBiosName": str,
    },
)
_OptionalCreateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalCreateSvmActiveDirectoryConfigurationTypeDef",
    {
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationTypeDef",
    },
    total=False,
)


class CreateSvmActiveDirectoryConfigurationTypeDef(
    _RequiredCreateSvmActiveDirectoryConfigurationTypeDef,
    _OptionalCreateSvmActiveDirectoryConfigurationTypeDef,
):
    pass


_RequiredCreateVolumeFromBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVolumeFromBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "Name": str,
    },
)
_OptionalCreateVolumeFromBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVolumeFromBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "CreateOntapVolumeConfigurationTypeDef",
        "Tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateVolumeFromBackupRequestRequestTypeDef(
    _RequiredCreateVolumeFromBackupRequestRequestTypeDef,
    _OptionalCreateVolumeFromBackupRequestRequestTypeDef,
):
    pass


CreateVolumeFromBackupResponseTypeDef = TypedDict(
    "CreateVolumeFromBackupResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVolumeRequestRequestTypeDef",
    {
        "VolumeType": Literal["ONTAP"],
        "Name": str,
    },
)
_OptionalCreateVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVolumeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "CreateOntapVolumeConfigurationTypeDef",
        "Tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateVolumeRequestRequestTypeDef(
    _RequiredCreateVolumeRequestRequestTypeDef, _OptionalCreateVolumeRequestRequestTypeDef
):
    pass


CreateVolumeResponseTypeDef = TypedDict(
    "CreateVolumeResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {
        "Lifecycle": DataRepositoryLifecycleType,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "FailureDetails": "DataRepositoryFailureDetailsTypeDef",
    },
    total=False,
)

DataRepositoryFailureDetailsTypeDef = TypedDict(
    "DataRepositoryFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DataRepositoryTaskFailureDetailsTypeDef = TypedDict(
    "DataRepositoryTaskFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DataRepositoryTaskFilterTypeDef = TypedDict(
    "DataRepositoryTaskFilterTypeDef",
    {
        "Name": DataRepositoryTaskFilterNameType,
        "Values": Sequence[str],
    },
    total=False,
)

DataRepositoryTaskStatusTypeDef = TypedDict(
    "DataRepositoryTaskStatusTypeDef",
    {
        "TotalCount": int,
        "SucceededCount": int,
        "FailedCount": int,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredDataRepositoryTaskTypeDef = TypedDict(
    "_RequiredDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "Type": Literal["EXPORT_TO_REPOSITORY"],
        "CreationTime": datetime,
        "FileSystemId": str,
    },
)
_OptionalDataRepositoryTaskTypeDef = TypedDict(
    "_OptionalDataRepositoryTaskTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "Paths": List[str],
        "FailureDetails": "DataRepositoryTaskFailureDetailsTypeDef",
        "Status": "DataRepositoryTaskStatusTypeDef",
        "Report": "CompletionReportTypeDef",
    },
    total=False,
)


class DataRepositoryTaskTypeDef(
    _RequiredDataRepositoryTaskTypeDef, _OptionalDataRepositoryTaskTypeDef
):
    pass


_RequiredDeleteBackupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
_OptionalDeleteBackupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class DeleteBackupRequestRequestTypeDef(
    _RequiredDeleteBackupRequestRequestTypeDef, _OptionalDeleteBackupRequestRequestTypeDef
):
    pass


DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemLustreConfigurationTypeDef = TypedDict(
    "DeleteFileSystemLustreConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": Sequence["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemLustreResponseTypeDef = TypedDict(
    "DeleteFileSystemLustreResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDeleteFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFileSystemRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "WindowsConfiguration": "DeleteFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "DeleteFileSystemLustreConfigurationTypeDef",
    },
    total=False,
)


class DeleteFileSystemRequestRequestTypeDef(
    _RequiredDeleteFileSystemRequestRequestTypeDef, _OptionalDeleteFileSystemRequestRequestTypeDef
):
    pass


DeleteFileSystemResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": FileSystemLifecycleType,
        "WindowsResponse": "DeleteFileSystemWindowsResponseTypeDef",
        "LustreResponse": "DeleteFileSystemLustreResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": Sequence["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemWindowsResponseTypeDef = TypedDict(
    "DeleteFileSystemWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStorageVirtualMachineRequestRequestTypeDef",
    {
        "StorageVirtualMachineId": str,
    },
)
_OptionalDeleteStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStorageVirtualMachineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class DeleteStorageVirtualMachineRequestRequestTypeDef(
    _RequiredDeleteStorageVirtualMachineRequestRequestTypeDef,
    _OptionalDeleteStorageVirtualMachineRequestRequestTypeDef,
):
    pass


DeleteStorageVirtualMachineResponseTypeDef = TypedDict(
    "DeleteStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachineId": str,
        "Lifecycle": StorageVirtualMachineLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeOntapConfigurationTypeDef = TypedDict(
    "DeleteVolumeOntapConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": Sequence["TagTypeDef"],
    },
    total=False,
)

DeleteVolumeOntapResponseTypeDef = TypedDict(
    "DeleteVolumeOntapResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDeleteVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVolumeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "DeleteVolumeOntapConfigurationTypeDef",
    },
    total=False,
)


class DeleteVolumeRequestRequestTypeDef(
    _RequiredDeleteVolumeRequestRequestTypeDef, _OptionalDeleteVolumeRequestRequestTypeDef
):
    pass


DeleteVolumeResponseTypeDef = TypedDict(
    "DeleteVolumeResponseTypeDef",
    {
        "VolumeId": str,
        "Lifecycle": VolumeLifecycleType,
        "OntapResponse": "DeleteVolumeOntapResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "BackupIds": Sequence[str],
        "Filters": Sequence["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataRepositoryTasksRequestRequestTypeDef = TypedDict(
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    {
        "TaskIds": Sequence[str],
        "Filters": Sequence["DataRepositoryTaskFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDataRepositoryTasksResponseTypeDef = TypedDict(
    "DescribeDataRepositoryTasksResponseTypeDef",
    {
        "DataRepositoryTasks": List["DataRepositoryTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDescribeFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFileSystemAliasesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeFileSystemAliasesRequestRequestTypeDef(
    _RequiredDescribeFileSystemAliasesRequestRequestTypeDef,
    _OptionalDescribeFileSystemAliasesRequestRequestTypeDef,
):
    pass


DescribeFileSystemAliasesResponseTypeDef = TypedDict(
    "DescribeFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemsRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestRequestTypeDef",
    {
        "FileSystemIds": Sequence[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "FileSystems": List["FileSystemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorageVirtualMachinesRequestRequestTypeDef = TypedDict(
    "DescribeStorageVirtualMachinesRequestRequestTypeDef",
    {
        "StorageVirtualMachineIds": Sequence[str],
        "Filters": Sequence["StorageVirtualMachineFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeStorageVirtualMachinesResponseTypeDef = TypedDict(
    "DescribeStorageVirtualMachinesResponseTypeDef",
    {
        "StorageVirtualMachines": List["StorageVirtualMachineTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "VolumeIds": Sequence[str],
        "Filters": Sequence["VolumeFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVolumesResponseTypeDef = TypedDict(
    "DescribeVolumesResponseTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": Sequence[str],
    },
)
_OptionalDisassociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateFileSystemAliasesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class DisassociateFileSystemAliasesRequestRequestTypeDef(
    _RequiredDisassociateFileSystemAliasesRequestRequestTypeDef,
    _OptionalDisassociateFileSystemAliasesRequestRequestTypeDef,
):
    pass


DisassociateFileSystemAliasesResponseTypeDef = TypedDict(
    "DisassociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskIopsConfigurationTypeDef = TypedDict(
    "DiskIopsConfigurationTypeDef",
    {
        "Mode": DiskIopsConfigurationModeType,
        "Iops": int,
    },
    total=False,
)

FileSystemEndpointTypeDef = TypedDict(
    "FileSystemEndpointTypeDef",
    {
        "DNSName": str,
        "IpAddresses": List[str],
    },
    total=False,
)

FileSystemEndpointsTypeDef = TypedDict(
    "FileSystemEndpointsTypeDef",
    {
        "Intercluster": "FileSystemEndpointTypeDef",
        "Management": "FileSystemEndpointTypeDef",
    },
    total=False,
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": FileSystemTypeType,
        "Lifecycle": FileSystemLifecycleType,
        "FailureDetails": "FileSystemFailureDetailsTypeDef",
        "StorageCapacity": int,
        "StorageType": StorageTypeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "WindowsConfiguration": "WindowsFileSystemConfigurationTypeDef",
        "LustreConfiguration": "LustreFileSystemConfigurationTypeDef",
        "AdministrativeActions": List[Dict[str, Any]],
        "OntapConfiguration": "OntapFileSystemConfigurationTypeDef",
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": FilterNameType,
        "Values": Sequence[str],
    },
    total=False,
)

LifecycleTransitionReasonTypeDef = TypedDict(
    "LifecycleTransitionReasonTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": "DataRepositoryConfigurationTypeDef",
        "DeploymentType": LustreDeploymentTypeType,
        "PerUnitStorageThroughput": int,
        "MountName": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheTypeType,
        "DataCompressionType": DataCompressionTypeType,
    },
    total=False,
)

OntapFileSystemConfigurationTypeDef = TypedDict(
    "OntapFileSystemConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "DailyAutomaticBackupStartTime": str,
        "DeploymentType": Literal["MULTI_AZ_1"],
        "EndpointIpAddressRange": str,
        "Endpoints": "FileSystemEndpointsTypeDef",
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "PreferredSubnetId": str,
        "RouteTableIds": List[str],
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)

OntapVolumeConfigurationTypeDef = TypedDict(
    "OntapVolumeConfigurationTypeDef",
    {
        "FlexCacheEndpointType": FlexCacheEndpointTypeType,
        "JunctionPath": str,
        "SecurityStyle": SecurityStyleType,
        "SizeInMegabytes": int,
        "StorageEfficiencyEnabled": bool,
        "StorageVirtualMachineId": str,
        "StorageVirtualMachineRoot": bool,
        "TieringPolicy": "TieringPolicyTypeDef",
        "UUID": str,
        "OntapVolumeType": OntapVolumeTypeType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

_RequiredSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "UserName": str,
        "Password": str,
        "DnsIps": Sequence[str],
    },
)
_OptionalSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
    },
    total=False,
)


class SelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalSelfManagedActiveDirectoryConfigurationTypeDef,
):
    pass


SelfManagedActiveDirectoryConfigurationUpdatesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    {
        "UserName": str,
        "Password": str,
        "DnsIps": Sequence[str],
    },
    total=False,
)

StorageVirtualMachineFilterTypeDef = TypedDict(
    "StorageVirtualMachineFilterTypeDef",
    {
        "Name": Literal["file-system-id"],
        "Values": Sequence[str],
    },
    total=False,
)

StorageVirtualMachineTypeDef = TypedDict(
    "StorageVirtualMachineTypeDef",
    {
        "ActiveDirectoryConfiguration": "SvmActiveDirectoryConfigurationTypeDef",
        "CreationTime": datetime,
        "Endpoints": "SvmEndpointsTypeDef",
        "FileSystemId": str,
        "Lifecycle": StorageVirtualMachineLifecycleType,
        "Name": str,
        "ResourceARN": str,
        "StorageVirtualMachineId": str,
        "Subtype": StorageVirtualMachineSubtypeType,
        "UUID": str,
        "Tags": List["TagTypeDef"],
        "LifecycleTransitionReason": "LifecycleTransitionReasonTypeDef",
        "RootVolumeSecurityStyle": StorageVirtualMachineRootVolumeSecurityStyleType,
    },
    total=False,
)

SvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "SvmActiveDirectoryConfigurationTypeDef",
    {
        "NetBiosName": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryAttributesTypeDef",
    },
    total=False,
)

SvmEndpointTypeDef = TypedDict(
    "SvmEndpointTypeDef",
    {
        "DNSName": str,
        "IpAddresses": List[str],
    },
    total=False,
)

SvmEndpointsTypeDef = TypedDict(
    "SvmEndpointsTypeDef",
    {
        "Iscsi": "SvmEndpointTypeDef",
        "Management": "SvmEndpointTypeDef",
        "Nfs": "SvmEndpointTypeDef",
        "Smb": "SvmEndpointTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TieringPolicyTypeDef = TypedDict(
    "TieringPolicyTypeDef",
    {
        "CoolingPeriod": int,
        "Name": TieringPolicyNameType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "UpdateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "DataCompressionType": DataCompressionTypeType,
    },
    total=False,
)

UpdateFileSystemOntapConfigurationTypeDef = TypedDict(
    "UpdateFileSystemOntapConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "DailyAutomaticBackupStartTime": str,
        "FsxAdminPassword": str,
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)

_RequiredUpdateFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalUpdateFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFileSystemRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "StorageCapacity": int,
        "WindowsConfiguration": "UpdateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "UpdateFileSystemLustreConfigurationTypeDef",
        "OntapConfiguration": "UpdateFileSystemOntapConfigurationTypeDef",
    },
    total=False,
)


class UpdateFileSystemRequestRequestTypeDef(
    _RequiredUpdateFileSystemRequestRequestTypeDef, _OptionalUpdateFileSystemRequestRequestTypeDef
):
    pass


UpdateFileSystemResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "UpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "ThroughputCapacity": int,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
        "AuditLogConfiguration": "WindowsAuditLogCreateConfigurationTypeDef",
    },
    total=False,
)

UpdateOntapVolumeConfigurationTypeDef = TypedDict(
    "UpdateOntapVolumeConfigurationTypeDef",
    {
        "JunctionPath": str,
        "SecurityStyle": SecurityStyleType,
        "SizeInMegabytes": int,
        "StorageEfficiencyEnabled": bool,
        "TieringPolicy": "TieringPolicyTypeDef",
    },
    total=False,
)

_RequiredUpdateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageVirtualMachineRequestRequestTypeDef",
    {
        "StorageVirtualMachineId": str,
    },
)
_OptionalUpdateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageVirtualMachineRequestRequestTypeDef",
    {
        "ActiveDirectoryConfiguration": "UpdateSvmActiveDirectoryConfigurationTypeDef",
        "ClientRequestToken": str,
        "SvmAdminPassword": str,
    },
    total=False,
)


class UpdateStorageVirtualMachineRequestRequestTypeDef(
    _RequiredUpdateStorageVirtualMachineRequestRequestTypeDef,
    _OptionalUpdateStorageVirtualMachineRequestRequestTypeDef,
):
    pass


UpdateStorageVirtualMachineResponseTypeDef = TypedDict(
    "UpdateStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachine": "StorageVirtualMachineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    {
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    },
    total=False,
)

_RequiredUpdateVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalUpdateVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVolumeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "UpdateOntapVolumeConfigurationTypeDef",
    },
    total=False,
)


class UpdateVolumeRequestRequestTypeDef(
    _RequiredUpdateVolumeRequestRequestTypeDef, _OptionalUpdateVolumeRequestRequestTypeDef
):
    pass


UpdateVolumeResponseTypeDef = TypedDict(
    "UpdateVolumeResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeFilterTypeDef = TypedDict(
    "VolumeFilterTypeDef",
    {
        "Name": VolumeFilterNameType,
        "Values": Sequence[str],
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "CreationTime": datetime,
        "FileSystemId": str,
        "Lifecycle": VolumeLifecycleType,
        "Name": str,
        "OntapConfiguration": "OntapVolumeConfigurationTypeDef",
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "VolumeId": str,
        "VolumeType": Literal["ONTAP"],
        "LifecycleTransitionReason": "LifecycleTransitionReasonTypeDef",
    },
    total=False,
)

_RequiredWindowsAuditLogConfigurationTypeDef = TypedDict(
    "_RequiredWindowsAuditLogConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
    },
)
_OptionalWindowsAuditLogConfigurationTypeDef = TypedDict(
    "_OptionalWindowsAuditLogConfigurationTypeDef",
    {
        "AuditLogDestination": str,
    },
    total=False,
)


class WindowsAuditLogConfigurationTypeDef(
    _RequiredWindowsAuditLogConfigurationTypeDef, _OptionalWindowsAuditLogConfigurationTypeDef
):
    pass


_RequiredWindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "_RequiredWindowsAuditLogCreateConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
    },
)
_OptionalWindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "_OptionalWindowsAuditLogCreateConfigurationTypeDef",
    {
        "AuditLogDestination": str,
    },
    total=False,
)


class WindowsAuditLogCreateConfigurationTypeDef(
    _RequiredWindowsAuditLogCreateConfigurationTypeDef,
    _OptionalWindowsAuditLogCreateConfigurationTypeDef,
):
    pass


WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryAttributesTypeDef",
        "DeploymentType": WindowsDeploymentTypeType,
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[FileSystemMaintenanceOperationType],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List["AliasTypeDef"],
        "AuditLogConfiguration": "WindowsAuditLogConfigurationTypeDef",
    },
    total=False,
)
