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

__all__ = [
    'GetVpcsResult',
    'AwaitableGetVpcsResult',
    'get_vpcs',
    'get_vpcs_output',
]

@pulumi.output_type
class GetVpcsResult:
    """
    A collection of values returned by getVpcs.
    """
    def __init__(__self__, filters=None, id=None, ids=None, tags=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVpcsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of all the VPC Ids found. This data source will fail if none are found.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")


class AwaitableGetVpcsResult(GetVpcsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcsResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            tags=self.tags)


def get_vpcs(filters: Optional[Sequence[pulumi.InputType['GetVpcsFilterArgs']]] = None,
             tags: Optional[Mapping[str, str]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcsResult:
    """
    This resource can be useful for getting back a list of VPC Ids for a region.

    The following example retrieves a list of VPC Ids with a custom tag of `service` set to a value of "production".


    :param Sequence[pulumi.InputType['GetVpcsFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired vpcs.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcs:getVpcs', __args__, opts=opts, typ=GetVpcsResult).value

    return AwaitableGetVpcsResult(
        filters=__ret__.filters,
        id=__ret__.id,
        ids=__ret__.ids,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_vpcs)
def get_vpcs_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVpcsFilterArgs']]]]] = None,
                    tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcsResult]:
    """
    This resource can be useful for getting back a list of VPC Ids for a region.

    The following example retrieves a list of VPC Ids with a custom tag of `service` set to a value of "production".


    :param Sequence[pulumi.InputType['GetVpcsFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired vpcs.
    """
    ...
