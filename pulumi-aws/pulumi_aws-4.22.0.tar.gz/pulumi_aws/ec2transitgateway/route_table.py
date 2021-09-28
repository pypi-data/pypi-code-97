# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RouteTableArgs', 'RouteTable']

@pulumi.input_type
class RouteTableArgs:
    def __init__(__self__, *,
                 transit_gateway_id: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RouteTable resource.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[str]:
        """
        Identifier of EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _RouteTableState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 default_association_route_table: Optional[pulumi.Input[bool]] = None,
                 default_propagation_route_table: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RouteTable resources.
        :param pulumi.Input[str] arn: EC2 Transit Gateway Route Table Amazon Resource Name (ARN).
        :param pulumi.Input[bool] default_association_route_table: Boolean whether this is the default association route table for the EC2 Transit Gateway.
        :param pulumi.Input[bool] default_propagation_route_table: Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if default_association_route_table is not None:
            pulumi.set(__self__, "default_association_route_table", default_association_route_table)
        if default_propagation_route_table is not None:
            pulumi.set(__self__, "default_propagation_route_table", default_propagation_route_table)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if transit_gateway_id is not None:
            pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        EC2 Transit Gateway Route Table Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="defaultAssociationRouteTable")
    def default_association_route_table(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether this is the default association route table for the EC2 Transit Gateway.
        """
        return pulumi.get(self, "default_association_route_table")

    @default_association_route_table.setter
    def default_association_route_table(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_association_route_table", value)

    @property
    @pulumi.getter(name="defaultPropagationRouteTable")
    def default_propagation_route_table(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
        """
        return pulumi.get(self, "default_propagation_route_table")

    @default_propagation_route_table.setter
    def default_propagation_route_table(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_propagation_route_table", value)

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
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_id", value)


class RouteTable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an EC2 Transit Gateway Route Table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2transitgateway.RouteTable("example", transit_gateway_id=aws_ec2_transit_gateway["example"]["id"])
        ```

        ## Import

        `aws_ec2_transit_gateway_route_table` can be imported by using the EC2 Transit Gateway Route Table identifier, e.g.

        ```sh
         $ pulumi import aws:ec2transitgateway/routeTable:RouteTable example tgw-rtb-12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteTableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an EC2 Transit Gateway Route Table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2transitgateway.RouteTable("example", transit_gateway_id=aws_ec2_transit_gateway["example"]["id"])
        ```

        ## Import

        `aws_ec2_transit_gateway_route_table` can be imported by using the EC2 Transit Gateway Route Table identifier, e.g.

        ```sh
         $ pulumi import aws:ec2transitgateway/routeTable:RouteTable example tgw-rtb-12345678
        ```

        :param str resource_name: The name of the resource.
        :param RouteTableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteTableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = RouteTableArgs.__new__(RouteTableArgs)

            __props__.__dict__["tags"] = tags
            if transit_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_id'")
            __props__.__dict__["transit_gateway_id"] = transit_gateway_id
            __props__.__dict__["arn"] = None
            __props__.__dict__["default_association_route_table"] = None
            __props__.__dict__["default_propagation_route_table"] = None
            __props__.__dict__["tags_all"] = None
        super(RouteTable, __self__).__init__(
            'aws:ec2transitgateway/routeTable:RouteTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_association_route_table: Optional[pulumi.Input[bool]] = None,
            default_propagation_route_table: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            transit_gateway_id: Optional[pulumi.Input[str]] = None) -> 'RouteTable':
        """
        Get an existing RouteTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: EC2 Transit Gateway Route Table Amazon Resource Name (ARN).
        :param pulumi.Input[bool] default_association_route_table: Boolean whether this is the default association route table for the EC2 Transit Gateway.
        :param pulumi.Input[bool] default_propagation_route_table: Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RouteTableState.__new__(_RouteTableState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["default_association_route_table"] = default_association_route_table
        __props__.__dict__["default_propagation_route_table"] = default_propagation_route_table
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["transit_gateway_id"] = transit_gateway_id
        return RouteTable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        EC2 Transit Gateway Route Table Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultAssociationRouteTable")
    def default_association_route_table(self) -> pulumi.Output[bool]:
        """
        Boolean whether this is the default association route table for the EC2 Transit Gateway.
        """
        return pulumi.get(self, "default_association_route_table")

    @property
    @pulumi.getter(name="defaultPropagationRouteTable")
    def default_propagation_route_table(self) -> pulumi.Output[bool]:
        """
        Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
        """
        return pulumi.get(self, "default_propagation_route_table")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

