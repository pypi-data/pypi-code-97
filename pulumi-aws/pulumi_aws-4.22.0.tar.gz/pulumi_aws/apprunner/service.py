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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 service_name: pulumi.Input[str],
                 source_configuration: pulumi.Input['ServiceSourceConfigurationArgs'],
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
                 encryption_configuration: Optional[pulumi.Input['ServiceEncryptionConfigurationArgs']] = None,
                 health_check_configuration: Optional[pulumi.Input['ServiceHealthCheckConfigurationArgs']] = None,
                 instance_configuration: Optional[pulumi.Input['ServiceInstanceConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] service_name: Name of the service.
        :param pulumi.Input['ServiceSourceConfigurationArgs'] source_configuration: The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        :param pulumi.Input[str] auto_scaling_configuration_arn: ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        :param pulumi.Input['ServiceEncryptionConfigurationArgs'] encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        :param pulumi.Input['ServiceHealthCheckConfigurationArgs'] health_check_configuration: Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        :param pulumi.Input['ServiceInstanceConfigurationArgs'] instance_configuration: The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "source_configuration", source_configuration)
        if auto_scaling_configuration_arn is not None:
            pulumi.set(__self__, "auto_scaling_configuration_arn", auto_scaling_configuration_arn)
        if encryption_configuration is not None:
            pulumi.set(__self__, "encryption_configuration", encryption_configuration)
        if health_check_configuration is not None:
            pulumi.set(__self__, "health_check_configuration", health_check_configuration)
        if instance_configuration is not None:
            pulumi.set(__self__, "instance_configuration", instance_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> pulumi.Input['ServiceSourceConfigurationArgs']:
        """
        The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        """
        return pulumi.get(self, "source_configuration")

    @source_configuration.setter
    def source_configuration(self, value: pulumi.Input['ServiceSourceConfigurationArgs']):
        pulumi.set(self, "source_configuration", value)

    @property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        """
        return pulumi.get(self, "auto_scaling_configuration_arn")

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_scaling_configuration_arn", value)

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input['ServiceEncryptionConfigurationArgs']]:
        """
        An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        """
        return pulumi.get(self, "encryption_configuration")

    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input['ServiceEncryptionConfigurationArgs']]):
        pulumi.set(self, "encryption_configuration", value)

    @property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(self) -> Optional[pulumi.Input['ServiceHealthCheckConfigurationArgs']]:
        """
        Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        """
        return pulumi.get(self, "health_check_configuration")

    @health_check_configuration.setter
    def health_check_configuration(self, value: Optional[pulumi.Input['ServiceHealthCheckConfigurationArgs']]):
        pulumi.set(self, "health_check_configuration", value)

    @property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> Optional[pulumi.Input['ServiceInstanceConfigurationArgs']]:
        """
        The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        """
        return pulumi.get(self, "instance_configuration")

    @instance_configuration.setter
    def instance_configuration(self, value: Optional[pulumi.Input['ServiceInstanceConfigurationArgs']]):
        pulumi.set(self, "instance_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ServiceState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
                 encryption_configuration: Optional[pulumi.Input['ServiceEncryptionConfigurationArgs']] = None,
                 health_check_configuration: Optional[pulumi.Input['ServiceHealthCheckConfigurationArgs']] = None,
                 instance_configuration: Optional[pulumi.Input['ServiceInstanceConfigurationArgs']] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_url: Optional[pulumi.Input[str]] = None,
                 source_configuration: Optional[pulumi.Input['ServiceSourceConfigurationArgs']] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Service resources.
        :param pulumi.Input[str] arn: ARN of the App Runner service.
        :param pulumi.Input[str] auto_scaling_configuration_arn: ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        :param pulumi.Input['ServiceEncryptionConfigurationArgs'] encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        :param pulumi.Input['ServiceHealthCheckConfigurationArgs'] health_check_configuration: Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        :param pulumi.Input['ServiceInstanceConfigurationArgs'] instance_configuration: The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        :param pulumi.Input[str] service_id: An alphanumeric ID that App Runner generated for this service. Unique within the AWS Region.
        :param pulumi.Input[str] service_name: Name of the service.
        :param pulumi.Input[str] service_url: A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.
        :param pulumi.Input['ServiceSourceConfigurationArgs'] source_configuration: The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        :param pulumi.Input[str] status: The current state of the App Runner service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if auto_scaling_configuration_arn is not None:
            pulumi.set(__self__, "auto_scaling_configuration_arn", auto_scaling_configuration_arn)
        if encryption_configuration is not None:
            pulumi.set(__self__, "encryption_configuration", encryption_configuration)
        if health_check_configuration is not None:
            pulumi.set(__self__, "health_check_configuration", health_check_configuration)
        if instance_configuration is not None:
            pulumi.set(__self__, "instance_configuration", instance_configuration)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if service_url is not None:
            pulumi.set(__self__, "service_url", service_url)
        if source_configuration is not None:
            pulumi.set(__self__, "source_configuration", source_configuration)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the App Runner service.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        """
        return pulumi.get(self, "auto_scaling_configuration_arn")

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_scaling_configuration_arn", value)

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input['ServiceEncryptionConfigurationArgs']]:
        """
        An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        """
        return pulumi.get(self, "encryption_configuration")

    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input['ServiceEncryptionConfigurationArgs']]):
        pulumi.set(self, "encryption_configuration", value)

    @property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(self) -> Optional[pulumi.Input['ServiceHealthCheckConfigurationArgs']]:
        """
        Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        """
        return pulumi.get(self, "health_check_configuration")

    @health_check_configuration.setter
    def health_check_configuration(self, value: Optional[pulumi.Input['ServiceHealthCheckConfigurationArgs']]):
        pulumi.set(self, "health_check_configuration", value)

    @property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> Optional[pulumi.Input['ServiceInstanceConfigurationArgs']]:
        """
        The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        """
        return pulumi.get(self, "instance_configuration")

    @instance_configuration.setter
    def instance_configuration(self, value: Optional[pulumi.Input['ServiceInstanceConfigurationArgs']]):
        pulumi.set(self, "instance_configuration", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[str]]:
        """
        An alphanumeric ID that App Runner generated for this service. Unique within the AWS Region.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> Optional[pulumi.Input[str]]:
        """
        A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.
        """
        return pulumi.get(self, "service_url")

    @service_url.setter
    def service_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_url", value)

    @property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> Optional[pulumi.Input['ServiceSourceConfigurationArgs']]:
        """
        The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        """
        return pulumi.get(self, "source_configuration")

    @source_configuration.setter
    def source_configuration(self, value: Optional[pulumi.Input['ServiceSourceConfigurationArgs']]):
        pulumi.set(self, "source_configuration", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the App Runner service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
                 encryption_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceEncryptionConfigurationArgs']]] = None,
                 health_check_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceHealthCheckConfigurationArgs']]] = None,
                 instance_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceInstanceConfigurationArgs']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 source_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceSourceConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an App Runner Service.

        ## Example Usage
        ### Service with a Code Repository Source

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apprunner.Service("example",
            service_name="example",
            source_configuration=aws.apprunner.ServiceSourceConfigurationArgs(
                authentication_configuration=aws.apprunner.ServiceSourceConfigurationAuthenticationConfigurationArgs(
                    connection_arn=aws_apprunner_connection["example"]["arn"],
                ),
                code_repository=aws.apprunner.ServiceSourceConfigurationCodeRepositoryArgs(
                    code_configuration=aws.apprunner.ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgs(
                        code_configuration_values=aws.apprunner.ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgs(
                            build_command="python setup.py develop",
                            port="8000",
                            runtime="PYTHON_3",
                            start_command="python runapp.py",
                        ),
                        configuration_source="API",
                    ),
                    repository_url="https://github.com/example/my-example-python-app",
                    source_code_version=aws.apprunner.ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgs(
                        type="BRANCH",
                        value="main",
                    ),
                ),
            ),
            tags={
                "Name": "example-apprunner-service",
            })
        ```
        ### Service with an Image Repository Source

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apprunner.Service("example",
            service_name="example",
            source_configuration=aws.apprunner.ServiceSourceConfigurationArgs(
                image_repository=aws.apprunner.ServiceSourceConfigurationImageRepositoryArgs(
                    image_configuration=aws.apprunner.ServiceSourceConfigurationImageRepositoryImageConfigurationArgs(
                        port="8000",
                    ),
                    image_identifier="public.ecr.aws/jg/hello:latest",
                    image_repository_type="ECR_PUBLIC",
                ),
            ),
            tags={
                "Name": "example-apprunner-service",
            })
        ```

        ## Import

        App Runner Services can be imported by using the `arn`, e.g.

        ```sh
         $ pulumi import aws:apprunner/service:Service example arn:aws:apprunner:us-east-1:1234567890:service/example/0a03292a89764e5882c41d8f991c82fe
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_scaling_configuration_arn: ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        :param pulumi.Input[pulumi.InputType['ServiceEncryptionConfigurationArgs']] encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        :param pulumi.Input[pulumi.InputType['ServiceHealthCheckConfigurationArgs']] health_check_configuration: Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        :param pulumi.Input[pulumi.InputType['ServiceInstanceConfigurationArgs']] instance_configuration: The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        :param pulumi.Input[str] service_name: Name of the service.
        :param pulumi.Input[pulumi.InputType['ServiceSourceConfigurationArgs']] source_configuration: The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an App Runner Service.

        ## Example Usage
        ### Service with a Code Repository Source

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apprunner.Service("example",
            service_name="example",
            source_configuration=aws.apprunner.ServiceSourceConfigurationArgs(
                authentication_configuration=aws.apprunner.ServiceSourceConfigurationAuthenticationConfigurationArgs(
                    connection_arn=aws_apprunner_connection["example"]["arn"],
                ),
                code_repository=aws.apprunner.ServiceSourceConfigurationCodeRepositoryArgs(
                    code_configuration=aws.apprunner.ServiceSourceConfigurationCodeRepositoryCodeConfigurationArgs(
                        code_configuration_values=aws.apprunner.ServiceSourceConfigurationCodeRepositoryCodeConfigurationCodeConfigurationValuesArgs(
                            build_command="python setup.py develop",
                            port="8000",
                            runtime="PYTHON_3",
                            start_command="python runapp.py",
                        ),
                        configuration_source="API",
                    ),
                    repository_url="https://github.com/example/my-example-python-app",
                    source_code_version=aws.apprunner.ServiceSourceConfigurationCodeRepositorySourceCodeVersionArgs(
                        type="BRANCH",
                        value="main",
                    ),
                ),
            ),
            tags={
                "Name": "example-apprunner-service",
            })
        ```
        ### Service with an Image Repository Source

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apprunner.Service("example",
            service_name="example",
            source_configuration=aws.apprunner.ServiceSourceConfigurationArgs(
                image_repository=aws.apprunner.ServiceSourceConfigurationImageRepositoryArgs(
                    image_configuration=aws.apprunner.ServiceSourceConfigurationImageRepositoryImageConfigurationArgs(
                        port="8000",
                    ),
                    image_identifier="public.ecr.aws/jg/hello:latest",
                    image_repository_type="ECR_PUBLIC",
                ),
            ),
            tags={
                "Name": "example-apprunner-service",
            })
        ```

        ## Import

        App Runner Services can be imported by using the `arn`, e.g.

        ```sh
         $ pulumi import aws:apprunner/service:Service example arn:aws:apprunner:us-east-1:1234567890:service/example/0a03292a89764e5882c41d8f991c82fe
        ```

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
                 encryption_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceEncryptionConfigurationArgs']]] = None,
                 health_check_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceHealthCheckConfigurationArgs']]] = None,
                 instance_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceInstanceConfigurationArgs']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 source_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceSourceConfigurationArgs']]] = None,
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
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
            __props__.__dict__["encryption_configuration"] = encryption_configuration
            __props__.__dict__["health_check_configuration"] = health_check_configuration
            __props__.__dict__["instance_configuration"] = instance_configuration
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if source_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'source_configuration'")
            __props__.__dict__["source_configuration"] = source_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["service_id"] = None
            __props__.__dict__["service_url"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["tags_all"] = None
        super(Service, __self__).__init__(
            'aws:apprunner/service:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            auto_scaling_configuration_arn: Optional[pulumi.Input[str]] = None,
            encryption_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceEncryptionConfigurationArgs']]] = None,
            health_check_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceHealthCheckConfigurationArgs']]] = None,
            instance_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceInstanceConfigurationArgs']]] = None,
            service_id: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            service_url: Optional[pulumi.Input[str]] = None,
            source_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceSourceConfigurationArgs']]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the App Runner service.
        :param pulumi.Input[str] auto_scaling_configuration_arn: ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        :param pulumi.Input[pulumi.InputType['ServiceEncryptionConfigurationArgs']] encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        :param pulumi.Input[pulumi.InputType['ServiceHealthCheckConfigurationArgs']] health_check_configuration: Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        :param pulumi.Input[pulumi.InputType['ServiceInstanceConfigurationArgs']] instance_configuration: The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        :param pulumi.Input[str] service_id: An alphanumeric ID that App Runner generated for this service. Unique within the AWS Region.
        :param pulumi.Input[str] service_name: Name of the service.
        :param pulumi.Input[str] service_url: A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.
        :param pulumi.Input[pulumi.InputType['ServiceSourceConfigurationArgs']] source_configuration: The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        :param pulumi.Input[str] status: The current state of the App Runner service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceState.__new__(_ServiceState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        __props__.__dict__["encryption_configuration"] = encryption_configuration
        __props__.__dict__["health_check_configuration"] = health_check_configuration
        __props__.__dict__["instance_configuration"] = instance_configuration
        __props__.__dict__["service_id"] = service_id
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["service_url"] = service_url
        __props__.__dict__["source_configuration"] = source_configuration
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the App Runner service.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> pulumi.Output[str]:
        """
        ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
        """
        return pulumi.get(self, "auto_scaling_configuration_arn")

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[Optional['outputs.ServiceEncryptionConfiguration']]:
        """
        An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed CMK. See Encryption Configuration below for more details.
        """
        return pulumi.get(self, "encryption_configuration")

    @property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(self) -> pulumi.Output['outputs.ServiceHealthCheckConfiguration']:
        """
        Settings of the health check that AWS App Runner performs to monitor the health of your service. See Health Check Configuration below for more details.
        """
        return pulumi.get(self, "health_check_configuration")

    @property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> pulumi.Output['outputs.ServiceInstanceConfiguration']:
        """
        The runtime configuration of instances (scaling units) of the App Runner service. See Instance Configuration below for more details.
        """
        return pulumi.get(self, "instance_configuration")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[str]:
        """
        An alphanumeric ID that App Runner generated for this service. Unique within the AWS Region.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> pulumi.Output[str]:
        """
        A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.
        """
        return pulumi.get(self, "service_url")

    @property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> pulumi.Output['outputs.ServiceSourceConfiguration']:
        """
        The source to deploy to the App Runner service. Can be a code or an image repository. See Source Configuration below for more details.
        """
        return pulumi.get(self, "source_configuration")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The current state of the App Runner service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

