"""
Type annotations for cloudfront service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudfront.literals import CachePolicyCookieBehaviorType

    data: CachePolicyCookieBehaviorType = "all"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CachePolicyCookieBehaviorType",
    "CachePolicyHeaderBehaviorType",
    "CachePolicyQueryStringBehaviorType",
    "CachePolicyTypeType",
    "CertificateSourceType",
    "DistributionDeployedWaiterName",
    "EventTypeType",
    "FormatType",
    "FunctionRuntimeType",
    "FunctionStageType",
    "GeoRestrictionTypeType",
    "HttpVersionType",
    "ICPRecordalStatusType",
    "InvalidationCompletedWaiterName",
    "ItemSelectionType",
    "ListCloudFrontOriginAccessIdentitiesPaginatorName",
    "ListDistributionsPaginatorName",
    "ListInvalidationsPaginatorName",
    "ListStreamingDistributionsPaginatorName",
    "MethodType",
    "MinimumProtocolVersionType",
    "OriginProtocolPolicyType",
    "OriginRequestPolicyCookieBehaviorType",
    "OriginRequestPolicyHeaderBehaviorType",
    "OriginRequestPolicyQueryStringBehaviorType",
    "OriginRequestPolicyTypeType",
    "PriceClassType",
    "RealtimeMetricsSubscriptionStatusType",
    "SSLSupportMethodType",
    "SslProtocolType",
    "StreamingDistributionDeployedWaiterName",
    "ViewerProtocolPolicyType",
    "ServiceName",
    "PaginatorName",
    "WaiterName",
)


CachePolicyCookieBehaviorType = Literal["all", "allExcept", "none", "whitelist"]
CachePolicyHeaderBehaviorType = Literal["none", "whitelist"]
CachePolicyQueryStringBehaviorType = Literal["all", "allExcept", "none", "whitelist"]
CachePolicyTypeType = Literal["custom", "managed"]
CertificateSourceType = Literal["acm", "cloudfront", "iam"]
DistributionDeployedWaiterName = Literal["distribution_deployed"]
EventTypeType = Literal["origin-request", "origin-response", "viewer-request", "viewer-response"]
FormatType = Literal["URLEncoded"]
FunctionRuntimeType = Literal["cloudfront-js-1.0"]
FunctionStageType = Literal["DEVELOPMENT", "LIVE"]
GeoRestrictionTypeType = Literal["blacklist", "none", "whitelist"]
HttpVersionType = Literal["http1.1", "http2"]
ICPRecordalStatusType = Literal["APPROVED", "PENDING", "SUSPENDED"]
InvalidationCompletedWaiterName = Literal["invalidation_completed"]
ItemSelectionType = Literal["all", "none", "whitelist"]
ListCloudFrontOriginAccessIdentitiesPaginatorName = Literal[
    "list_cloud_front_origin_access_identities"
]
ListDistributionsPaginatorName = Literal["list_distributions"]
ListInvalidationsPaginatorName = Literal["list_invalidations"]
ListStreamingDistributionsPaginatorName = Literal["list_streaming_distributions"]
MethodType = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
MinimumProtocolVersionType = Literal[
    "SSLv3", "TLSv1", "TLSv1.1_2016", "TLSv1.2_2018", "TLSv1.2_2019", "TLSv1.2_2021", "TLSv1_2016"
]
OriginProtocolPolicyType = Literal["http-only", "https-only", "match-viewer"]
OriginRequestPolicyCookieBehaviorType = Literal["all", "none", "whitelist"]
OriginRequestPolicyHeaderBehaviorType = Literal[
    "allViewer", "allViewerAndWhitelistCloudFront", "none", "whitelist"
]
OriginRequestPolicyQueryStringBehaviorType = Literal["all", "none", "whitelist"]
OriginRequestPolicyTypeType = Literal["custom", "managed"]
PriceClassType = Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"]
RealtimeMetricsSubscriptionStatusType = Literal["Disabled", "Enabled"]
SSLSupportMethodType = Literal["sni-only", "static-ip", "vip"]
SslProtocolType = Literal["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]
StreamingDistributionDeployedWaiterName = Literal["streaming_distribution_deployed"]
ViewerProtocolPolicyType = Literal["allow-all", "https-only", "redirect-to-https"]
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
    "list_cloud_front_origin_access_identities",
    "list_distributions",
    "list_invalidations",
    "list_streaming_distributions",
]
WaiterName = Literal[
    "distribution_deployed", "invalidation_completed", "streaming_distribution_deployed"
]
