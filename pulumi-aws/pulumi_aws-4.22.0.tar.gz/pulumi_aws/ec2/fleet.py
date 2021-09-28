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

__all__ = ['FleetArgs', 'Fleet']

@pulumi.input_type
class FleetArgs:
    def __init__(__self__, *,
                 launch_template_config: pulumi.Input['FleetLaunchTemplateConfigArgs'],
                 target_capacity_specification: pulumi.Input['FleetTargetCapacitySpecificationArgs'],
                 excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
                 on_demand_options: Optional[pulumi.Input['FleetOnDemandOptionsArgs']] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input['FleetSpotOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 terminate_instances: Optional[pulumi.Input[bool]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Fleet resource.
        :param pulumi.Input['FleetLaunchTemplateConfigArgs'] launch_template_config: Nested argument containing EC2 Launch Template configurations. Defined below.
        :param pulumi.Input['FleetTargetCapacitySpecificationArgs'] target_capacity_specification: Nested argument containing target capacity configurations. Defined below.
        :param pulumi.Input[str] excess_capacity_termination_policy: Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        :param pulumi.Input['FleetOnDemandOptionsArgs'] on_demand_options: Nested argument containing On-Demand configurations. Defined below.
        :param pulumi.Input[bool] replace_unhealthy_instances: Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        :param pulumi.Input['FleetSpotOptionsArgs'] spot_options: Nested argument containing Spot configurations. Defined below.
        :param pulumi.Input[bool] terminate_instances: Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        :param pulumi.Input[bool] terminate_instances_with_expiration: Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        :param pulumi.Input[str] type: The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        pulumi.set(__self__, "launch_template_config", launch_template_config)
        pulumi.set(__self__, "target_capacity_specification", target_capacity_specification)
        if excess_capacity_termination_policy is not None:
            pulumi.set(__self__, "excess_capacity_termination_policy", excess_capacity_termination_policy)
        if on_demand_options is not None:
            pulumi.set(__self__, "on_demand_options", on_demand_options)
        if replace_unhealthy_instances is not None:
            pulumi.set(__self__, "replace_unhealthy_instances", replace_unhealthy_instances)
        if spot_options is not None:
            pulumi.set(__self__, "spot_options", spot_options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if terminate_instances is not None:
            pulumi.set(__self__, "terminate_instances", terminate_instances)
        if terminate_instances_with_expiration is not None:
            pulumi.set(__self__, "terminate_instances_with_expiration", terminate_instances_with_expiration)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="launchTemplateConfig")
    def launch_template_config(self) -> pulumi.Input['FleetLaunchTemplateConfigArgs']:
        """
        Nested argument containing EC2 Launch Template configurations. Defined below.
        """
        return pulumi.get(self, "launch_template_config")

    @launch_template_config.setter
    def launch_template_config(self, value: pulumi.Input['FleetLaunchTemplateConfigArgs']):
        pulumi.set(self, "launch_template_config", value)

    @property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Input['FleetTargetCapacitySpecificationArgs']:
        """
        Nested argument containing target capacity configurations. Defined below.
        """
        return pulumi.get(self, "target_capacity_specification")

    @target_capacity_specification.setter
    def target_capacity_specification(self, value: pulumi.Input['FleetTargetCapacitySpecificationArgs']):
        pulumi.set(self, "target_capacity_specification", value)

    @property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        """
        return pulumi.get(self, "excess_capacity_termination_policy")

    @excess_capacity_termination_policy.setter
    def excess_capacity_termination_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "excess_capacity_termination_policy", value)

    @property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> Optional[pulumi.Input['FleetOnDemandOptionsArgs']]:
        """
        Nested argument containing On-Demand configurations. Defined below.
        """
        return pulumi.get(self, "on_demand_options")

    @on_demand_options.setter
    def on_demand_options(self, value: Optional[pulumi.Input['FleetOnDemandOptionsArgs']]):
        pulumi.set(self, "on_demand_options", value)

    @property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        """
        return pulumi.get(self, "replace_unhealthy_instances")

    @replace_unhealthy_instances.setter
    def replace_unhealthy_instances(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace_unhealthy_instances", value)

    @property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input['FleetSpotOptionsArgs']]:
        """
        Nested argument containing Spot configurations. Defined below.
        """
        return pulumi.get(self, "spot_options")

    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input['FleetSpotOptionsArgs']]):
        pulumi.set(self, "spot_options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances")

    @terminate_instances.setter
    def terminate_instances(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "terminate_instances", value)

    @property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances_with_expiration")

    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "terminate_instances_with_expiration", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _FleetState:
    def __init__(__self__, *,
                 excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
                 launch_template_config: Optional[pulumi.Input['FleetLaunchTemplateConfigArgs']] = None,
                 on_demand_options: Optional[pulumi.Input['FleetOnDemandOptionsArgs']] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input['FleetSpotOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_capacity_specification: Optional[pulumi.Input['FleetTargetCapacitySpecificationArgs']] = None,
                 terminate_instances: Optional[pulumi.Input[bool]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Fleet resources.
        :param pulumi.Input[str] excess_capacity_termination_policy: Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        :param pulumi.Input['FleetLaunchTemplateConfigArgs'] launch_template_config: Nested argument containing EC2 Launch Template configurations. Defined below.
        :param pulumi.Input['FleetOnDemandOptionsArgs'] on_demand_options: Nested argument containing On-Demand configurations. Defined below.
        :param pulumi.Input[bool] replace_unhealthy_instances: Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        :param pulumi.Input['FleetSpotOptionsArgs'] spot_options: Nested argument containing Spot configurations. Defined below.
        :param pulumi.Input['FleetTargetCapacitySpecificationArgs'] target_capacity_specification: Nested argument containing target capacity configurations. Defined below.
        :param pulumi.Input[bool] terminate_instances: Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        :param pulumi.Input[bool] terminate_instances_with_expiration: Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        :param pulumi.Input[str] type: The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        if excess_capacity_termination_policy is not None:
            pulumi.set(__self__, "excess_capacity_termination_policy", excess_capacity_termination_policy)
        if launch_template_config is not None:
            pulumi.set(__self__, "launch_template_config", launch_template_config)
        if on_demand_options is not None:
            pulumi.set(__self__, "on_demand_options", on_demand_options)
        if replace_unhealthy_instances is not None:
            pulumi.set(__self__, "replace_unhealthy_instances", replace_unhealthy_instances)
        if spot_options is not None:
            pulumi.set(__self__, "spot_options", spot_options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if target_capacity_specification is not None:
            pulumi.set(__self__, "target_capacity_specification", target_capacity_specification)
        if terminate_instances is not None:
            pulumi.set(__self__, "terminate_instances", terminate_instances)
        if terminate_instances_with_expiration is not None:
            pulumi.set(__self__, "terminate_instances_with_expiration", terminate_instances_with_expiration)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        """
        return pulumi.get(self, "excess_capacity_termination_policy")

    @excess_capacity_termination_policy.setter
    def excess_capacity_termination_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "excess_capacity_termination_policy", value)

    @property
    @pulumi.getter(name="launchTemplateConfig")
    def launch_template_config(self) -> Optional[pulumi.Input['FleetLaunchTemplateConfigArgs']]:
        """
        Nested argument containing EC2 Launch Template configurations. Defined below.
        """
        return pulumi.get(self, "launch_template_config")

    @launch_template_config.setter
    def launch_template_config(self, value: Optional[pulumi.Input['FleetLaunchTemplateConfigArgs']]):
        pulumi.set(self, "launch_template_config", value)

    @property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> Optional[pulumi.Input['FleetOnDemandOptionsArgs']]:
        """
        Nested argument containing On-Demand configurations. Defined below.
        """
        return pulumi.get(self, "on_demand_options")

    @on_demand_options.setter
    def on_demand_options(self, value: Optional[pulumi.Input['FleetOnDemandOptionsArgs']]):
        pulumi.set(self, "on_demand_options", value)

    @property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        """
        return pulumi.get(self, "replace_unhealthy_instances")

    @replace_unhealthy_instances.setter
    def replace_unhealthy_instances(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace_unhealthy_instances", value)

    @property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input['FleetSpotOptionsArgs']]:
        """
        Nested argument containing Spot configurations. Defined below.
        """
        return pulumi.get(self, "spot_options")

    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input['FleetSpotOptionsArgs']]):
        pulumi.set(self, "spot_options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> Optional[pulumi.Input['FleetTargetCapacitySpecificationArgs']]:
        """
        Nested argument containing target capacity configurations. Defined below.
        """
        return pulumi.get(self, "target_capacity_specification")

    @target_capacity_specification.setter
    def target_capacity_specification(self, value: Optional[pulumi.Input['FleetTargetCapacitySpecificationArgs']]):
        pulumi.set(self, "target_capacity_specification", value)

    @property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances")

    @terminate_instances.setter
    def terminate_instances(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "terminate_instances", value)

    @property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances_with_expiration")

    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "terminate_instances_with_expiration", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Fleet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
                 launch_template_config: Optional[pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']]] = None,
                 on_demand_options: Optional[pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']]] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']]] = None,
                 terminate_instances: Optional[pulumi.Input[bool]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to manage EC2 Fleets.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.Fleet("example",
            launch_template_config=aws.ec2.FleetLaunchTemplateConfigArgs(
                launch_template_specification=aws.ec2.FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs(
                    launch_template_id=aws_launch_template["example"]["id"],
                    version=aws_launch_template["example"]["latest_version"],
                ),
            ),
            target_capacity_specification=aws.ec2.FleetTargetCapacitySpecificationArgs(
                default_target_capacity_type="spot",
                total_target_capacity=5,
            ))
        ```

        ## Import

        `aws_ec2_fleet` can be imported by using the Fleet identifier, e.g.

        ```sh
         $ pulumi import aws:ec2/fleet:Fleet example fleet-b9b55d27-c5fc-41ac-a6f3-48fcc91f080c
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] excess_capacity_termination_policy: Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        :param pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']] launch_template_config: Nested argument containing EC2 Launch Template configurations. Defined below.
        :param pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']] on_demand_options: Nested argument containing On-Demand configurations. Defined below.
        :param pulumi.Input[bool] replace_unhealthy_instances: Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']] spot_options: Nested argument containing Spot configurations. Defined below.
        :param pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']] target_capacity_specification: Nested argument containing target capacity configurations. Defined below.
        :param pulumi.Input[bool] terminate_instances: Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        :param pulumi.Input[bool] terminate_instances_with_expiration: Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        :param pulumi.Input[str] type: The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FleetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage EC2 Fleets.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.Fleet("example",
            launch_template_config=aws.ec2.FleetLaunchTemplateConfigArgs(
                launch_template_specification=aws.ec2.FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs(
                    launch_template_id=aws_launch_template["example"]["id"],
                    version=aws_launch_template["example"]["latest_version"],
                ),
            ),
            target_capacity_specification=aws.ec2.FleetTargetCapacitySpecificationArgs(
                default_target_capacity_type="spot",
                total_target_capacity=5,
            ))
        ```

        ## Import

        `aws_ec2_fleet` can be imported by using the Fleet identifier, e.g.

        ```sh
         $ pulumi import aws:ec2/fleet:Fleet example fleet-b9b55d27-c5fc-41ac-a6f3-48fcc91f080c
        ```

        :param str resource_name: The name of the resource.
        :param FleetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FleetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
                 launch_template_config: Optional[pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']]] = None,
                 on_demand_options: Optional[pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']]] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']]] = None,
                 terminate_instances: Optional[pulumi.Input[bool]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = FleetArgs.__new__(FleetArgs)

            __props__.__dict__["excess_capacity_termination_policy"] = excess_capacity_termination_policy
            if launch_template_config is None and not opts.urn:
                raise TypeError("Missing required property 'launch_template_config'")
            __props__.__dict__["launch_template_config"] = launch_template_config
            __props__.__dict__["on_demand_options"] = on_demand_options
            __props__.__dict__["replace_unhealthy_instances"] = replace_unhealthy_instances
            __props__.__dict__["spot_options"] = spot_options
            __props__.__dict__["tags"] = tags
            if target_capacity_specification is None and not opts.urn:
                raise TypeError("Missing required property 'target_capacity_specification'")
            __props__.__dict__["target_capacity_specification"] = target_capacity_specification
            __props__.__dict__["terminate_instances"] = terminate_instances
            __props__.__dict__["terminate_instances_with_expiration"] = terminate_instances_with_expiration
            __props__.__dict__["type"] = type
            __props__.__dict__["tags_all"] = None
        super(Fleet, __self__).__init__(
            'aws:ec2/fleet:Fleet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
            launch_template_config: Optional[pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']]] = None,
            on_demand_options: Optional[pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']]] = None,
            replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
            spot_options: Optional[pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']]] = None,
            terminate_instances: Optional[pulumi.Input[bool]] = None,
            terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Fleet':
        """
        Get an existing Fleet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] excess_capacity_termination_policy: Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        :param pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']] launch_template_config: Nested argument containing EC2 Launch Template configurations. Defined below.
        :param pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']] on_demand_options: Nested argument containing On-Demand configurations. Defined below.
        :param pulumi.Input[bool] replace_unhealthy_instances: Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']] spot_options: Nested argument containing Spot configurations. Defined below.
        :param pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']] target_capacity_specification: Nested argument containing target capacity configurations. Defined below.
        :param pulumi.Input[bool] terminate_instances: Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        :param pulumi.Input[bool] terminate_instances_with_expiration: Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        :param pulumi.Input[str] type: The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FleetState.__new__(_FleetState)

        __props__.__dict__["excess_capacity_termination_policy"] = excess_capacity_termination_policy
        __props__.__dict__["launch_template_config"] = launch_template_config
        __props__.__dict__["on_demand_options"] = on_demand_options
        __props__.__dict__["replace_unhealthy_instances"] = replace_unhealthy_instances
        __props__.__dict__["spot_options"] = spot_options
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["target_capacity_specification"] = target_capacity_specification
        __props__.__dict__["terminate_instances"] = terminate_instances
        __props__.__dict__["terminate_instances_with_expiration"] = terminate_instances_with_expiration
        __props__.__dict__["type"] = type
        return Fleet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        """
        return pulumi.get(self, "excess_capacity_termination_policy")

    @property
    @pulumi.getter(name="launchTemplateConfig")
    def launch_template_config(self) -> pulumi.Output['outputs.FleetLaunchTemplateConfig']:
        """
        Nested argument containing EC2 Launch Template configurations. Defined below.
        """
        return pulumi.get(self, "launch_template_config")

    @property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> pulumi.Output[Optional['outputs.FleetOnDemandOptions']]:
        """
        Nested argument containing On-Demand configurations. Defined below.
        """
        return pulumi.get(self, "on_demand_options")

    @property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        """
        return pulumi.get(self, "replace_unhealthy_instances")

    @property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> pulumi.Output[Optional['outputs.FleetSpotOptions']]:
        """
        Nested argument containing Spot configurations. Defined below.
        """
        return pulumi.get(self, "spot_options")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Output['outputs.FleetTargetCapacitySpecification']:
        """
        Nested argument containing target capacity configurations. Defined below.
        """
        return pulumi.get(self, "target_capacity_specification")

    @property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances")

    @property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances_with_expiration")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        return pulumi.get(self, "type")

