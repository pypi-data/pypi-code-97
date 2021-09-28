# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['LocalGatewayRouteTableVpcAssociationArgs', 'LocalGatewayRouteTableVpcAssociation']

@pulumi.input_type
class LocalGatewayRouteTableVpcAssociationArgs:
    def __init__(__self__, *,
                 local_gateway_route_table_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LocalGatewayRouteTableVpcAssociation resource.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[str] vpc_id: Identifier of EC2 VPC.
        """
        pulumi.set(__self__, "local_gateway_route_table_id", local_gateway_route_table_id)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Input[str]:
        """
        Identifier of EC2 Local Gateway Route Table.
        """
        return pulumi.get(self, "local_gateway_route_table_id")

    @local_gateway_route_table_id.setter
    def local_gateway_route_table_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "local_gateway_route_table_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        Identifier of EC2 VPC.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _LocalGatewayRouteTableVpcAssociationState:
    def __init__(__self__, *,
                 local_gateway_id: Optional[pulumi.Input[str]] = None,
                 local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LocalGatewayRouteTableVpcAssociation resources.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[str] vpc_id: Identifier of EC2 VPC.
        """
        if local_gateway_id is not None:
            pulumi.set(__self__, "local_gateway_id", local_gateway_id)
        if local_gateway_route_table_id is not None:
            pulumi.set(__self__, "local_gateway_route_table_id", local_gateway_route_table_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "local_gateway_id")

    @local_gateway_id.setter
    def local_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_gateway_id", value)

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of EC2 Local Gateway Route Table.
        """
        return pulumi.get(self, "local_gateway_route_table_id")

    @local_gateway_route_table_id.setter
    def local_gateway_route_table_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_gateway_route_table_id", value)

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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of EC2 VPC.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class LocalGatewayRouteTableVpcAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an EC2 Local Gateway Route Table VPC Association. More information can be found in the [Outposts User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_local_gateway_route_table = aws.ec2.get_local_gateway_route_table(outpost_arn="arn:aws:outposts:us-west-2:123456789012:outpost/op-1234567890abcdef")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_local_gateway_route_table_vpc_association = aws.ec2.LocalGatewayRouteTableVpcAssociation("exampleLocalGatewayRouteTableVpcAssociation",
            local_gateway_route_table_id=example_local_gateway_route_table.id,
            vpc_id=example_vpc.id)
        ```

        ## Import

        `aws_ec2_local_gateway_route_table_vpc_association` can be imported by using the Local Gateway Route Table VPC Association identifier, e.g.

        ```sh
         $ pulumi import aws:ec2/localGatewayRouteTableVpcAssociation:LocalGatewayRouteTableVpcAssociation example lgw-vpc-assoc-1234567890abcdef
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[str] vpc_id: Identifier of EC2 VPC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalGatewayRouteTableVpcAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an EC2 Local Gateway Route Table VPC Association. More information can be found in the [Outposts User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_local_gateway_route_table = aws.ec2.get_local_gateway_route_table(outpost_arn="arn:aws:outposts:us-west-2:123456789012:outpost/op-1234567890abcdef")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_local_gateway_route_table_vpc_association = aws.ec2.LocalGatewayRouteTableVpcAssociation("exampleLocalGatewayRouteTableVpcAssociation",
            local_gateway_route_table_id=example_local_gateway_route_table.id,
            vpc_id=example_vpc.id)
        ```

        ## Import

        `aws_ec2_local_gateway_route_table_vpc_association` can be imported by using the Local Gateway Route Table VPC Association identifier, e.g.

        ```sh
         $ pulumi import aws:ec2/localGatewayRouteTableVpcAssociation:LocalGatewayRouteTableVpcAssociation example lgw-vpc-assoc-1234567890abcdef
        ```

        :param str resource_name: The name of the resource.
        :param LocalGatewayRouteTableVpcAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalGatewayRouteTableVpcAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = LocalGatewayRouteTableVpcAssociationArgs.__new__(LocalGatewayRouteTableVpcAssociationArgs)

            if local_gateway_route_table_id is None and not opts.urn:
                raise TypeError("Missing required property 'local_gateway_route_table_id'")
            __props__.__dict__["local_gateway_route_table_id"] = local_gateway_route_table_id
            __props__.__dict__["tags"] = tags
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["local_gateway_id"] = None
            __props__.__dict__["tags_all"] = None
        super(LocalGatewayRouteTableVpcAssociation, __self__).__init__(
            'aws:ec2/localGatewayRouteTableVpcAssociation:LocalGatewayRouteTableVpcAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            local_gateway_id: Optional[pulumi.Input[str]] = None,
            local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'LocalGatewayRouteTableVpcAssociation':
        """
        Get an existing LocalGatewayRouteTableVpcAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[str] vpc_id: Identifier of EC2 VPC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LocalGatewayRouteTableVpcAssociationState.__new__(_LocalGatewayRouteTableVpcAssociationState)

        __props__.__dict__["local_gateway_id"] = local_gateway_id
        __props__.__dict__["local_gateway_route_table_id"] = local_gateway_route_table_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["vpc_id"] = vpc_id
        return LocalGatewayRouteTableVpcAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "local_gateway_id")

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Local Gateway Route Table.
        """
        return pulumi.get(self, "local_gateway_route_table_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 VPC.
        """
        return pulumi.get(self, "vpc_id")

