"""
Type annotations for nimble service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/literals.html)

Usage::

    ```python
    from mypy_boto3_nimble.literals import LaunchProfilePersonaType

    data: LaunchProfilePersonaType = "USER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "LaunchProfilePersonaType",
    "LaunchProfilePlatformType",
    "LaunchProfileStateType",
    "LaunchProfileStatusCodeType",
    "ListEulaAcceptancesPaginatorName",
    "ListEulasPaginatorName",
    "ListLaunchProfileMembersPaginatorName",
    "ListLaunchProfilesPaginatorName",
    "ListStreamingImagesPaginatorName",
    "ListStreamingSessionsPaginatorName",
    "ListStudioComponentsPaginatorName",
    "ListStudioMembersPaginatorName",
    "ListStudiosPaginatorName",
    "StreamingClipboardModeType",
    "StreamingImageEncryptionConfigurationKeyTypeType",
    "StreamingImageStateType",
    "StreamingImageStatusCodeType",
    "StreamingInstanceTypeType",
    "StreamingSessionStateType",
    "StreamingSessionStatusCodeType",
    "StreamingSessionStreamStateType",
    "StreamingSessionStreamStatusCodeType",
    "StudioComponentInitializationScriptRunContextType",
    "StudioComponentStateType",
    "StudioComponentStatusCodeType",
    "StudioComponentSubtypeType",
    "StudioComponentTypeType",
    "StudioEncryptionConfigurationKeyTypeType",
    "StudioPersonaType",
    "StudioStateType",
    "StudioStatusCodeType",
    "ServiceName",
    "PaginatorName",
)


LaunchProfilePersonaType = Literal["USER"]
LaunchProfilePlatformType = Literal["LINUX", "WINDOWS"]
LaunchProfileStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
LaunchProfileStatusCodeType = Literal[
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "INVALID_SUBNETS_PROVIDED",
    "LAUNCH_PROFILE_CREATED",
    "LAUNCH_PROFILE_CREATE_IN_PROGRESS",
    "LAUNCH_PROFILE_DELETED",
    "LAUNCH_PROFILE_DELETE_IN_PROGRESS",
    "LAUNCH_PROFILE_UPDATED",
    "LAUNCH_PROFILE_UPDATE_IN_PROGRESS",
    "LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED",
    "STREAMING_IMAGE_NOT_FOUND",
    "STREAMING_IMAGE_NOT_READY",
]
ListEulaAcceptancesPaginatorName = Literal["list_eula_acceptances"]
ListEulasPaginatorName = Literal["list_eulas"]
ListLaunchProfileMembersPaginatorName = Literal["list_launch_profile_members"]
ListLaunchProfilesPaginatorName = Literal["list_launch_profiles"]
ListStreamingImagesPaginatorName = Literal["list_streaming_images"]
ListStreamingSessionsPaginatorName = Literal["list_streaming_sessions"]
ListStudioComponentsPaginatorName = Literal["list_studio_components"]
ListStudioMembersPaginatorName = Literal["list_studio_members"]
ListStudiosPaginatorName = Literal["list_studios"]
StreamingClipboardModeType = Literal["DISABLED", "ENABLED"]
StreamingImageEncryptionConfigurationKeyTypeType = Literal["CUSTOMER_MANAGED_KEY"]
StreamingImageStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StreamingImageStatusCodeType = Literal[
    "INTERNAL_ERROR",
    "STREAMING_IMAGE_CREATE_IN_PROGRESS",
    "STREAMING_IMAGE_DELETED",
    "STREAMING_IMAGE_DELETE_IN_PROGRESS",
    "STREAMING_IMAGE_READY",
    "STREAMING_IMAGE_UPDATE_IN_PROGRESS",
]
StreamingInstanceTypeType = Literal[
    "g4dn.12xlarge", "g4dn.16xlarge", "g4dn.2xlarge", "g4dn.4xlarge", "g4dn.8xlarge", "g4dn.xlarge"
]
StreamingSessionStateType = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"
]
StreamingSessionStatusCodeType = Literal[
    "ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
    "DECRYPT_STREAMING_IMAGE_ERROR",
    "INITIALIZATION_SCRIPT_ERROR",
    "INSUFFICIENT_CAPACITY",
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "NETWORK_INTERFACE_ERROR",
    "STREAMING_SESSION_CREATE_IN_PROGRESS",
    "STREAMING_SESSION_DELETED",
    "STREAMING_SESSION_DELETE_IN_PROGRESS",
    "STREAMING_SESSION_READY",
]
StreamingSessionStreamStateType = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"
]
StreamingSessionStreamStatusCodeType = Literal[
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "STREAM_CREATE_IN_PROGRESS",
    "STREAM_DELETED",
    "STREAM_DELETE_IN_PROGRESS",
    "STREAM_READY",
]
StudioComponentInitializationScriptRunContextType = Literal[
    "SYSTEM_INITIALIZATION", "USER_INITIALIZATION"
]
StudioComponentStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StudioComponentStatusCodeType = Literal[
    "ACTIVE_DIRECTORY_ALREADY_EXISTS",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "STUDIO_COMPONENT_CREATED",
    "STUDIO_COMPONENT_CREATE_IN_PROGRESS",
    "STUDIO_COMPONENT_DELETED",
    "STUDIO_COMPONENT_DELETE_IN_PROGRESS",
    "STUDIO_COMPONENT_UPDATED",
    "STUDIO_COMPONENT_UPDATE_IN_PROGRESS",
]
StudioComponentSubtypeType = Literal[
    "AMAZON_FSX_FOR_LUSTRE", "AMAZON_FSX_FOR_WINDOWS", "AWS_MANAGED_MICROSOFT_AD", "CUSTOM"
]
StudioComponentTypeType = Literal[
    "ACTIVE_DIRECTORY", "COMPUTE_FARM", "CUSTOM", "LICENSE_SERVICE", "SHARED_FILE_SYSTEM"
]
StudioEncryptionConfigurationKeyTypeType = Literal["AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY"]
StudioPersonaType = Literal["ADMINISTRATOR"]
StudioStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StudioStatusCodeType = Literal[
    "AWS_SSO_ACCESS_DENIED",
    "AWS_SSO_CONFIGURATION_REPAIRED",
    "AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS",
    "AWS_SSO_NOT_ENABLED",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "ROLE_COULD_NOT_BE_ASSUMED",
    "ROLE_NOT_OWNED_BY_STUDIO_OWNER",
    "STUDIO_CREATED",
    "STUDIO_CREATE_IN_PROGRESS",
    "STUDIO_DELETED",
    "STUDIO_DELETE_IN_PROGRESS",
    "STUDIO_UPDATED",
    "STUDIO_UPDATE_IN_PROGRESS",
    "STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED",
    "STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED",
    "STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED",
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
    "list_eula_acceptances",
    "list_eulas",
    "list_launch_profile_members",
    "list_launch_profiles",
    "list_streaming_images",
    "list_streaming_sessions",
    "list_studio_components",
    "list_studio_members",
    "list_studios",
]
