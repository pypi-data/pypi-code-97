"""
Type annotations for lex-models service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/literals.html)

Usage::

    ```python
    from mypy_boto3_lex_models.literals import ChannelStatusType

    data: ChannelStatusType = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ChannelStatusType",
    "ChannelTypeType",
    "ContentTypeType",
    "DestinationType",
    "ExportStatusType",
    "ExportTypeType",
    "FulfillmentActivityTypeType",
    "GetBotAliasesPaginatorName",
    "GetBotChannelAssociationsPaginatorName",
    "GetBotVersionsPaginatorName",
    "GetBotsPaginatorName",
    "GetBuiltinIntentsPaginatorName",
    "GetBuiltinSlotTypesPaginatorName",
    "GetIntentVersionsPaginatorName",
    "GetIntentsPaginatorName",
    "GetSlotTypeVersionsPaginatorName",
    "GetSlotTypesPaginatorName",
    "ImportStatusType",
    "LocaleType",
    "LogTypeType",
    "MergeStrategyType",
    "MigrationAlertTypeType",
    "MigrationSortAttributeType",
    "MigrationStatusType",
    "MigrationStrategyType",
    "ObfuscationSettingType",
    "ProcessBehaviorType",
    "ResourceTypeType",
    "SlotConstraintType",
    "SlotValueSelectionStrategyType",
    "SortOrderType",
    "StatusType",
    "StatusTypeType",
    "ServiceName",
    "PaginatorName",
)


ChannelStatusType = Literal["CREATED", "FAILED", "IN_PROGRESS"]
ChannelTypeType = Literal["Facebook", "Kik", "Slack", "Twilio-Sms"]
ContentTypeType = Literal["CustomPayload", "PlainText", "SSML"]
DestinationType = Literal["CLOUDWATCH_LOGS", "S3"]
ExportStatusType = Literal["FAILED", "IN_PROGRESS", "READY"]
ExportTypeType = Literal["ALEXA_SKILLS_KIT", "LEX"]
FulfillmentActivityTypeType = Literal["CodeHook", "ReturnIntent"]
GetBotAliasesPaginatorName = Literal["get_bot_aliases"]
GetBotChannelAssociationsPaginatorName = Literal["get_bot_channel_associations"]
GetBotVersionsPaginatorName = Literal["get_bot_versions"]
GetBotsPaginatorName = Literal["get_bots"]
GetBuiltinIntentsPaginatorName = Literal["get_builtin_intents"]
GetBuiltinSlotTypesPaginatorName = Literal["get_builtin_slot_types"]
GetIntentVersionsPaginatorName = Literal["get_intent_versions"]
GetIntentsPaginatorName = Literal["get_intents"]
GetSlotTypeVersionsPaginatorName = Literal["get_slot_type_versions"]
GetSlotTypesPaginatorName = Literal["get_slot_types"]
ImportStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
LocaleType = Literal[
    "de-DE",
    "en-AU",
    "en-GB",
    "en-IN",
    "en-US",
    "es-419",
    "es-ES",
    "es-US",
    "fr-CA",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "ko-KR",
]
LogTypeType = Literal["AUDIO", "TEXT"]
MergeStrategyType = Literal["FAIL_ON_CONFLICT", "OVERWRITE_LATEST"]
MigrationAlertTypeType = Literal["ERROR", "WARN"]
MigrationSortAttributeType = Literal["MIGRATION_DATE_TIME", "V1_BOT_NAME"]
MigrationStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
MigrationStrategyType = Literal["CREATE_NEW", "UPDATE_EXISTING"]
ObfuscationSettingType = Literal["DEFAULT_OBFUSCATION", "NONE"]
ProcessBehaviorType = Literal["BUILD", "SAVE"]
ResourceTypeType = Literal["BOT", "INTENT", "SLOT_TYPE"]
SlotConstraintType = Literal["Optional", "Required"]
SlotValueSelectionStrategyType = Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StatusType = Literal["BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"]
StatusTypeType = Literal["Detected", "Missed"]
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
    "get_bot_aliases",
    "get_bot_channel_associations",
    "get_bot_versions",
    "get_bots",
    "get_builtin_intents",
    "get_builtin_slot_types",
    "get_intent_versions",
    "get_intents",
    "get_slot_type_versions",
    "get_slot_types",
]
