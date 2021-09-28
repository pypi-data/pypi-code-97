# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ClusterClusterEndpointArgs',
    'SafetyRuleRuleConfigArgs',
]

@pulumi.input_type
class ClusterClusterEndpointArgs:
    def __init__(__self__, *,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] endpoint: Cluster endpoint.
        :param pulumi.Input[str] region: Region of the endpoint.
        """
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster endpoint.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region of the endpoint.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class SafetyRuleRuleConfigArgs:
    def __init__(__self__, *,
                 inverted: pulumi.Input[bool],
                 threshold: pulumi.Input[int],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[bool] inverted: Logical negation of the rule.
        :param pulumi.Input[int] threshold: Number of controls that must be set when you specify an `ATLEAST` type rule.
        :param pulumi.Input[str] type: Rule type. Valid values are `ATLEAST`, `AND`, and `OR`.
        """
        pulumi.set(__self__, "inverted", inverted)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def inverted(self) -> pulumi.Input[bool]:
        """
        Logical negation of the rule.
        """
        return pulumi.get(self, "inverted")

    @inverted.setter
    def inverted(self, value: pulumi.Input[bool]):
        pulumi.set(self, "inverted", value)

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[int]:
        """
        Number of controls that must be set when you specify an `ATLEAST` type rule.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: pulumi.Input[int]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Rule type. Valid values are `ATLEAST`, `AND`, and `OR`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


