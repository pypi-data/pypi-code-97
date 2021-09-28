# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RoutingControlArgs', 'RoutingControl']

@pulumi.input_type
class RoutingControlArgs:
    def __init__(__self__, *,
                 cluster_arn: pulumi.Input[str],
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RoutingControl resource.
        :param pulumi.Input[str] cluster_arn: ARN of the cluster in which this routing control will reside.
        :param pulumi.Input[str] control_panel_arn: ARN of the control panel in which this routing control will reside.
        :param pulumi.Input[str] name: The name describing the routing control.
        """
        pulumi.set(__self__, "cluster_arn", cluster_arn)
        if control_panel_arn is not None:
            pulumi.set(__self__, "control_panel_arn", control_panel_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[str]:
        """
        ARN of the cluster in which this routing control will reside.
        """
        return pulumi.get(self, "cluster_arn")

    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_arn", value)

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the control panel in which this routing control will reside.
        """
        return pulumi.get(self, "control_panel_arn")

    @control_panel_arn.setter
    def control_panel_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "control_panel_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name describing the routing control.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RoutingControlState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RoutingControl resources.
        :param pulumi.Input[str] arn: ARN of the routing control.
        :param pulumi.Input[str] cluster_arn: ARN of the cluster in which this routing control will reside.
        :param pulumi.Input[str] control_panel_arn: ARN of the control panel in which this routing control will reside.
        :param pulumi.Input[str] name: The name describing the routing control.
        :param pulumi.Input[str] status: Status of routing control. `PENDING` when it is being created/updated, `PENDING_DELETION` when it is being deleted, and `DEPLOYED` otherwise.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if cluster_arn is not None:
            pulumi.set(__self__, "cluster_arn", cluster_arn)
        if control_panel_arn is not None:
            pulumi.set(__self__, "control_panel_arn", control_panel_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the routing control.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the cluster in which this routing control will reside.
        """
        return pulumi.get(self, "cluster_arn")

    @cluster_arn.setter
    def cluster_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_arn", value)

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the control panel in which this routing control will reside.
        """
        return pulumi.get(self, "control_panel_arn")

    @control_panel_arn.setter
    def control_panel_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "control_panel_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name describing the routing control.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of routing control. `PENDING` when it is being created/updated, `PENDING_DELETION` when it is being deleted, and `DEPLOYED` otherwise.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class RoutingControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an AWS Route 53 Recovery Control Config Routing Control.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53recoverycontrol.RoutingControl("example", cluster_arn="arn:aws:route53-recovery-control::881188118811:cluster/8d47920e-d789-437d-803a-2dcc4b204393")
        ```

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53recoverycontrol.RoutingControl("example",
            cluster_arn="arn:aws:route53-recovery-control::881188118811:cluster/8d47920e-d789-437d-803a-2dcc4b204393",
            control_panel_arn="arn:aws:route53-recovery-control::428113431245:controlpanel/abd5fbfc052d4844a082dbf400f61da8")
        ```

        ## Import

        Route53 Recovery Control Config Routing Control can be imported via the routing control arn, e.g.

        ```sh
         $ pulumi import aws:route53recoverycontrol/routingControl:RoutingControl mycontrol arn:aws:route53-recovery-control::313517334327:controlpanel/abd5fbfc052d4844a082dbf400f61da8/routingcontrol/d5d90e587870494b
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_arn: ARN of the cluster in which this routing control will reside.
        :param pulumi.Input[str] control_panel_arn: ARN of the control panel in which this routing control will reside.
        :param pulumi.Input[str] name: The name describing the routing control.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoutingControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS Route 53 Recovery Control Config Routing Control.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53recoverycontrol.RoutingControl("example", cluster_arn="arn:aws:route53-recovery-control::881188118811:cluster/8d47920e-d789-437d-803a-2dcc4b204393")
        ```

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53recoverycontrol.RoutingControl("example",
            cluster_arn="arn:aws:route53-recovery-control::881188118811:cluster/8d47920e-d789-437d-803a-2dcc4b204393",
            control_panel_arn="arn:aws:route53-recovery-control::428113431245:controlpanel/abd5fbfc052d4844a082dbf400f61da8")
        ```

        ## Import

        Route53 Recovery Control Config Routing Control can be imported via the routing control arn, e.g.

        ```sh
         $ pulumi import aws:route53recoverycontrol/routingControl:RoutingControl mycontrol arn:aws:route53-recovery-control::313517334327:controlpanel/abd5fbfc052d4844a082dbf400f61da8/routingcontrol/d5d90e587870494b
        ```

        :param str resource_name: The name of the resource.
        :param RoutingControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoutingControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = RoutingControlArgs.__new__(RoutingControlArgs)

            if cluster_arn is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_arn'")
            __props__.__dict__["cluster_arn"] = cluster_arn
            __props__.__dict__["control_panel_arn"] = control_panel_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["arn"] = None
            __props__.__dict__["status"] = None
        super(RoutingControl, __self__).__init__(
            'aws:route53recoverycontrol/routingControl:RoutingControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cluster_arn: Optional[pulumi.Input[str]] = None,
            control_panel_arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'RoutingControl':
        """
        Get an existing RoutingControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the routing control.
        :param pulumi.Input[str] cluster_arn: ARN of the cluster in which this routing control will reside.
        :param pulumi.Input[str] control_panel_arn: ARN of the control panel in which this routing control will reside.
        :param pulumi.Input[str] name: The name describing the routing control.
        :param pulumi.Input[str] status: Status of routing control. `PENDING` when it is being created/updated, `PENDING_DELETION` when it is being deleted, and `DEPLOYED` otherwise.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoutingControlState.__new__(_RoutingControlState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["cluster_arn"] = cluster_arn
        __props__.__dict__["control_panel_arn"] = control_panel_arn
        __props__.__dict__["name"] = name
        __props__.__dict__["status"] = status
        return RoutingControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the routing control.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Output[str]:
        """
        ARN of the cluster in which this routing control will reside.
        """
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> pulumi.Output[str]:
        """
        ARN of the control panel in which this routing control will reside.
        """
        return pulumi.get(self, "control_panel_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name describing the routing control.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of routing control. `PENDING` when it is being created/updated, `PENDING_DELETION` when it is being deleted, and `DEPLOYED` otherwise.
        """
        return pulumi.get(self, "status")

