"""
Type annotations for lambda service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/literals.html)

Usage::

    ```python
    from mypy_boto3_lambda.literals import CodeSigningPolicyType

    data: CodeSigningPolicyType = "Enforce"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CodeSigningPolicyType",
    "EndPointTypeType",
    "EventSourcePositionType",
    "FunctionActiveWaiterName",
    "FunctionExistsWaiterName",
    "FunctionResponseTypeType",
    "FunctionUpdatedWaiterName",
    "FunctionVersionType",
    "InvocationTypeType",
    "LastUpdateStatusReasonCodeType",
    "LastUpdateStatusType",
    "ListAliasesPaginatorName",
    "ListCodeSigningConfigsPaginatorName",
    "ListEventSourceMappingsPaginatorName",
    "ListFunctionEventInvokeConfigsPaginatorName",
    "ListFunctionsByCodeSigningConfigPaginatorName",
    "ListFunctionsPaginatorName",
    "ListLayerVersionsPaginatorName",
    "ListLayersPaginatorName",
    "ListProvisionedConcurrencyConfigsPaginatorName",
    "ListVersionsByFunctionPaginatorName",
    "LogTypeType",
    "PackageTypeType",
    "ProvisionedConcurrencyStatusEnumType",
    "RuntimeType",
    "SourceAccessTypeType",
    "StateReasonCodeType",
    "StateType",
    "TracingModeType",
    "ServiceName",
    "PaginatorName",
    "WaiterName",
)


CodeSigningPolicyType = Literal["Enforce", "Warn"]
EndPointTypeType = Literal["KAFKA_BOOTSTRAP_SERVERS"]
EventSourcePositionType = Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
FunctionActiveWaiterName = Literal["function_active"]
FunctionExistsWaiterName = Literal["function_exists"]
FunctionResponseTypeType = Literal["ReportBatchItemFailures"]
FunctionUpdatedWaiterName = Literal["function_updated"]
FunctionVersionType = Literal["ALL"]
InvocationTypeType = Literal["DryRun", "Event", "RequestResponse"]
LastUpdateStatusReasonCodeType = Literal[
    "EniLimitExceeded",
    "ImageAccessDenied",
    "ImageDeleted",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidConfiguration",
    "InvalidImage",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "SubnetOutOfIPAddresses",
]
LastUpdateStatusType = Literal["Failed", "InProgress", "Successful"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListCodeSigningConfigsPaginatorName = Literal["list_code_signing_configs"]
ListEventSourceMappingsPaginatorName = Literal["list_event_source_mappings"]
ListFunctionEventInvokeConfigsPaginatorName = Literal["list_function_event_invoke_configs"]
ListFunctionsByCodeSigningConfigPaginatorName = Literal["list_functions_by_code_signing_config"]
ListFunctionsPaginatorName = Literal["list_functions"]
ListLayerVersionsPaginatorName = Literal["list_layer_versions"]
ListLayersPaginatorName = Literal["list_layers"]
ListProvisionedConcurrencyConfigsPaginatorName = Literal["list_provisioned_concurrency_configs"]
ListVersionsByFunctionPaginatorName = Literal["list_versions_by_function"]
LogTypeType = Literal["None", "Tail"]
PackageTypeType = Literal["Image", "Zip"]
ProvisionedConcurrencyStatusEnumType = Literal["FAILED", "IN_PROGRESS", "READY"]
RuntimeType = Literal[
    "dotnetcore1.0",
    "dotnetcore2.0",
    "dotnetcore2.1",
    "dotnetcore3.1",
    "go1.x",
    "java11",
    "java8",
    "java8.al2",
    "nodejs",
    "nodejs10.x",
    "nodejs12.x",
    "nodejs14.x",
    "nodejs4.3",
    "nodejs4.3-edge",
    "nodejs6.10",
    "nodejs8.10",
    "provided",
    "provided.al2",
    "python2.7",
    "python3.6",
    "python3.7",
    "python3.8",
    "python3.9",
    "ruby2.5",
    "ruby2.7",
]
SourceAccessTypeType = Literal[
    "BASIC_AUTH",
    "SASL_SCRAM_256_AUTH",
    "SASL_SCRAM_512_AUTH",
    "VIRTUAL_HOST",
    "VPC_SECURITY_GROUP",
    "VPC_SUBNET",
]
StateReasonCodeType = Literal[
    "Creating",
    "EniLimitExceeded",
    "Idle",
    "ImageAccessDenied",
    "ImageDeleted",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidConfiguration",
    "InvalidImage",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "Restoring",
    "SubnetOutOfIPAddresses",
]
StateType = Literal["Active", "Failed", "Inactive", "Pending"]
TracingModeType = Literal["Active", "PassThrough"]
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
    "list_aliases",
    "list_code_signing_configs",
    "list_event_source_mappings",
    "list_function_event_invoke_configs",
    "list_functions",
    "list_functions_by_code_signing_config",
    "list_layer_versions",
    "list_layers",
    "list_provisioned_concurrency_configs",
    "list_versions_by_function",
]
WaiterName = Literal["function_active", "function_exists", "function_updated"]
