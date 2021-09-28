# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OrganizationArgs', 'Organization']

@pulumi.input_type
class OrganizationArgs:
    def __init__(__self__, *,
                 aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feature_set: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Organization resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aws_service_access_principals: List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_policy_types: List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        :param pulumi.Input[str] feature_set: Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        """
        if aws_service_access_principals is not None:
            pulumi.set(__self__, "aws_service_access_principals", aws_service_access_principals)
        if enabled_policy_types is not None:
            pulumi.set(__self__, "enabled_policy_types", enabled_policy_types)
        if feature_set is not None:
            pulumi.set(__self__, "feature_set", feature_set)

    @property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        """
        return pulumi.get(self, "aws_service_access_principals")

    @aws_service_access_principals.setter
    def aws_service_access_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aws_service_access_principals", value)

    @property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        """
        return pulumi.get(self, "enabled_policy_types")

    @enabled_policy_types.setter
    def enabled_policy_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_policy_types", value)

    @property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> Optional[pulumi.Input[str]]:
        """
        Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        """
        return pulumi.get(self, "feature_set")

    @feature_set.setter
    def feature_set(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature_set", value)


@pulumi.input_type
class _OrganizationState:
    def __init__(__self__, *,
                 accounts: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgs']]]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feature_set: Optional[pulumi.Input[str]] = None,
                 master_account_arn: Optional[pulumi.Input[str]] = None,
                 master_account_email: Optional[pulumi.Input[str]] = None,
                 master_account_id: Optional[pulumi.Input[str]] = None,
                 non_master_accounts: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationNonMasterAccountArgs']]]] = None,
                 roots: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationRootArgs']]]] = None):
        """
        Input properties used for looking up and filtering Organization resources.
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgs']]] accounts: List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
        :param pulumi.Input[str] arn: ARN of the root
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aws_service_access_principals: List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_policy_types: List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        :param pulumi.Input[str] feature_set: Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        :param pulumi.Input[str] master_account_arn: ARN of the master account
        :param pulumi.Input[str] master_account_email: Email address of the master account
        :param pulumi.Input[str] master_account_id: Identifier of the master account
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationNonMasterAccountArgs']]] non_master_accounts: List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationRootArgs']]] roots: List of organization roots. All elements have these attributes:
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if aws_service_access_principals is not None:
            pulumi.set(__self__, "aws_service_access_principals", aws_service_access_principals)
        if enabled_policy_types is not None:
            pulumi.set(__self__, "enabled_policy_types", enabled_policy_types)
        if feature_set is not None:
            pulumi.set(__self__, "feature_set", feature_set)
        if master_account_arn is not None:
            pulumi.set(__self__, "master_account_arn", master_account_arn)
        if master_account_email is not None:
            pulumi.set(__self__, "master_account_email", master_account_email)
        if master_account_id is not None:
            pulumi.set(__self__, "master_account_id", master_account_id)
        if non_master_accounts is not None:
            pulumi.set(__self__, "non_master_accounts", non_master_accounts)
        if roots is not None:
            pulumi.set(__self__, "roots", roots)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgs']]]]:
        """
        List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
        """
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgs']]]]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        """
        return pulumi.get(self, "aws_service_access_principals")

    @aws_service_access_principals.setter
    def aws_service_access_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aws_service_access_principals", value)

    @property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        """
        return pulumi.get(self, "enabled_policy_types")

    @enabled_policy_types.setter
    def enabled_policy_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_policy_types", value)

    @property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> Optional[pulumi.Input[str]]:
        """
        Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        """
        return pulumi.get(self, "feature_set")

    @feature_set.setter
    def feature_set(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature_set", value)

    @property
    @pulumi.getter(name="masterAccountArn")
    def master_account_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the master account
        """
        return pulumi.get(self, "master_account_arn")

    @master_account_arn.setter
    def master_account_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_account_arn", value)

    @property
    @pulumi.getter(name="masterAccountEmail")
    def master_account_email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the master account
        """
        return pulumi.get(self, "master_account_email")

    @master_account_email.setter
    def master_account_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_account_email", value)

    @property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the master account
        """
        return pulumi.get(self, "master_account_id")

    @master_account_id.setter
    def master_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_account_id", value)

    @property
    @pulumi.getter(name="nonMasterAccounts")
    def non_master_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationNonMasterAccountArgs']]]]:
        """
        List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
        """
        return pulumi.get(self, "non_master_accounts")

    @non_master_accounts.setter
    def non_master_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationNonMasterAccountArgs']]]]):
        pulumi.set(self, "non_master_accounts", value)

    @property
    @pulumi.getter
    def roots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationRootArgs']]]]:
        """
        List of organization roots. All elements have these attributes:
        """
        return pulumi.get(self, "roots")

    @roots.setter
    def roots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationRootArgs']]]]):
        pulumi.set(self, "roots", value)


class Organization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feature_set: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create an organization.

        !> **WARNING:** When migrating from a `feature_set` of `CONSOLIDATED_BILLING` to `ALL`, the Organization account owner will received an email stating the following: "You started the process to enable all features for your AWS organization. As part of that process, all member accounts that joined your organization by invitation must approve the change. You don’t need approval from member accounts that you directly created from within your AWS organization." After all member accounts have accepted the invitation, the Organization account owner must then finalize the changes via the [AWS Console](https://console.aws.amazon.com/organizations/home#/organization/settings/migration-progress). Until these steps are performed, the provider will perpetually show a difference, and the `DescribeOrganization` API will continue to show the `FeatureSet` as `CONSOLIDATED_BILLING`. See the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) for more information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        org = aws.organizations.Organization("org",
            aws_service_access_principals=[
                "cloudtrail.amazonaws.com",
                "config.amazonaws.com",
            ],
            feature_set="ALL")
        ```

        ## Import

        The AWS organization can be imported by using the `id`, e.g.

        ```sh
         $ pulumi import aws:organizations/organization:Organization my_org o-1234567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aws_service_access_principals: List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_policy_types: List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        :param pulumi.Input[str] feature_set: Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OrganizationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create an organization.

        !> **WARNING:** When migrating from a `feature_set` of `CONSOLIDATED_BILLING` to `ALL`, the Organization account owner will received an email stating the following: "You started the process to enable all features for your AWS organization. As part of that process, all member accounts that joined your organization by invitation must approve the change. You don’t need approval from member accounts that you directly created from within your AWS organization." After all member accounts have accepted the invitation, the Organization account owner must then finalize the changes via the [AWS Console](https://console.aws.amazon.com/organizations/home#/organization/settings/migration-progress). Until these steps are performed, the provider will perpetually show a difference, and the `DescribeOrganization` API will continue to show the `FeatureSet` as `CONSOLIDATED_BILLING`. See the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) for more information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        org = aws.organizations.Organization("org",
            aws_service_access_principals=[
                "cloudtrail.amazonaws.com",
                "config.amazonaws.com",
            ],
            feature_set="ALL")
        ```

        ## Import

        The AWS organization can be imported by using the `id`, e.g.

        ```sh
         $ pulumi import aws:organizations/organization:Organization my_org o-1234567
        ```

        :param str resource_name: The name of the resource.
        :param OrganizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feature_set: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationArgs.__new__(OrganizationArgs)

            __props__.__dict__["aws_service_access_principals"] = aws_service_access_principals
            __props__.__dict__["enabled_policy_types"] = enabled_policy_types
            __props__.__dict__["feature_set"] = feature_set
            __props__.__dict__["accounts"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["master_account_arn"] = None
            __props__.__dict__["master_account_email"] = None
            __props__.__dict__["master_account_id"] = None
            __props__.__dict__["non_master_accounts"] = None
            __props__.__dict__["roots"] = None
        super(Organization, __self__).__init__(
            'aws:organizations/organization:Organization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationAccountArgs']]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            feature_set: Optional[pulumi.Input[str]] = None,
            master_account_arn: Optional[pulumi.Input[str]] = None,
            master_account_email: Optional[pulumi.Input[str]] = None,
            master_account_id: Optional[pulumi.Input[str]] = None,
            non_master_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationNonMasterAccountArgs']]]]] = None,
            roots: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationRootArgs']]]]] = None) -> 'Organization':
        """
        Get an existing Organization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationAccountArgs']]]] accounts: List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
        :param pulumi.Input[str] arn: ARN of the root
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aws_service_access_principals: List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_policy_types: List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        :param pulumi.Input[str] feature_set: Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        :param pulumi.Input[str] master_account_arn: ARN of the master account
        :param pulumi.Input[str] master_account_email: Email address of the master account
        :param pulumi.Input[str] master_account_id: Identifier of the master account
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationNonMasterAccountArgs']]]] non_master_accounts: List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationRootArgs']]]] roots: List of organization roots. All elements have these attributes:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrganizationState.__new__(_OrganizationState)

        __props__.__dict__["accounts"] = accounts
        __props__.__dict__["arn"] = arn
        __props__.__dict__["aws_service_access_principals"] = aws_service_access_principals
        __props__.__dict__["enabled_policy_types"] = enabled_policy_types
        __props__.__dict__["feature_set"] = feature_set
        __props__.__dict__["master_account_arn"] = master_account_arn
        __props__.__dict__["master_account_email"] = master_account_email
        __props__.__dict__["master_account_id"] = master_account_id
        __props__.__dict__["non_master_accounts"] = non_master_accounts
        __props__.__dict__["roots"] = roots
        return Organization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accounts(self) -> pulumi.Output[Sequence['outputs.OrganizationAccount']]:
        """
        List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        """
        return pulumi.get(self, "aws_service_access_principals")

    @property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `AISERVICES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        """
        return pulumi.get(self, "enabled_policy_types")

    @property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> pulumi.Output[Optional[str]]:
        """
        Specify "ALL" (default) or "CONSOLIDATED_BILLING".
        """
        return pulumi.get(self, "feature_set")

    @property
    @pulumi.getter(name="masterAccountArn")
    def master_account_arn(self) -> pulumi.Output[str]:
        """
        ARN of the master account
        """
        return pulumi.get(self, "master_account_arn")

    @property
    @pulumi.getter(name="masterAccountEmail")
    def master_account_email(self) -> pulumi.Output[str]:
        """
        Email address of the master account
        """
        return pulumi.get(self, "master_account_email")

    @property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> pulumi.Output[str]:
        """
        Identifier of the master account
        """
        return pulumi.get(self, "master_account_id")

    @property
    @pulumi.getter(name="nonMasterAccounts")
    def non_master_accounts(self) -> pulumi.Output[Sequence['outputs.OrganizationNonMasterAccount']]:
        """
        List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
        """
        return pulumi.get(self, "non_master_accounts")

    @property
    @pulumi.getter
    def roots(self) -> pulumi.Output[Sequence['outputs.OrganizationRoot']]:
        """
        List of organization roots. All elements have these attributes:
        """
        return pulumi.get(self, "roots")

