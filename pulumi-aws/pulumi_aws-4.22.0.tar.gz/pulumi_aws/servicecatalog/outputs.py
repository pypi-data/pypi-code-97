# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ProductProvisioningArtifactParameters',
    'ProvisionedProductProvisioningParameter',
    'ProvisionedProductStackSetProvisioningPreferences',
    'ServiceActionDefinition',
    'GetLaunchPathsSummaryResult',
    'GetLaunchPathsSummaryConstraintSummaryResult',
    'GetPortfolioConstraintsDetailResult',
]

@pulumi.output_type
class ProductProvisioningArtifactParameters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "disableTemplateValidation":
            suggest = "disable_template_validation"
        elif key == "templatePhysicalId":
            suggest = "template_physical_id"
        elif key == "templateUrl":
            suggest = "template_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProductProvisioningArtifactParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProductProvisioningArtifactParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProductProvisioningArtifactParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: Optional[str] = None,
                 disable_template_validation: Optional[bool] = None,
                 name: Optional[str] = None,
                 template_physical_id: Optional[str] = None,
                 template_url: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str description: Description of the provisioning artifact (i.e., version), including how it differs from the previous provisioning artifact.
        :param bool disable_template_validation: Whether AWS Service Catalog stops validating the specified provisioning artifact template even if it is invalid.
        :param str name: Name of the provisioning artifact (for example, `v1`, `v2beta`). No spaces are allowed.
        :param str template_physical_id: Template source as the physical ID of the resource that contains the template. Currently only supports CloudFormation stack ARN. Specify the physical ID as `arn:[partition]:cloudformation:[region]:[account ID]:stack/[stack name]/[resource ID]`.
        :param str template_url: Template source as URL of the CloudFormation template in Amazon S3.
        :param str type: Type of provisioning artifact. Valid values: `CLOUD_FORMATION_TEMPLATE`, `MARKETPLACE_AMI`, `MARKETPLACE_CAR` (Marketplace Clusters and AWS Resources).
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disable_template_validation is not None:
            pulumi.set(__self__, "disable_template_validation", disable_template_validation)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if template_physical_id is not None:
            pulumi.set(__self__, "template_physical_id", template_physical_id)
        if template_url is not None:
            pulumi.set(__self__, "template_url", template_url)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the provisioning artifact (i.e., version), including how it differs from the previous provisioning artifact.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableTemplateValidation")
    def disable_template_validation(self) -> Optional[bool]:
        """
        Whether AWS Service Catalog stops validating the specified provisioning artifact template even if it is invalid.
        """
        return pulumi.get(self, "disable_template_validation")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the provisioning artifact (for example, `v1`, `v2beta`). No spaces are allowed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="templatePhysicalId")
    def template_physical_id(self) -> Optional[str]:
        """
        Template source as the physical ID of the resource that contains the template. Currently only supports CloudFormation stack ARN. Specify the physical ID as `arn:[partition]:cloudformation:[region]:[account ID]:stack/[stack name]/[resource ID]`.
        """
        return pulumi.get(self, "template_physical_id")

    @property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[str]:
        """
        Template source as URL of the CloudFormation template in Amazon S3.
        """
        return pulumi.get(self, "template_url")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of provisioning artifact. Valid values: `CLOUD_FORMATION_TEMPLATE`, `MARKETPLACE_AMI`, `MARKETPLACE_CAR` (Marketplace Clusters and AWS Resources).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ProvisionedProductProvisioningParameter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "usePreviousValue":
            suggest = "use_previous_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProvisionedProductProvisioningParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProvisionedProductProvisioningParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProvisionedProductProvisioningParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key: str,
                 use_previous_value: Optional[bool] = None,
                 value: Optional[str] = None):
        """
        :param str key: Parameter key.
        :param bool use_previous_value: Whether to ignore `value` and keep the previous parameter value. Ignored when initially provisioning a product.
        :param str value: Parameter value.
        """
        pulumi.set(__self__, "key", key)
        if use_previous_value is not None:
            pulumi.set(__self__, "use_previous_value", use_previous_value)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Parameter key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="usePreviousValue")
    def use_previous_value(self) -> Optional[bool]:
        """
        Whether to ignore `value` and keep the previous parameter value. Ignored when initially provisioning a product.
        """
        return pulumi.get(self, "use_previous_value")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Parameter value.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ProvisionedProductStackSetProvisioningPreferences(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "failureToleranceCount":
            suggest = "failure_tolerance_count"
        elif key == "failureTolerancePercentage":
            suggest = "failure_tolerance_percentage"
        elif key == "maxConcurrencyCount":
            suggest = "max_concurrency_count"
        elif key == "maxConcurrencyPercentage":
            suggest = "max_concurrency_percentage"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProvisionedProductStackSetProvisioningPreferences. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProvisionedProductStackSetProvisioningPreferences.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProvisionedProductStackSetProvisioningPreferences.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 accounts: Optional[Sequence[str]] = None,
                 failure_tolerance_count: Optional[int] = None,
                 failure_tolerance_percentage: Optional[int] = None,
                 max_concurrency_count: Optional[int] = None,
                 max_concurrency_percentage: Optional[int] = None,
                 regions: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] accounts: One or more AWS accounts that will have access to the provisioned product. The AWS accounts specified should be within the list of accounts in the STACKSET constraint. To get the list of accounts in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all accounts from the STACKSET constraint.
        :param int failure_tolerance_count: Number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both. The default value is 0 if no value is specified.
        :param int failure_tolerance_percentage: Percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both.
        :param int max_concurrency_count: Maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `failure_tolerance_count`. `max_concurrency_count` is at most one more than the `failure_tolerance_count`. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        :param int max_concurrency_percentage: Maximum percentage of accounts in which to perform this operation at one time. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as 1 instead. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        :param Sequence[str] regions: One or more AWS Regions where the provisioned product will be available. The specified regions should be within the list of regions from the STACKSET constraint. To get the list of regions in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all regions from the STACKSET constraint.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if failure_tolerance_count is not None:
            pulumi.set(__self__, "failure_tolerance_count", failure_tolerance_count)
        if failure_tolerance_percentage is not None:
            pulumi.set(__self__, "failure_tolerance_percentage", failure_tolerance_percentage)
        if max_concurrency_count is not None:
            pulumi.set(__self__, "max_concurrency_count", max_concurrency_count)
        if max_concurrency_percentage is not None:
            pulumi.set(__self__, "max_concurrency_percentage", max_concurrency_percentage)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[str]]:
        """
        One or more AWS accounts that will have access to the provisioned product. The AWS accounts specified should be within the list of accounts in the STACKSET constraint. To get the list of accounts in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all accounts from the STACKSET constraint.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[int]:
        """
        Number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both. The default value is 0 if no value is specified.
        """
        return pulumi.get(self, "failure_tolerance_count")

    @property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[int]:
        """
        Percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both.
        """
        return pulumi.get(self, "failure_tolerance_percentage")

    @property
    @pulumi.getter(name="maxConcurrencyCount")
    def max_concurrency_count(self) -> Optional[int]:
        """
        Maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `failure_tolerance_count`. `max_concurrency_count` is at most one more than the `failure_tolerance_count`. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        """
        return pulumi.get(self, "max_concurrency_count")

    @property
    @pulumi.getter(name="maxConcurrencyPercentage")
    def max_concurrency_percentage(self) -> Optional[int]:
        """
        Maximum percentage of accounts in which to perform this operation at one time. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as 1 instead. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        """
        return pulumi.get(self, "max_concurrency_percentage")

    @property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[str]]:
        """
        One or more AWS Regions where the provisioned product will be available. The specified regions should be within the list of regions from the STACKSET constraint. To get the list of regions in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all regions from the STACKSET constraint.
        """
        return pulumi.get(self, "regions")


@pulumi.output_type
class ServiceActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "assumeRole":
            suggest = "assume_role"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 version: str,
                 assume_role: Optional[str] = None,
                 parameters: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str name: Name of the SSM document. For example, `AWS-RestartEC2Instance`. If you are using a shared SSM document, you must provide the ARN instead of the name.
        :param str version: SSM document version. For example, `1`.
        :param str assume_role: ARN of the role that performs the self-service actions on your behalf. For example, `arn:aws:iam::12345678910:role/ActionRole`. To reuse the provisioned product launch role, set to `LAUNCH_ROLE`.
        :param str parameters: List of parameters in JSON format. For example: `[{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}]` or `[{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}]`.
        :param str type: Service action definition type. Valid value is `SSM_AUTOMATION`. Default is `SSM_AUTOMATION`.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "version", version)
        if assume_role is not None:
            pulumi.set(__self__, "assume_role", assume_role)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the SSM document. For example, `AWS-RestartEC2Instance`. If you are using a shared SSM document, you must provide the ARN instead of the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        SSM document version. For example, `1`.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="assumeRole")
    def assume_role(self) -> Optional[str]:
        """
        ARN of the role that performs the self-service actions on your behalf. For example, `arn:aws:iam::12345678910:role/ActionRole`. To reuse the provisioned product launch role, set to `LAUNCH_ROLE`.
        """
        return pulumi.get(self, "assume_role")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[str]:
        """
        List of parameters in JSON format. For example: `[{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}]` or `[{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}]`.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Service action definition type. Valid value is `SSM_AUTOMATION`. Default is `SSM_AUTOMATION`.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetLaunchPathsSummaryResult(dict):
    def __init__(__self__, *,
                 constraint_summaries: Sequence['outputs.GetLaunchPathsSummaryConstraintSummaryResult'],
                 name: str,
                 path_id: str,
                 tags: Mapping[str, str]):
        """
        :param Sequence['GetLaunchPathsSummaryConstraintSummaryArgs'] constraint_summaries: Block for constraints on the portfolio-product relationship. See details below.
        :param str name: Name of the portfolio to which the path was assigned.
        :param str path_id: Identifier of the product path.
        :param Mapping[str, str] tags: Tags associated with this product path.
        """
        pulumi.set(__self__, "constraint_summaries", constraint_summaries)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "path_id", path_id)
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="constraintSummaries")
    def constraint_summaries(self) -> Sequence['outputs.GetLaunchPathsSummaryConstraintSummaryResult']:
        """
        Block for constraints on the portfolio-product relationship. See details below.
        """
        return pulumi.get(self, "constraint_summaries")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the portfolio to which the path was assigned.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pathId")
    def path_id(self) -> str:
        """
        Identifier of the product path.
        """
        return pulumi.get(self, "path_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Tags associated with this product path.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class GetLaunchPathsSummaryConstraintSummaryResult(dict):
    def __init__(__self__, *,
                 description: str,
                 type: str):
        """
        :param str description: Description of the constraint.
        :param str type: Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `STACKSET`, and `TEMPLATE`.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the constraint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `STACKSET`, and `TEMPLATE`.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetPortfolioConstraintsDetailResult(dict):
    def __init__(__self__, *,
                 constraint_id: str,
                 description: str,
                 owner: str,
                 portfolio_id: str,
                 product_id: str,
                 type: str):
        """
        :param str constraint_id: Identifier of the constraint.
        :param str description: Description of the constraint.
        :param str portfolio_id: Portfolio identifier.
        :param str product_id: Product identifier.
        :param str type: Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `STACKSET`, and `TEMPLATE`.
        """
        pulumi.set(__self__, "constraint_id", constraint_id)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "portfolio_id", portfolio_id)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="constraintId")
    def constraint_id(self) -> str:
        """
        Identifier of the constraint.
        """
        return pulumi.get(self, "constraint_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the constraint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> str:
        """
        Portfolio identifier.
        """
        return pulumi.get(self, "portfolio_id")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        Product identifier.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `STACKSET`, and `TEMPLATE`.
        """
        return pulumi.get(self, "type")


