"""
Type annotations for emr service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/literals.html)

Usage::

    ```python
    from mypy_boto3_emr.literals import ActionOnFailureType

    data: ActionOnFailureType = "CANCEL_AND_WAIT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionOnFailureType",
    "AdjustmentTypeType",
    "AuthModeType",
    "AutoScalingPolicyStateChangeReasonCodeType",
    "AutoScalingPolicyStateType",
    "CancelStepsRequestStatusType",
    "ClusterRunningWaiterName",
    "ClusterStateChangeReasonCodeType",
    "ClusterStateType",
    "ClusterTerminatedWaiterName",
    "ComparisonOperatorType",
    "ComputeLimitsUnitTypeType",
    "ExecutionEngineTypeType",
    "IdentityTypeType",
    "InstanceCollectionTypeType",
    "InstanceFleetStateChangeReasonCodeType",
    "InstanceFleetStateType",
    "InstanceFleetTypeType",
    "InstanceGroupStateChangeReasonCodeType",
    "InstanceGroupStateType",
    "InstanceGroupTypeType",
    "InstanceRoleTypeType",
    "InstanceStateChangeReasonCodeType",
    "InstanceStateType",
    "JobFlowExecutionStateType",
    "ListBootstrapActionsPaginatorName",
    "ListClustersPaginatorName",
    "ListInstanceFleetsPaginatorName",
    "ListInstanceGroupsPaginatorName",
    "ListInstancesPaginatorName",
    "ListNotebookExecutionsPaginatorName",
    "ListSecurityConfigurationsPaginatorName",
    "ListStepsPaginatorName",
    "ListStudioSessionMappingsPaginatorName",
    "ListStudiosPaginatorName",
    "MarketTypeType",
    "NotebookExecutionStatusType",
    "OnDemandCapacityReservationPreferenceType",
    "OnDemandCapacityReservationUsageStrategyType",
    "OnDemandProvisioningAllocationStrategyType",
    "PlacementGroupStrategyType",
    "RepoUpgradeOnBootType",
    "ScaleDownBehaviorType",
    "SpotProvisioningAllocationStrategyType",
    "SpotProvisioningTimeoutActionType",
    "StatisticType",
    "StepCancellationOptionType",
    "StepCompleteWaiterName",
    "StepExecutionStateType",
    "StepStateChangeReasonCodeType",
    "StepStateType",
    "UnitType",
    "ServiceName",
    "PaginatorName",
    "WaiterName",
)


ActionOnFailureType = Literal[
    "CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_CLUSTER", "TERMINATE_JOB_FLOW"
]
AdjustmentTypeType = Literal["CHANGE_IN_CAPACITY", "EXACT_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY"]
AuthModeType = Literal["IAM", "SSO"]
AutoScalingPolicyStateChangeReasonCodeType = Literal[
    "CLEANUP_FAILURE", "PROVISION_FAILURE", "USER_REQUEST"
]
AutoScalingPolicyStateType = Literal[
    "ATTACHED", "ATTACHING", "DETACHED", "DETACHING", "FAILED", "PENDING"
]
CancelStepsRequestStatusType = Literal["FAILED", "SUBMITTED"]
ClusterRunningWaiterName = Literal["cluster_running"]
ClusterStateChangeReasonCodeType = Literal[
    "ALL_STEPS_COMPLETED",
    "BOOTSTRAP_FAILURE",
    "INSTANCE_FAILURE",
    "INSTANCE_FLEET_TIMEOUT",
    "INTERNAL_ERROR",
    "STEP_FAILURE",
    "USER_REQUEST",
    "VALIDATION_ERROR",
]
ClusterStateType = Literal[
    "BOOTSTRAPPING",
    "RUNNING",
    "STARTING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
    "TERMINATING",
    "WAITING",
]
ClusterTerminatedWaiterName = Literal["cluster_terminated"]
ComparisonOperatorType = Literal[
    "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
]
ComputeLimitsUnitTypeType = Literal["InstanceFleetUnits", "Instances", "VCPU"]
ExecutionEngineTypeType = Literal["EMR"]
IdentityTypeType = Literal["GROUP", "USER"]
InstanceCollectionTypeType = Literal["INSTANCE_FLEET", "INSTANCE_GROUP"]
InstanceFleetStateChangeReasonCodeType = Literal[
    "CLUSTER_TERMINATED", "INSTANCE_FAILURE", "INTERNAL_ERROR", "VALIDATION_ERROR"
]
InstanceFleetStateType = Literal[
    "BOOTSTRAPPING", "PROVISIONING", "RESIZING", "RUNNING", "SUSPENDED", "TERMINATED", "TERMINATING"
]
InstanceFleetTypeType = Literal["CORE", "MASTER", "TASK"]
InstanceGroupStateChangeReasonCodeType = Literal[
    "CLUSTER_TERMINATED", "INSTANCE_FAILURE", "INTERNAL_ERROR", "VALIDATION_ERROR"
]
InstanceGroupStateType = Literal[
    "ARRESTED",
    "BOOTSTRAPPING",
    "ENDED",
    "PROVISIONING",
    "RECONFIGURING",
    "RESIZING",
    "RUNNING",
    "SHUTTING_DOWN",
    "SUSPENDED",
    "TERMINATED",
    "TERMINATING",
]
InstanceGroupTypeType = Literal["CORE", "MASTER", "TASK"]
InstanceRoleTypeType = Literal["CORE", "MASTER", "TASK"]
InstanceStateChangeReasonCodeType = Literal[
    "BOOTSTRAP_FAILURE",
    "CLUSTER_TERMINATED",
    "INSTANCE_FAILURE",
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
]
InstanceStateType = Literal[
    "AWAITING_FULFILLMENT", "BOOTSTRAPPING", "PROVISIONING", "RUNNING", "TERMINATED"
]
JobFlowExecutionStateType = Literal[
    "BOOTSTRAPPING",
    "COMPLETED",
    "FAILED",
    "RUNNING",
    "SHUTTING_DOWN",
    "STARTING",
    "TERMINATED",
    "WAITING",
]
ListBootstrapActionsPaginatorName = Literal["list_bootstrap_actions"]
ListClustersPaginatorName = Literal["list_clusters"]
ListInstanceFleetsPaginatorName = Literal["list_instance_fleets"]
ListInstanceGroupsPaginatorName = Literal["list_instance_groups"]
ListInstancesPaginatorName = Literal["list_instances"]
ListNotebookExecutionsPaginatorName = Literal["list_notebook_executions"]
ListSecurityConfigurationsPaginatorName = Literal["list_security_configurations"]
ListStepsPaginatorName = Literal["list_steps"]
ListStudioSessionMappingsPaginatorName = Literal["list_studio_session_mappings"]
ListStudiosPaginatorName = Literal["list_studios"]
MarketTypeType = Literal["ON_DEMAND", "SPOT"]
NotebookExecutionStatusType = Literal[
    "FAILED",
    "FAILING",
    "FINISHED",
    "FINISHING",
    "RUNNING",
    "STARTING",
    "START_PENDING",
    "STOPPED",
    "STOPPING",
    "STOP_PENDING",
]
OnDemandCapacityReservationPreferenceType = Literal["none", "open"]
OnDemandCapacityReservationUsageStrategyType = Literal["use-capacity-reservations-first"]
OnDemandProvisioningAllocationStrategyType = Literal["lowest-price"]
PlacementGroupStrategyType = Literal["CLUSTER", "NONE", "PARTITION", "SPREAD"]
RepoUpgradeOnBootType = Literal["NONE", "SECURITY"]
ScaleDownBehaviorType = Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"]
SpotProvisioningAllocationStrategyType = Literal["capacity-optimized"]
SpotProvisioningTimeoutActionType = Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"]
StatisticType = Literal["AVERAGE", "MAXIMUM", "MINIMUM", "SAMPLE_COUNT", "SUM"]
StepCancellationOptionType = Literal["SEND_INTERRUPT", "TERMINATE_PROCESS"]
StepCompleteWaiterName = Literal["step_complete"]
StepExecutionStateType = Literal[
    "CANCELLED", "COMPLETED", "CONTINUE", "FAILED", "INTERRUPTED", "PENDING", "RUNNING"
]
StepStateChangeReasonCodeType = Literal["NONE"]
StepStateType = Literal[
    "CANCELLED", "CANCEL_PENDING", "COMPLETED", "FAILED", "INTERRUPTED", "PENDING", "RUNNING"
]
UnitType = Literal[
    "BITS",
    "BITS_PER_SECOND",
    "BYTES",
    "BYTES_PER_SECOND",
    "COUNT",
    "COUNT_PER_SECOND",
    "GIGA_BITS",
    "GIGA_BITS_PER_SECOND",
    "GIGA_BYTES",
    "GIGA_BYTES_PER_SECOND",
    "KILO_BITS",
    "KILO_BITS_PER_SECOND",
    "KILO_BYTES",
    "KILO_BYTES_PER_SECOND",
    "MEGA_BITS",
    "MEGA_BITS_PER_SECOND",
    "MEGA_BYTES",
    "MEGA_BYTES_PER_SECOND",
    "MICRO_SECONDS",
    "MILLI_SECONDS",
    "NONE",
    "PERCENT",
    "SECONDS",
    "TERA_BITS",
    "TERA_BITS_PER_SECOND",
    "TERA_BYTES",
    "TERA_BYTES_PER_SECOND",
]
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
    "list_bootstrap_actions",
    "list_clusters",
    "list_instance_fleets",
    "list_instance_groups",
    "list_instances",
    "list_notebook_executions",
    "list_security_configurations",
    "list_steps",
    "list_studio_session_mappings",
    "list_studios",
]
WaiterName = Literal["cluster_running", "cluster_terminated", "step_complete"]
