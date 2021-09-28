# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BaiduChannelArgs', 'BaiduChannel']

@pulumi.input_type
class BaiduChannelArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 application_id: pulumi.Input[str],
                 secret_key: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a BaiduChannel resource.
        :param pulumi.Input[str] api_key: Platform credential API key from Baidu.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[str] secret_key: Platform credential Secret key from Baidu.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
        """
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "secret_key", secret_key)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        Platform credential API key from Baidu.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        The application ID.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Input[str]:
        """
        Platform credential Secret key from Baidu.
        """
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_key", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to enable the channel. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class _BaiduChannelState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BaiduChannel resources.
        :param pulumi.Input[str] api_key: Platform credential API key from Baidu.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
        :param pulumi.Input[str] secret_key: Platform credential Secret key from Baidu.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if secret_key is not None:
            pulumi.set(__self__, "secret_key", secret_key)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        Platform credential API key from Baidu.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The application ID.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to enable the channel. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        Platform credential Secret key from Baidu.
        """
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_key", value)


class BaiduChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Pinpoint Baidu Channel resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        app = aws.pinpoint.App("app")
        channel = aws.pinpoint.BaiduChannel("channel",
            application_id=app.application_id,
            api_key="",
            secret_key="")
        ```

        ## Import

        Pinpoint Baidu Channel can be imported using the `application-id`, e.g.

        ```sh
         $ pulumi import aws:pinpoint/baiduChannel:BaiduChannel channel application-id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: Platform credential API key from Baidu.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
        :param pulumi.Input[str] secret_key: Platform credential Secret key from Baidu.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BaiduChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Pinpoint Baidu Channel resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        app = aws.pinpoint.App("app")
        channel = aws.pinpoint.BaiduChannel("channel",
            application_id=app.application_id,
            api_key="",
            secret_key="")
        ```

        ## Import

        Pinpoint Baidu Channel can be imported using the `application-id`, e.g.

        ```sh
         $ pulumi import aws:pinpoint/baiduChannel:BaiduChannel channel application-id
        ```

        :param str resource_name: The name of the resource.
        :param BaiduChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BaiduChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
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
            __props__ = BaiduChannelArgs.__new__(BaiduChannelArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = api_key
            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["enabled"] = enabled
            if secret_key is None and not opts.urn:
                raise TypeError("Missing required property 'secret_key'")
            __props__.__dict__["secret_key"] = secret_key
        super(BaiduChannel, __self__).__init__(
            'aws:pinpoint/baiduChannel:BaiduChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            secret_key: Optional[pulumi.Input[str]] = None) -> 'BaiduChannel':
        """
        Get an existing BaiduChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: Platform credential API key from Baidu.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
        :param pulumi.Input[str] secret_key: Platform credential Secret key from Baidu.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BaiduChannelState.__new__(_BaiduChannelState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["secret_key"] = secret_key
        return BaiduChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        Platform credential API key from Baidu.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The application ID.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to enable the channel. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[str]:
        """
        Platform credential Secret key from Baidu.
        """
        return pulumi.get(self, "secret_key")

