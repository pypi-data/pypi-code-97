"""
Type annotations for gamelift service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/literals.html)

Usage::

    ```python
    from mypy_boto3_gamelift.literals import AcceptanceTypeType

    data: AcceptanceTypeType = "ACCEPT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AcceptanceTypeType",
    "BackfillModeType",
    "BalancingStrategyType",
    "BuildStatusType",
    "CertificateTypeType",
    "ComparisonOperatorTypeType",
    "DescribeFleetAttributesPaginatorName",
    "DescribeFleetCapacityPaginatorName",
    "DescribeFleetEventsPaginatorName",
    "DescribeFleetUtilizationPaginatorName",
    "DescribeGameServerInstancesPaginatorName",
    "DescribeGameSessionDetailsPaginatorName",
    "DescribeGameSessionQueuesPaginatorName",
    "DescribeGameSessionsPaginatorName",
    "DescribeInstancesPaginatorName",
    "DescribeMatchmakingConfigurationsPaginatorName",
    "DescribeMatchmakingRuleSetsPaginatorName",
    "DescribePlayerSessionsPaginatorName",
    "DescribeScalingPoliciesPaginatorName",
    "EC2InstanceTypeType",
    "EventCodeType",
    "FleetActionType",
    "FleetStatusType",
    "FleetTypeType",
    "FlexMatchModeType",
    "GameServerClaimStatusType",
    "GameServerGroupActionType",
    "GameServerGroupDeleteOptionType",
    "GameServerGroupInstanceTypeType",
    "GameServerGroupStatusType",
    "GameServerHealthCheckType",
    "GameServerInstanceStatusType",
    "GameServerProtectionPolicyType",
    "GameServerUtilizationStatusType",
    "GameSessionPlacementStateType",
    "GameSessionStatusReasonType",
    "GameSessionStatusType",
    "InstanceStatusType",
    "IpProtocolType",
    "ListAliasesPaginatorName",
    "ListBuildsPaginatorName",
    "ListFleetsPaginatorName",
    "ListGameServerGroupsPaginatorName",
    "ListGameServersPaginatorName",
    "ListScriptsPaginatorName",
    "LocationUpdateStatusType",
    "MatchmakingConfigurationStatusType",
    "MetricNameType",
    "OperatingSystemType",
    "PlayerSessionCreationPolicyType",
    "PlayerSessionStatusType",
    "PolicyTypeType",
    "PriorityTypeType",
    "ProtectionPolicyType",
    "RoutingStrategyTypeType",
    "ScalingAdjustmentTypeType",
    "ScalingStatusTypeType",
    "SearchGameSessionsPaginatorName",
    "SortOrderType",
    "ServiceName",
    "PaginatorName",
)


AcceptanceTypeType = Literal["ACCEPT", "REJECT"]
BackfillModeType = Literal["AUTOMATIC", "MANUAL"]
BalancingStrategyType = Literal["ON_DEMAND_ONLY", "SPOT_ONLY", "SPOT_PREFERRED"]
BuildStatusType = Literal["FAILED", "INITIALIZED", "READY"]
CertificateTypeType = Literal["DISABLED", "GENERATED"]
ComparisonOperatorTypeType = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
DescribeFleetAttributesPaginatorName = Literal["describe_fleet_attributes"]
DescribeFleetCapacityPaginatorName = Literal["describe_fleet_capacity"]
DescribeFleetEventsPaginatorName = Literal["describe_fleet_events"]
DescribeFleetUtilizationPaginatorName = Literal["describe_fleet_utilization"]
DescribeGameServerInstancesPaginatorName = Literal["describe_game_server_instances"]
DescribeGameSessionDetailsPaginatorName = Literal["describe_game_session_details"]
DescribeGameSessionQueuesPaginatorName = Literal["describe_game_session_queues"]
DescribeGameSessionsPaginatorName = Literal["describe_game_sessions"]
DescribeInstancesPaginatorName = Literal["describe_instances"]
DescribeMatchmakingConfigurationsPaginatorName = Literal["describe_matchmaking_configurations"]
DescribeMatchmakingRuleSetsPaginatorName = Literal["describe_matchmaking_rule_sets"]
DescribePlayerSessionsPaginatorName = Literal["describe_player_sessions"]
DescribeScalingPoliciesPaginatorName = Literal["describe_scaling_policies"]
EC2InstanceTypeType = Literal[
    "c3.2xlarge",
    "c3.4xlarge",
    "c3.8xlarge",
    "c3.large",
    "c3.xlarge",
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c4.large",
    "c4.xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.large",
    "c5.xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.large",
    "c5a.xlarge",
    "m3.2xlarge",
    "m3.large",
    "m3.medium",
    "m3.xlarge",
    "m4.10xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.large",
    "m4.xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.large",
    "m5.xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.large",
    "m5a.xlarge",
    "r3.2xlarge",
    "r3.4xlarge",
    "r3.8xlarge",
    "r3.large",
    "r3.xlarge",
    "r4.16xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.large",
    "r4.xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.large",
    "r5.xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.large",
    "r5a.xlarge",
    "t2.large",
    "t2.medium",
    "t2.micro",
    "t2.small",
]
EventCodeType = Literal[
    "FLEET_ACTIVATION_FAILED",
    "FLEET_ACTIVATION_FAILED_NO_INSTANCES",
    "FLEET_BINARY_DOWNLOAD_FAILED",
    "FLEET_CREATED",
    "FLEET_CREATION_EXTRACTING_BUILD",
    "FLEET_CREATION_RUNNING_INSTALLER",
    "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
    "FLEET_DELETED",
    "FLEET_INITIALIZATION_FAILED",
    "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED",
    "FLEET_SCALING_EVENT",
    "FLEET_STATE_ACTIVATING",
    "FLEET_STATE_ACTIVE",
    "FLEET_STATE_BUILDING",
    "FLEET_STATE_DOWNLOADING",
    "FLEET_STATE_ERROR",
    "FLEET_STATE_VALIDATING",
    "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE",
    "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
    "FLEET_VALIDATION_TIMED_OUT",
    "FLEET_VPC_PEERING_DELETED",
    "FLEET_VPC_PEERING_FAILED",
    "FLEET_VPC_PEERING_SUCCEEDED",
    "GAME_SESSION_ACTIVATION_TIMEOUT",
    "GENERIC_EVENT",
    "INSTANCE_INTERRUPTED",
    "SERVER_PROCESS_CRASHED",
    "SERVER_PROCESS_FORCE_TERMINATED",
    "SERVER_PROCESS_INVALID_PATH",
    "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT",
    "SERVER_PROCESS_PROCESS_READY_TIMEOUT",
    "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT",
    "SERVER_PROCESS_TERMINATED_UNHEALTHY",
]
FleetActionType = Literal["AUTO_SCALING"]
FleetStatusType = Literal[
    "ACTIVATING",
    "ACTIVE",
    "BUILDING",
    "DELETING",
    "DOWNLOADING",
    "ERROR",
    "NEW",
    "TERMINATED",
    "VALIDATING",
]
FleetTypeType = Literal["ON_DEMAND", "SPOT"]
FlexMatchModeType = Literal["STANDALONE", "WITH_QUEUE"]
GameServerClaimStatusType = Literal["CLAIMED"]
GameServerGroupActionType = Literal["REPLACE_INSTANCE_TYPES"]
GameServerGroupDeleteOptionType = Literal["FORCE_DELETE", "RETAIN", "SAFE_DELETE"]
GameServerGroupInstanceTypeType = Literal[
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c4.large",
    "c4.xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.large",
    "c5.xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.large",
    "c5a.xlarge",
    "m4.10xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.large",
    "m4.xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.large",
    "m5.xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.large",
    "m5a.xlarge",
    "r4.16xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.large",
    "r4.xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.large",
    "r5.xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.large",
    "r5a.xlarge",
]
GameServerGroupStatusType = Literal[
    "ACTIVATING", "ACTIVE", "DELETED", "DELETE_SCHEDULED", "DELETING", "ERROR", "NEW"
]
GameServerHealthCheckType = Literal["HEALTHY"]
GameServerInstanceStatusType = Literal["ACTIVE", "DRAINING", "SPOT_TERMINATING"]
GameServerProtectionPolicyType = Literal["FULL_PROTECTION", "NO_PROTECTION"]
GameServerUtilizationStatusType = Literal["AVAILABLE", "UTILIZED"]
GameSessionPlacementStateType = Literal["CANCELLED", "FAILED", "FULFILLED", "PENDING", "TIMED_OUT"]
GameSessionStatusReasonType = Literal["INTERRUPTED"]
GameSessionStatusType = Literal["ACTIVATING", "ACTIVE", "ERROR", "TERMINATED", "TERMINATING"]
InstanceStatusType = Literal["ACTIVE", "PENDING", "TERMINATING"]
IpProtocolType = Literal["TCP", "UDP"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListBuildsPaginatorName = Literal["list_builds"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListGameServerGroupsPaginatorName = Literal["list_game_server_groups"]
ListGameServersPaginatorName = Literal["list_game_servers"]
ListScriptsPaginatorName = Literal["list_scripts"]
LocationUpdateStatusType = Literal["PENDING_UPDATE"]
MatchmakingConfigurationStatusType = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PLACING",
    "QUEUED",
    "REQUIRES_ACCEPTANCE",
    "SEARCHING",
    "TIMED_OUT",
]
MetricNameType = Literal[
    "ActivatingGameSessions",
    "ActiveGameSessions",
    "ActiveInstances",
    "AvailableGameSessions",
    "AvailablePlayerSessions",
    "CurrentPlayerSessions",
    "IdleInstances",
    "PercentAvailableGameSessions",
    "PercentIdleInstances",
    "QueueDepth",
    "WaitTime",
]
OperatingSystemType = Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
PlayerSessionCreationPolicyType = Literal["ACCEPT_ALL", "DENY_ALL"]
PlayerSessionStatusType = Literal["ACTIVE", "COMPLETED", "RESERVED", "TIMEDOUT"]
PolicyTypeType = Literal["RuleBased", "TargetBased"]
PriorityTypeType = Literal["COST", "DESTINATION", "LATENCY", "LOCATION"]
ProtectionPolicyType = Literal["FullProtection", "NoProtection"]
RoutingStrategyTypeType = Literal["SIMPLE", "TERMINAL"]
ScalingAdjustmentTypeType = Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
ScalingStatusTypeType = Literal[
    "ACTIVE", "DELETED", "DELETE_REQUESTED", "DELETING", "ERROR", "UPDATE_REQUESTED", "UPDATING"
]
SearchGameSessionsPaginatorName = Literal["search_game_sessions"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
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
PaginatorName = Literal[
    "describe_fleet_attributes",
    "describe_fleet_capacity",
    "describe_fleet_events",
    "describe_fleet_utilization",
    "describe_game_server_instances",
    "describe_game_session_details",
    "describe_game_session_queues",
    "describe_game_sessions",
    "describe_instances",
    "describe_matchmaking_configurations",
    "describe_matchmaking_rule_sets",
    "describe_player_sessions",
    "describe_scaling_policies",
    "list_aliases",
    "list_builds",
    "list_fleets",
    "list_game_server_groups",
    "list_game_servers",
    "list_scripts",
    "search_game_sessions",
]
