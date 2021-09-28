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

__all__ = ['DomainNameArgs', 'DomainName']

@pulumi.input_type
class DomainNameArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 domain_name_configuration: pulumi.Input['DomainNameDomainNameConfigurationArgs'],
                 mutual_tls_authentication: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DomainName resource.
        :param pulumi.Input[str] domain_name: The domain name. Must be between 1 and 512 characters in length.
        :param pulumi.Input['DomainNameDomainNameConfigurationArgs'] domain_name_configuration: The domain name configuration.
        :param pulumi.Input['DomainNameMutualTlsAuthenticationArgs'] mutual_tls_authentication: The mutual TLS authentication configuration for the domain name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "domain_name_configuration", domain_name_configuration)
        if mutual_tls_authentication is not None:
            pulumi.set(__self__, "mutual_tls_authentication", mutual_tls_authentication)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The domain name. Must be between 1 and 512 characters in length.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="domainNameConfiguration")
    def domain_name_configuration(self) -> pulumi.Input['DomainNameDomainNameConfigurationArgs']:
        """
        The domain name configuration.
        """
        return pulumi.get(self, "domain_name_configuration")

    @domain_name_configuration.setter
    def domain_name_configuration(self, value: pulumi.Input['DomainNameDomainNameConfigurationArgs']):
        pulumi.set(self, "domain_name_configuration", value)

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]:
        """
        The mutual TLS authentication configuration for the domain name.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @mutual_tls_authentication.setter
    def mutual_tls_authentication(self, value: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]):
        pulumi.set(self, "mutual_tls_authentication", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _DomainNameState:
    def __init__(__self__, *,
                 api_mapping_selection_expression: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_name_configuration: Optional[pulumi.Input['DomainNameDomainNameConfigurationArgs']] = None,
                 mutual_tls_authentication: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering DomainName resources.
        :param pulumi.Input[str] api_mapping_selection_expression: The [API mapping selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressions) for the domain name.
        :param pulumi.Input[str] arn: The ARN of the domain name.
        :param pulumi.Input[str] domain_name: The domain name. Must be between 1 and 512 characters in length.
        :param pulumi.Input['DomainNameDomainNameConfigurationArgs'] domain_name_configuration: The domain name configuration.
        :param pulumi.Input['DomainNameMutualTlsAuthenticationArgs'] mutual_tls_authentication: The mutual TLS authentication configuration for the domain name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        if api_mapping_selection_expression is not None:
            pulumi.set(__self__, "api_mapping_selection_expression", api_mapping_selection_expression)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if domain_name_configuration is not None:
            pulumi.set(__self__, "domain_name_configuration", domain_name_configuration)
        if mutual_tls_authentication is not None:
            pulumi.set(__self__, "mutual_tls_authentication", mutual_tls_authentication)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="apiMappingSelectionExpression")
    def api_mapping_selection_expression(self) -> Optional[pulumi.Input[str]]:
        """
        The [API mapping selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressions) for the domain name.
        """
        return pulumi.get(self, "api_mapping_selection_expression")

    @api_mapping_selection_expression.setter
    def api_mapping_selection_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_mapping_selection_expression", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the domain name.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The domain name. Must be between 1 and 512 characters in length.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="domainNameConfiguration")
    def domain_name_configuration(self) -> Optional[pulumi.Input['DomainNameDomainNameConfigurationArgs']]:
        """
        The domain name configuration.
        """
        return pulumi.get(self, "domain_name_configuration")

    @domain_name_configuration.setter
    def domain_name_configuration(self, value: Optional[pulumi.Input['DomainNameDomainNameConfigurationArgs']]):
        pulumi.set(self, "domain_name_configuration", value)

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]:
        """
        The mutual TLS authentication configuration for the domain name.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @mutual_tls_authentication.setter
    def mutual_tls_authentication(self, value: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]):
        pulumi.set(self, "mutual_tls_authentication", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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


class DomainName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_name_configuration: Optional[pulumi.Input[pulumi.InputType['DomainNameDomainNameConfigurationArgs']]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an Amazon API Gateway Version 2 domain name.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

        > **Note:** This resource establishes ownership of and the TLS settings for
        a particular domain name. An API stage can be associated with the domain name using the `apigatewayv2.ApiMapping` resource.

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.DomainName("example",
            domain_name="ws-api.example.com",
            domain_name_configuration=aws.apigatewayv2.DomainNameDomainNameConfigurationArgs(
                certificate_arn=aws_acm_certificate["example"]["arn"],
                endpoint_type="REGIONAL",
                security_policy="TLS_1_2",
            ))
        ```
        ### Associated Route 53 Resource Record

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain_name = aws.apigatewayv2.DomainName("exampleDomainName",
            domain_name="http-api.example.com",
            domain_name_configuration=aws.apigatewayv2.DomainNameDomainNameConfigurationArgs(
                certificate_arn=aws_acm_certificate["example"]["arn"],
                endpoint_type="REGIONAL",
                security_policy="TLS_1_2",
            ))
        example_record = aws.route53.Record("exampleRecord",
            name=example_domain_name.domain_name,
            type="A",
            zone_id=aws_route53_zone["example"]["zone_id"],
            aliases=[aws.route53.RecordAliasArgs(
                name=example_domain_name.domain_name_configuration.target_domain_name,
                zone_id=example_domain_name.domain_name_configuration.hosted_zone_id,
                evaluate_target_health=False,
            )])
        ```

        ## Import

        `aws_apigatewayv2_domain_name` can be imported by using the domain name, e.g.

        ```sh
         $ pulumi import aws:apigatewayv2/domainName:DomainName example ws-api.example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The domain name. Must be between 1 and 512 characters in length.
        :param pulumi.Input[pulumi.InputType['DomainNameDomainNameConfigurationArgs']] domain_name_configuration: The domain name configuration.
        :param pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']] mutual_tls_authentication: The mutual TLS authentication configuration for the domain name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Amazon API Gateway Version 2 domain name.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

        > **Note:** This resource establishes ownership of and the TLS settings for
        a particular domain name. An API stage can be associated with the domain name using the `apigatewayv2.ApiMapping` resource.

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.DomainName("example",
            domain_name="ws-api.example.com",
            domain_name_configuration=aws.apigatewayv2.DomainNameDomainNameConfigurationArgs(
                certificate_arn=aws_acm_certificate["example"]["arn"],
                endpoint_type="REGIONAL",
                security_policy="TLS_1_2",
            ))
        ```
        ### Associated Route 53 Resource Record

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain_name = aws.apigatewayv2.DomainName("exampleDomainName",
            domain_name="http-api.example.com",
            domain_name_configuration=aws.apigatewayv2.DomainNameDomainNameConfigurationArgs(
                certificate_arn=aws_acm_certificate["example"]["arn"],
                endpoint_type="REGIONAL",
                security_policy="TLS_1_2",
            ))
        example_record = aws.route53.Record("exampleRecord",
            name=example_domain_name.domain_name,
            type="A",
            zone_id=aws_route53_zone["example"]["zone_id"],
            aliases=[aws.route53.RecordAliasArgs(
                name=example_domain_name.domain_name_configuration.target_domain_name,
                zone_id=example_domain_name.domain_name_configuration.hosted_zone_id,
                evaluate_target_health=False,
            )])
        ```

        ## Import

        `aws_apigatewayv2_domain_name` can be imported by using the domain name, e.g.

        ```sh
         $ pulumi import aws:apigatewayv2/domainName:DomainName example ws-api.example.com
        ```

        :param str resource_name: The name of the resource.
        :param DomainNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_name_configuration: Optional[pulumi.Input[pulumi.InputType['DomainNameDomainNameConfigurationArgs']]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
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
            __props__ = DomainNameArgs.__new__(DomainNameArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if domain_name_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name_configuration'")
            __props__.__dict__["domain_name_configuration"] = domain_name_configuration
            __props__.__dict__["mutual_tls_authentication"] = mutual_tls_authentication
            __props__.__dict__["tags"] = tags
            __props__.__dict__["api_mapping_selection_expression"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(DomainName, __self__).__init__(
            'aws:apigatewayv2/domainName:DomainName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_mapping_selection_expression: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            domain_name_configuration: Optional[pulumi.Input[pulumi.InputType['DomainNameDomainNameConfigurationArgs']]] = None,
            mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'DomainName':
        """
        Get an existing DomainName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_mapping_selection_expression: The [API mapping selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressions) for the domain name.
        :param pulumi.Input[str] arn: The ARN of the domain name.
        :param pulumi.Input[str] domain_name: The domain name. Must be between 1 and 512 characters in length.
        :param pulumi.Input[pulumi.InputType['DomainNameDomainNameConfigurationArgs']] domain_name_configuration: The domain name configuration.
        :param pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']] mutual_tls_authentication: The mutual TLS authentication configuration for the domain name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainNameState.__new__(_DomainNameState)

        __props__.__dict__["api_mapping_selection_expression"] = api_mapping_selection_expression
        __props__.__dict__["arn"] = arn
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["domain_name_configuration"] = domain_name_configuration
        __props__.__dict__["mutual_tls_authentication"] = mutual_tls_authentication
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return DomainName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiMappingSelectionExpression")
    def api_mapping_selection_expression(self) -> pulumi.Output[str]:
        """
        The [API mapping selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressions) for the domain name.
        """
        return pulumi.get(self, "api_mapping_selection_expression")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the domain name.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name. Must be between 1 and 512 characters in length.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainNameConfiguration")
    def domain_name_configuration(self) -> pulumi.Output['outputs.DomainNameDomainNameConfiguration']:
        """
        The domain name configuration.
        """
        return pulumi.get(self, "domain_name_configuration")

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> pulumi.Output[Optional['outputs.DomainNameMutualTlsAuthentication']]:
        """
        The mutual TLS authentication configuration for the domain name.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the domain name. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

