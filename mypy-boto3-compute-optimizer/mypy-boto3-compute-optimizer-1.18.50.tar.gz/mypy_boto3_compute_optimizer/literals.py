"""
Type annotations for compute-optimizer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/literals.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.literals import CpuVendorArchitectureType

    data: CpuVendorArchitectureType = "AWS_ARM64"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CpuVendorArchitectureType",
    "EBSFilterNameType",
    "EBSFindingType",
    "EBSMetricNameType",
    "EnrollmentFilterNameType",
    "ExportableAutoScalingGroupFieldType",
    "ExportableInstanceFieldType",
    "ExportableLambdaFunctionFieldType",
    "ExportableVolumeFieldType",
    "FileFormatType",
    "FilterNameType",
    "FindingReasonCodeType",
    "FindingType",
    "InstanceRecommendationFindingReasonCodeType",
    "JobFilterNameType",
    "JobStatusType",
    "LambdaFunctionMemoryMetricNameType",
    "LambdaFunctionMemoryMetricStatisticType",
    "LambdaFunctionMetricNameType",
    "LambdaFunctionMetricStatisticType",
    "LambdaFunctionRecommendationFilterNameType",
    "LambdaFunctionRecommendationFindingReasonCodeType",
    "LambdaFunctionRecommendationFindingType",
    "MetricNameType",
    "MetricStatisticType",
    "PlatformDifferenceType",
    "RecommendationSourceTypeType",
    "ResourceTypeType",
    "StatusType",
    "ServiceName",
)


CpuVendorArchitectureType = Literal["AWS_ARM64", "CURRENT"]
EBSFilterNameType = Literal["Finding"]
EBSFindingType = Literal["NotOptimized", "Optimized"]
EBSMetricNameType = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
]
EnrollmentFilterNameType = Literal["Status"]
ExportableAutoScalingGroupFieldType = Literal[
    "AccountId",
    "AutoScalingGroupArn",
    "AutoScalingGroupName",
    "CurrentConfigurationDesiredCapacity",
    "CurrentConfigurationInstanceType",
    "CurrentConfigurationMaxSize",
    "CurrentConfigurationMinSize",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
]
ExportableInstanceFieldType = Literal[
    "AccountId",
    "CurrentInstanceType",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "FindingReasonCodes",
    "InstanceArn",
    "InstanceName",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsPlatformDifferences",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
]
ExportableLambdaFunctionFieldType = Literal[
    "AccountId",
    "CurrentConfigurationMemorySize",
    "CurrentConfigurationTimeout",
    "CurrentCostAverage",
    "CurrentCostTotal",
    "Finding",
    "FindingReasonCodes",
    "FunctionArn",
    "FunctionVersion",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "NumberOfInvocations",
    "RecommendationOptionsConfigurationMemorySize",
    "RecommendationOptionsCostHigh",
    "RecommendationOptionsCostLow",
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
    "UtilizationMetricsDurationAverage",
    "UtilizationMetricsDurationMaximum",
    "UtilizationMetricsMemoryAverage",
    "UtilizationMetricsMemoryMaximum",
]
ExportableVolumeFieldType = Literal[
    "AccountId",
    "CurrentConfigurationVolumeBaselineIOPS",
    "CurrentConfigurationVolumeBaselineThroughput",
    "CurrentConfigurationVolumeBurstIOPS",
    "CurrentConfigurationVolumeBurstThroughput",
    "CurrentConfigurationVolumeSize",
    "CurrentConfigurationVolumeType",
    "CurrentMonthlyPrice",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationVolumeBaselineIOPS",
    "RecommendationOptionsConfigurationVolumeBaselineThroughput",
    "RecommendationOptionsConfigurationVolumeBurstIOPS",
    "RecommendationOptionsConfigurationVolumeBurstThroughput",
    "RecommendationOptionsConfigurationVolumeSize",
    "RecommendationOptionsConfigurationVolumeType",
    "RecommendationOptionsMonthlyPrice",
    "RecommendationOptionsPerformanceRisk",
    "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "VolumeArn",
]
FileFormatType = Literal["Csv"]
FilterNameType = Literal["Finding", "FindingReasonCodes", "RecommendationSourceType"]
FindingReasonCodeType = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
FindingType = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
InstanceRecommendationFindingReasonCodeType = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "DiskIOPSOverprovisioned",
    "DiskIOPSUnderprovisioned",
    "DiskThroughputOverprovisioned",
    "DiskThroughputUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NetworkPPSOverprovisioned",
    "NetworkPPSUnderprovisioned",
]
JobFilterNameType = Literal["JobStatus", "ResourceType"]
JobStatusType = Literal["Complete", "Failed", "InProgress", "Queued"]
LambdaFunctionMemoryMetricNameType = Literal["Duration"]
LambdaFunctionMemoryMetricStatisticType = Literal["Expected", "LowerBound", "UpperBound"]
LambdaFunctionMetricNameType = Literal["Duration", "Memory"]
LambdaFunctionMetricStatisticType = Literal["Average", "Maximum"]
LambdaFunctionRecommendationFilterNameType = Literal["Finding", "FindingReasonCode"]
LambdaFunctionRecommendationFindingReasonCodeType = Literal[
    "Inconclusive", "InsufficientData", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
LambdaFunctionRecommendationFindingType = Literal["NotOptimized", "Optimized", "Unavailable"]
MetricNameType = Literal[
    "Cpu",
    "DISK_READ_BYTES_PER_SECOND",
    "DISK_READ_OPS_PER_SECOND",
    "DISK_WRITE_BYTES_PER_SECOND",
    "DISK_WRITE_OPS_PER_SECOND",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "Memory",
    "NETWORK_IN_BYTES_PER_SECOND",
    "NETWORK_OUT_BYTES_PER_SECOND",
    "NETWORK_PACKETS_IN_PER_SECOND",
    "NETWORK_PACKETS_OUT_PER_SECOND",
]
MetricStatisticType = Literal["Average", "Maximum"]
PlatformDifferenceType = Literal[
    "Architecture",
    "Hypervisor",
    "InstanceStoreAvailability",
    "NetworkInterface",
    "StorageInterface",
    "VirtualizationType",
]
RecommendationSourceTypeType = Literal[
    "AutoScalingGroup", "EbsVolume", "Ec2Instance", "LambdaFunction"
]
ResourceTypeType = Literal["AutoScalingGroup", "EbsVolume", "Ec2Instance", "LambdaFunction"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
ServiceName = Literal[
    "accessanalyzer",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "backup",
    "batch",
    "braket",
    "budgets",
    "ce",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-messaging",
    "cloud9",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecommit",
    "codedeploy",
    "codeguru-reviewer",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectparticipant",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "dax",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "es",
    "events",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iotwireless",
    "ivs",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "machinelearning",
    "macie",
    "macie2",
    "managedblockchain",
    "marketplace-catalog",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migrationhub-config",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "network-firewall",
    "networkmanager",
    "nimble",
    "opensearch",
    "opsworks",
    "opsworkscm",
    "organizations",
    "outposts",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "polly",
    "pricing",
    "proton",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "rekognition",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53resolver",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-runtime",
    "savingsplans",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "support",
    "swf",
    "synthetics",
    "textract",
    "timestream-query",
    "timestream-write",
    "transcribe",
    "transfer",
    "translate",
    "voice-id",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "xray",
]
