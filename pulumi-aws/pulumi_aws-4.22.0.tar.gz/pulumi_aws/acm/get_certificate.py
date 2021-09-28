# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, arn=None, domain=None, id=None, key_types=None, most_recent=None, status=None, statuses=None, tags=None, types=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_types and not isinstance(key_types, list):
            raise TypeError("Expected argument 'key_types' to be a list")
        pulumi.set(__self__, "key_types", key_types)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if types and not isinstance(types, list):
            raise TypeError("Expected argument 'types' to be a list")
        pulumi.set(__self__, "types", types)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the found certificate, suitable for referencing in other resources that support ACM certificates.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def domain(self) -> str:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyTypes")
    def key_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "key_types")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the found certificate.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags for the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "types")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            arn=self.arn,
            domain=self.domain,
            id=self.id,
            key_types=self.key_types,
            most_recent=self.most_recent,
            status=self.status,
            statuses=self.statuses,
            tags=self.tags,
            types=self.types)


def get_certificate(domain: Optional[str] = None,
                    key_types: Optional[Sequence[str]] = None,
                    most_recent: Optional[bool] = None,
                    statuses: Optional[Sequence[str]] = None,
                    tags: Optional[Mapping[str, str]] = None,
                    types: Optional[Sequence[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Use this data source to get the ARN of a certificate in AWS Certificate
    Manager (ACM), you can reference
    it by domain without having to hard code the ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    issued = aws.acm.get_certificate(domain="tf.example.com",
        statuses=["ISSUED"])
    amazon_issued = aws.acm.get_certificate(domain="tf.example.com",
        most_recent=True,
        types=["AMAZON_ISSUED"])
    rsa4096 = aws.acm.get_certificate(domain="tf.example.com",
        key_types=["RSA_4096"])
    ```


    :param str domain: The domain of the certificate to look up. If no certificate is found with this name, an error will be returned.
    :param Sequence[str] key_types: A list of key algorithms to filter certificates. By default, ACM does not return all certificate types when searching. Valid values are `RSA_1024`, `RSA_2048`, `RSA_4096`, `EC_prime256v1`, `EC_secp384r1`, and `EC_secp521r1`.
    :param bool most_recent: If set to true, it sorts the certificates matched by previous criteria by the NotBefore field, returning only the most recent one. If set to false, it returns an error if more than one certificate is found. Defaults to false.
    :param Sequence[str] statuses: A list of statuses on which to filter the returned list. Valid values are `PENDING_VALIDATION`, `ISSUED`,
           `INACTIVE`, `EXPIRED`, `VALIDATION_TIMED_OUT`, `REVOKED` and `FAILED`. If no value is specified, only certificates in the `ISSUED` state
           are returned.
    :param Mapping[str, str] tags: A mapping of tags for the resource.
    :param Sequence[str] types: A list of types on which to filter the returned list. Valid values are `AMAZON_ISSUED` and `IMPORTED`.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['keyTypes'] = key_types
    __args__['mostRecent'] = most_recent
    __args__['statuses'] = statuses
    __args__['tags'] = tags
    __args__['types'] = types
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:acm/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        arn=__ret__.arn,
        domain=__ret__.domain,
        id=__ret__.id,
        key_types=__ret__.key_types,
        most_recent=__ret__.most_recent,
        status=__ret__.status,
        statuses=__ret__.statuses,
        tags=__ret__.tags,
        types=__ret__.types)


@_utilities.lift_output_func(get_certificate)
def get_certificate_output(domain: Optional[pulumi.Input[str]] = None,
                           key_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           most_recent: Optional[pulumi.Input[Optional[bool]]] = None,
                           statuses: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                           types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Use this data source to get the ARN of a certificate in AWS Certificate
    Manager (ACM), you can reference
    it by domain without having to hard code the ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    issued = aws.acm.get_certificate(domain="tf.example.com",
        statuses=["ISSUED"])
    amazon_issued = aws.acm.get_certificate(domain="tf.example.com",
        most_recent=True,
        types=["AMAZON_ISSUED"])
    rsa4096 = aws.acm.get_certificate(domain="tf.example.com",
        key_types=["RSA_4096"])
    ```


    :param str domain: The domain of the certificate to look up. If no certificate is found with this name, an error will be returned.
    :param Sequence[str] key_types: A list of key algorithms to filter certificates. By default, ACM does not return all certificate types when searching. Valid values are `RSA_1024`, `RSA_2048`, `RSA_4096`, `EC_prime256v1`, `EC_secp384r1`, and `EC_secp521r1`.
    :param bool most_recent: If set to true, it sorts the certificates matched by previous criteria by the NotBefore field, returning only the most recent one. If set to false, it returns an error if more than one certificate is found. Defaults to false.
    :param Sequence[str] statuses: A list of statuses on which to filter the returned list. Valid values are `PENDING_VALIDATION`, `ISSUED`,
           `INACTIVE`, `EXPIRED`, `VALIDATION_TIMED_OUT`, `REVOKED` and `FAILED`. If no value is specified, only certificates in the `ISSUED` state
           are returned.
    :param Mapping[str, str] tags: A mapping of tags for the resource.
    :param Sequence[str] types: A list of types on which to filter the returned list. Valid values are `AMAZON_ISSUED` and `IMPORTED`.
    """
    ...
