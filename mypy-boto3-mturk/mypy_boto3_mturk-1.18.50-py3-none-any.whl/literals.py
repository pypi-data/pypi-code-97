"""
Type annotations for mturk service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/literals.html)

Usage::

    ```python
    from mypy_boto3_mturk.literals import AssignmentStatusType

    data: AssignmentStatusType = "Approved"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AssignmentStatusType",
    "ComparatorType",
    "EventTypeType",
    "HITAccessActionsType",
    "HITReviewStatusType",
    "HITStatusType",
    "ListAssignmentsForHITPaginatorName",
    "ListBonusPaymentsPaginatorName",
    "ListHITsForQualificationTypePaginatorName",
    "ListHITsPaginatorName",
    "ListQualificationRequestsPaginatorName",
    "ListQualificationTypesPaginatorName",
    "ListReviewableHITsPaginatorName",
    "ListWorkerBlocksPaginatorName",
    "ListWorkersWithQualificationTypePaginatorName",
    "NotificationTransportType",
    "NotifyWorkersFailureCodeType",
    "QualificationStatusType",
    "QualificationTypeStatusType",
    "ReviewActionStatusType",
    "ReviewPolicyLevelType",
    "ReviewableHITStatusType",
    "ServiceName",
    "PaginatorName",
)


AssignmentStatusType = Literal["Approved", "Rejected", "Submitted"]
ComparatorType = Literal[
    "DoesNotExist",
    "EqualTo",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "In",
    "LessThan",
    "LessThanOrEqualTo",
    "NotEqualTo",
    "NotIn",
]
EventTypeType = Literal[
    "AssignmentAbandoned",
    "AssignmentAccepted",
    "AssignmentApproved",
    "AssignmentRejected",
    "AssignmentReturned",
    "AssignmentSubmitted",
    "HITCreated",
    "HITDisposed",
    "HITExpired",
    "HITExtended",
    "HITReviewable",
    "Ping",
]
HITAccessActionsType = Literal["Accept", "DiscoverPreviewAndAccept", "PreviewAndAccept"]
HITReviewStatusType = Literal[
    "MarkedForReview", "NotReviewed", "ReviewedAppropriate", "ReviewedInappropriate"
]
HITStatusType = Literal["Assignable", "Disposed", "Reviewable", "Reviewing", "Unassignable"]
ListAssignmentsForHITPaginatorName = Literal["list_assignments_for_hit"]
ListBonusPaymentsPaginatorName = Literal["list_bonus_payments"]
ListHITsForQualificationTypePaginatorName = Literal["list_hits_for_qualification_type"]
ListHITsPaginatorName = Literal["list_hits"]
ListQualificationRequestsPaginatorName = Literal["list_qualification_requests"]
ListQualificationTypesPaginatorName = Literal["list_qualification_types"]
ListReviewableHITsPaginatorName = Literal["list_reviewable_hits"]
ListWorkerBlocksPaginatorName = Literal["list_worker_blocks"]
ListWorkersWithQualificationTypePaginatorName = Literal["list_workers_with_qualification_type"]
NotificationTransportType = Literal["Email", "SNS", "SQS"]
NotifyWorkersFailureCodeType = Literal["HardFailure", "SoftFailure"]
QualificationStatusType = Literal["Granted", "Revoked"]
QualificationTypeStatusType = Literal["Active", "Inactive"]
ReviewActionStatusType = Literal["Cancelled", "Failed", "Intended", "Succeeded"]
ReviewPolicyLevelType = Literal["Assignment", "HIT"]
ReviewableHITStatusType = Literal["Reviewable", "Reviewing"]
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
    "list_assignments_for_hit",
    "list_bonus_payments",
    "list_hits",
    "list_hits_for_qualification_type",
    "list_qualification_requests",
    "list_qualification_types",
    "list_reviewable_hits",
    "list_worker_blocks",
    "list_workers_with_qualification_type",
]
