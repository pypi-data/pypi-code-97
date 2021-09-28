"""
Type annotations for elbv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/literals.html)

Usage::

    ```python
    from mypy_boto3_elbv2.literals import ActionTypeEnumType

    data: ActionTypeEnumType = "authenticate-cognito"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionTypeEnumType",
    "AuthenticateCognitoActionConditionalBehaviorEnumType",
    "AuthenticateOidcActionConditionalBehaviorEnumType",
    "DescribeAccountLimitsPaginatorName",
    "DescribeListenerCertificatesPaginatorName",
    "DescribeListenersPaginatorName",
    "DescribeLoadBalancersPaginatorName",
    "DescribeRulesPaginatorName",
    "DescribeSSLPoliciesPaginatorName",
    "DescribeTargetGroupsPaginatorName",
    "IpAddressTypeType",
    "LoadBalancerAvailableWaiterName",
    "LoadBalancerExistsWaiterName",
    "LoadBalancerSchemeEnumType",
    "LoadBalancerStateEnumType",
    "LoadBalancerTypeEnumType",
    "LoadBalancersDeletedWaiterName",
    "ProtocolEnumType",
    "RedirectActionStatusCodeEnumType",
    "TargetDeregisteredWaiterName",
    "TargetHealthReasonEnumType",
    "TargetHealthStateEnumType",
    "TargetInServiceWaiterName",
    "TargetTypeEnumType",
    "ServiceName",
    "PaginatorName",
    "WaiterName",
)


ActionTypeEnumType = Literal[
    "authenticate-cognito", "authenticate-oidc", "fixed-response", "forward", "redirect"
]
AuthenticateCognitoActionConditionalBehaviorEnumType = Literal["allow", "authenticate", "deny"]
AuthenticateOidcActionConditionalBehaviorEnumType = Literal["allow", "authenticate", "deny"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeListenerCertificatesPaginatorName = Literal["describe_listener_certificates"]
DescribeListenersPaginatorName = Literal["describe_listeners"]
DescribeLoadBalancersPaginatorName = Literal["describe_load_balancers"]
DescribeRulesPaginatorName = Literal["describe_rules"]
DescribeSSLPoliciesPaginatorName = Literal["describe_ssl_policies"]
DescribeTargetGroupsPaginatorName = Literal["describe_target_groups"]
IpAddressTypeType = Literal["dualstack", "ipv4"]
LoadBalancerAvailableWaiterName = Literal["load_balancer_available"]
LoadBalancerExistsWaiterName = Literal["load_balancer_exists"]
LoadBalancerSchemeEnumType = Literal["internal", "internet-facing"]
LoadBalancerStateEnumType = Literal["active", "active_impaired", "failed", "provisioning"]
LoadBalancerTypeEnumType = Literal["application", "gateway", "network"]
LoadBalancersDeletedWaiterName = Literal["load_balancers_deleted"]
ProtocolEnumType = Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
RedirectActionStatusCodeEnumType = Literal["HTTP_301", "HTTP_302"]
TargetDeregisteredWaiterName = Literal["target_deregistered"]
TargetHealthReasonEnumType = Literal[
    "Elb.InitialHealthChecking",
    "Elb.InternalError",
    "Elb.RegistrationInProgress",
    "Target.DeregistrationInProgress",
    "Target.FailedHealthChecks",
    "Target.HealthCheckDisabled",
    "Target.InvalidState",
    "Target.IpUnusable",
    "Target.NotInUse",
    "Target.NotRegistered",
    "Target.ResponseCodeMismatch",
    "Target.Timeout",
]
TargetHealthStateEnumType = Literal[
    "draining", "healthy", "initial", "unavailable", "unhealthy", "unused"
]
TargetInServiceWaiterName = Literal["target_in_service"]
TargetTypeEnumType = Literal["alb", "instance", "ip", "lambda"]
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
    "describe_account_limits",
    "describe_listener_certificates",
    "describe_listeners",
    "describe_load_balancers",
    "describe_rules",
    "describe_ssl_policies",
    "describe_target_groups",
]
WaiterName = Literal[
    "load_balancer_available",
    "load_balancer_exists",
    "load_balancers_deleted",
    "target_deregistered",
    "target_in_service",
]
