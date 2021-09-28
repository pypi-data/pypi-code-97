"""
Type annotations for apigateway service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/literals.html)

Usage::

    ```python
    from mypy_boto3_apigateway.literals import ApiKeySourceTypeType

    data: ApiKeySourceTypeType = "AUTHORIZER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApiKeySourceTypeType",
    "ApiKeysFormatType",
    "AuthorizerTypeType",
    "CacheClusterSizeType",
    "CacheClusterStatusType",
    "ConnectionTypeType",
    "ContentHandlingStrategyType",
    "DocumentationPartTypeType",
    "DomainNameStatusType",
    "EndpointTypeType",
    "GatewayResponseTypeType",
    "GetApiKeysPaginatorName",
    "GetAuthorizersPaginatorName",
    "GetBasePathMappingsPaginatorName",
    "GetClientCertificatesPaginatorName",
    "GetDeploymentsPaginatorName",
    "GetDocumentationPartsPaginatorName",
    "GetDocumentationVersionsPaginatorName",
    "GetDomainNamesPaginatorName",
    "GetGatewayResponsesPaginatorName",
    "GetModelsPaginatorName",
    "GetRequestValidatorsPaginatorName",
    "GetResourcesPaginatorName",
    "GetRestApisPaginatorName",
    "GetSdkTypesPaginatorName",
    "GetUsagePaginatorName",
    "GetUsagePlanKeysPaginatorName",
    "GetUsagePlansPaginatorName",
    "GetVpcLinksPaginatorName",
    "IntegrationTypeType",
    "LocationStatusTypeType",
    "OpType",
    "PutModeType",
    "QuotaPeriodTypeType",
    "SecurityPolicyType",
    "UnauthorizedCacheControlHeaderStrategyType",
    "VpcLinkStatusType",
    "ServiceName",
    "PaginatorName",
)


ApiKeySourceTypeType = Literal["AUTHORIZER", "HEADER"]
ApiKeysFormatType = Literal["csv"]
AuthorizerTypeType = Literal["COGNITO_USER_POOLS", "REQUEST", "TOKEN"]
CacheClusterSizeType = Literal["0.5", "1.6", "118", "13.5", "237", "28.4", "58.2", "6.1"]
CacheClusterStatusType = Literal[
    "AVAILABLE", "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "FLUSH_IN_PROGRESS", "NOT_AVAILABLE"
]
ConnectionTypeType = Literal["INTERNET", "VPC_LINK"]
ContentHandlingStrategyType = Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
DocumentationPartTypeType = Literal[
    "API",
    "AUTHORIZER",
    "METHOD",
    "MODEL",
    "PATH_PARAMETER",
    "QUERY_PARAMETER",
    "REQUEST_BODY",
    "REQUEST_HEADER",
    "RESOURCE",
    "RESPONSE",
    "RESPONSE_BODY",
    "RESPONSE_HEADER",
]
DomainNameStatusType = Literal[
    "AVAILABLE",
    "PENDING",
    "PENDING_CERTIFICATE_REIMPORT",
    "PENDING_OWNERSHIP_VERIFICATION",
    "UPDATING",
]
EndpointTypeType = Literal["EDGE", "PRIVATE", "REGIONAL"]
GatewayResponseTypeType = Literal[
    "ACCESS_DENIED",
    "API_CONFIGURATION_ERROR",
    "AUTHORIZER_CONFIGURATION_ERROR",
    "AUTHORIZER_FAILURE",
    "BAD_REQUEST_BODY",
    "BAD_REQUEST_PARAMETERS",
    "DEFAULT_4XX",
    "DEFAULT_5XX",
    "EXPIRED_TOKEN",
    "INTEGRATION_FAILURE",
    "INTEGRATION_TIMEOUT",
    "INVALID_API_KEY",
    "INVALID_SIGNATURE",
    "MISSING_AUTHENTICATION_TOKEN",
    "QUOTA_EXCEEDED",
    "REQUEST_TOO_LARGE",
    "RESOURCE_NOT_FOUND",
    "THROTTLED",
    "UNAUTHORIZED",
    "UNSUPPORTED_MEDIA_TYPE",
    "WAF_FILTERED",
]
GetApiKeysPaginatorName = Literal["get_api_keys"]
GetAuthorizersPaginatorName = Literal["get_authorizers"]
GetBasePathMappingsPaginatorName = Literal["get_base_path_mappings"]
GetClientCertificatesPaginatorName = Literal["get_client_certificates"]
GetDeploymentsPaginatorName = Literal["get_deployments"]
GetDocumentationPartsPaginatorName = Literal["get_documentation_parts"]
GetDocumentationVersionsPaginatorName = Literal["get_documentation_versions"]
GetDomainNamesPaginatorName = Literal["get_domain_names"]
GetGatewayResponsesPaginatorName = Literal["get_gateway_responses"]
GetModelsPaginatorName = Literal["get_models"]
GetRequestValidatorsPaginatorName = Literal["get_request_validators"]
GetResourcesPaginatorName = Literal["get_resources"]
GetRestApisPaginatorName = Literal["get_rest_apis"]
GetSdkTypesPaginatorName = Literal["get_sdk_types"]
GetUsagePaginatorName = Literal["get_usage"]
GetUsagePlanKeysPaginatorName = Literal["get_usage_plan_keys"]
GetUsagePlansPaginatorName = Literal["get_usage_plans"]
GetVpcLinksPaginatorName = Literal["get_vpc_links"]
IntegrationTypeType = Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
LocationStatusTypeType = Literal["DOCUMENTED", "UNDOCUMENTED"]
OpType = Literal["add", "copy", "move", "remove", "replace", "test"]
PutModeType = Literal["merge", "overwrite"]
QuotaPeriodTypeType = Literal["DAY", "MONTH", "WEEK"]
SecurityPolicyType = Literal["TLS_1_0", "TLS_1_2"]
UnauthorizedCacheControlHeaderStrategyType = Literal[
    "FAIL_WITH_403", "SUCCEED_WITHOUT_RESPONSE_HEADER", "SUCCEED_WITH_RESPONSE_HEADER"
]
VpcLinkStatusType = Literal["AVAILABLE", "DELETING", "FAILED", "PENDING"]
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
    "get_api_keys",
    "get_authorizers",
    "get_base_path_mappings",
    "get_client_certificates",
    "get_deployments",
    "get_documentation_parts",
    "get_documentation_versions",
    "get_domain_names",
    "get_gateway_responses",
    "get_models",
    "get_request_validators",
    "get_resources",
    "get_rest_apis",
    "get_sdk_types",
    "get_usage",
    "get_usage_plan_keys",
    "get_usage_plans",
    "get_vpc_links",
]
