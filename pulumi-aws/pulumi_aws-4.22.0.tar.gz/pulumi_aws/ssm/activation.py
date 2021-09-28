# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ActivationArgs', 'Activation']

@pulumi.input_type
class ActivationArgs:
    def __init__(__self__, *,
                 iam_role: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registration_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Activation resource.
        :param pulumi.Input[str] iam_role: The IAM Role to attach to the managed instance.
        :param pulumi.Input[str] description: The description of the resource that you want to register.
        :param pulumi.Input[str] expiration_date: UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        :param pulumi.Input[str] name: The default name of the registered managed instance.
        :param pulumi.Input[int] registration_limit: The maximum number of managed instances you want to register. The default value is 1 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "iam_role", iam_role)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if registration_limit is not None:
            pulumi.set(__self__, "registration_limit", registration_limit)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> pulumi.Input[str]:
        """
        The IAM Role to attach to the managed instance.
        """
        return pulumi.get(self, "iam_role")

    @iam_role.setter
    def iam_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "iam_role", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the resource that you want to register.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[str]]:
        """
        UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        """
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The default name of the registered managed instance.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="registrationLimit")
    def registration_limit(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of managed instances you want to register. The default value is 1 instance.
        """
        return pulumi.get(self, "registration_limit")

    @registration_limit.setter
    def registration_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "registration_limit", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ActivationState:
    def __init__(__self__, *,
                 activation_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 expired: Optional[pulumi.Input[bool]] = None,
                 iam_role: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registration_count: Optional[pulumi.Input[int]] = None,
                 registration_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Activation resources.
        :param pulumi.Input[str] activation_code: The code the system generates when it processes the activation.
        :param pulumi.Input[str] description: The description of the resource that you want to register.
        :param pulumi.Input[str] expiration_date: UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        :param pulumi.Input[bool] expired: If the current activation has expired.
        :param pulumi.Input[str] iam_role: The IAM Role to attach to the managed instance.
        :param pulumi.Input[str] name: The default name of the registered managed instance.
        :param pulumi.Input[int] registration_count: The number of managed instances that are currently registered using this activation.
        :param pulumi.Input[int] registration_limit: The maximum number of managed instances you want to register. The default value is 1 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        if activation_code is not None:
            pulumi.set(__self__, "activation_code", activation_code)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if expired is not None:
            pulumi.set(__self__, "expired", expired)
        if iam_role is not None:
            pulumi.set(__self__, "iam_role", iam_role)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if registration_count is not None:
            pulumi.set(__self__, "registration_count", registration_count)
        if registration_limit is not None:
            pulumi.set(__self__, "registration_limit", registration_limit)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="activationCode")
    def activation_code(self) -> Optional[pulumi.Input[str]]:
        """
        The code the system generates when it processes the activation.
        """
        return pulumi.get(self, "activation_code")

    @activation_code.setter
    def activation_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "activation_code", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the resource that you want to register.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[str]]:
        """
        UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        """
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter
    def expired(self) -> Optional[pulumi.Input[bool]]:
        """
        If the current activation has expired.
        """
        return pulumi.get(self, "expired")

    @expired.setter
    def expired(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "expired", value)

    @property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> Optional[pulumi.Input[str]]:
        """
        The IAM Role to attach to the managed instance.
        """
        return pulumi.get(self, "iam_role")

    @iam_role.setter
    def iam_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_role", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The default name of the registered managed instance.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="registrationCount")
    def registration_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of managed instances that are currently registered using this activation.
        """
        return pulumi.get(self, "registration_count")

    @registration_count.setter
    def registration_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "registration_count", value)

    @property
    @pulumi.getter(name="registrationLimit")
    def registration_limit(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of managed instances you want to register. The default value is 1 instance.
        """
        return pulumi.get(self, "registration_limit")

    @registration_limit.setter
    def registration_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "registration_limit", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Activation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 iam_role: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registration_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_role = aws.iam.Role("testRole", assume_role_policy=\"\"\"  {
            "Version": "2012-10-17",
            "Statement": {
              "Effect": "Allow",
              "Principal": {"Service": "ssm.amazonaws.com"},
              "Action": "sts:AssumeRole"
            }
          }
        \"\"\")
        test_attach = aws.iam.RolePolicyAttachment("testAttach",
            role=test_role.name,
            policy_arn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore")
        foo = aws.ssm.Activation("foo",
            description="Test",
            iam_role=test_role.id,
            registration_limit=5,
            opts=pulumi.ResourceOptions(depends_on=[test_attach]))
        ```

        ## Import

        AWS SSM Activation can be imported using the `id`, e.g.

        ```sh
         $ pulumi import aws:ssm/activation:Activation example e488f2f6-e686-4afb-8a04-ef6dfEXAMPLE
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource that you want to register.
        :param pulumi.Input[str] expiration_date: UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        :param pulumi.Input[str] iam_role: The IAM Role to attach to the managed instance.
        :param pulumi.Input[str] name: The default name of the registered managed instance.
        :param pulumi.Input[int] registration_limit: The maximum number of managed instances you want to register. The default value is 1 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActivationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_role = aws.iam.Role("testRole", assume_role_policy=\"\"\"  {
            "Version": "2012-10-17",
            "Statement": {
              "Effect": "Allow",
              "Principal": {"Service": "ssm.amazonaws.com"},
              "Action": "sts:AssumeRole"
            }
          }
        \"\"\")
        test_attach = aws.iam.RolePolicyAttachment("testAttach",
            role=test_role.name,
            policy_arn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore")
        foo = aws.ssm.Activation("foo",
            description="Test",
            iam_role=test_role.id,
            registration_limit=5,
            opts=pulumi.ResourceOptions(depends_on=[test_attach]))
        ```

        ## Import

        AWS SSM Activation can be imported using the `id`, e.g.

        ```sh
         $ pulumi import aws:ssm/activation:Activation example e488f2f6-e686-4afb-8a04-ef6dfEXAMPLE
        ```

        :param str resource_name: The name of the resource.
        :param ActivationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActivationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 iam_role: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registration_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = ActivationArgs.__new__(ActivationArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["expiration_date"] = expiration_date
            if iam_role is None and not opts.urn:
                raise TypeError("Missing required property 'iam_role'")
            __props__.__dict__["iam_role"] = iam_role
            __props__.__dict__["name"] = name
            __props__.__dict__["registration_limit"] = registration_limit
            __props__.__dict__["tags"] = tags
            __props__.__dict__["activation_code"] = None
            __props__.__dict__["expired"] = None
            __props__.__dict__["registration_count"] = None
            __props__.__dict__["tags_all"] = None
        super(Activation, __self__).__init__(
            'aws:ssm/activation:Activation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            activation_code: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expiration_date: Optional[pulumi.Input[str]] = None,
            expired: Optional[pulumi.Input[bool]] = None,
            iam_role: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            registration_count: Optional[pulumi.Input[int]] = None,
            registration_limit: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Activation':
        """
        Get an existing Activation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] activation_code: The code the system generates when it processes the activation.
        :param pulumi.Input[str] description: The description of the resource that you want to register.
        :param pulumi.Input[str] expiration_date: UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        :param pulumi.Input[bool] expired: If the current activation has expired.
        :param pulumi.Input[str] iam_role: The IAM Role to attach to the managed instance.
        :param pulumi.Input[str] name: The default name of the registered managed instance.
        :param pulumi.Input[int] registration_count: The number of managed instances that are currently registered using this activation.
        :param pulumi.Input[int] registration_limit: The maximum number of managed instances you want to register. The default value is 1 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ActivationState.__new__(_ActivationState)

        __props__.__dict__["activation_code"] = activation_code
        __props__.__dict__["description"] = description
        __props__.__dict__["expiration_date"] = expiration_date
        __props__.__dict__["expired"] = expired
        __props__.__dict__["iam_role"] = iam_role
        __props__.__dict__["name"] = name
        __props__.__dict__["registration_count"] = registration_count
        __props__.__dict__["registration_limit"] = registration_limit
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Activation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activationCode")
    def activation_code(self) -> pulumi.Output[str]:
        """
        The code the system generates when it processes the activation.
        """
        return pulumi.get(self, "activation_code")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the resource that you want to register.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[str]:
        """
        UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def expired(self) -> pulumi.Output[bool]:
        """
        If the current activation has expired.
        """
        return pulumi.get(self, "expired")

    @property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> pulumi.Output[str]:
        """
        The IAM Role to attach to the managed instance.
        """
        return pulumi.get(self, "iam_role")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The default name of the registered managed instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registrationCount")
    def registration_count(self) -> pulumi.Output[int]:
        """
        The number of managed instances that are currently registered using this activation.
        """
        return pulumi.get(self, "registration_count")

    @property
    @pulumi.getter(name="registrationLimit")
    def registration_limit(self) -> pulumi.Output[int]:
        """
        The maximum number of managed instances you want to register. The default value is 1 instance.
        """
        return pulumi.get(self, "registration_limit")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the object. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

