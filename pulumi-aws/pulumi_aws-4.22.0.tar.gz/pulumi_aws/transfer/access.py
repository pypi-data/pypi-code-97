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

__all__ = ['AccessArgs', 'Access']

@pulumi.input_type
class AccessArgs:
    def __init__(__self__, *,
                 external_id: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input['AccessPosixProfileArgs']] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Access resource.
        :param pulumi.Input[str] external_id: The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        :param pulumi.Input[str] home_directory: The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        :param pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]] home_directory_mappings: Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        :param pulumi.Input[str] home_directory_type: The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        :param pulumi.Input['AccessPosixProfileArgs'] posix_profile: Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        :param pulumi.Input[str] role: Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        """
        pulumi.set(__self__, "external_id", external_id)
        pulumi.set(__self__, "server_id", server_id)
        if home_directory is not None:
            pulumi.set(__self__, "home_directory", home_directory)
        if home_directory_mappings is not None:
            pulumi.set(__self__, "home_directory_mappings", home_directory_mappings)
        if home_directory_type is not None:
            pulumi.set(__self__, "home_directory_type", home_directory_type)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if posix_profile is not None:
            pulumi.set(__self__, "posix_profile", posix_profile)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[str]:
        """
        The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        """
        return pulumi.get(self, "home_directory")

    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory", value)

    @property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]]]:
        """
        Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        """
        return pulumi.get(self, "home_directory_mappings")

    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]]]):
        pulumi.set(self, "home_directory_mappings", value)

    @property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        """
        return pulumi.get(self, "home_directory_type")

    @home_directory_type.setter
    def home_directory_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory_type", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> Optional[pulumi.Input['AccessPosixProfileArgs']]:
        """
        Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        """
        return pulumi.get(self, "posix_profile")

    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input['AccessPosixProfileArgs']]):
        pulumi.set(self, "posix_profile", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


@pulumi.input_type
class _AccessState:
    def __init__(__self__, *,
                 external_id: Optional[pulumi.Input[str]] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input['AccessPosixProfileArgs']] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Access resources.
        :param pulumi.Input[str] external_id: The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        :param pulumi.Input[str] home_directory: The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        :param pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]] home_directory_mappings: Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        :param pulumi.Input[str] home_directory_type: The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        :param pulumi.Input['AccessPosixProfileArgs'] posix_profile: Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        :param pulumi.Input[str] role: Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if home_directory is not None:
            pulumi.set(__self__, "home_directory", home_directory)
        if home_directory_mappings is not None:
            pulumi.set(__self__, "home_directory_mappings", home_directory_mappings)
        if home_directory_type is not None:
            pulumi.set(__self__, "home_directory_type", home_directory_type)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if posix_profile is not None:
            pulumi.set(__self__, "posix_profile", posix_profile)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        """
        return pulumi.get(self, "home_directory")

    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory", value)

    @property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]]]:
        """
        Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        """
        return pulumi.get(self, "home_directory_mappings")

    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessHomeDirectoryMappingArgs']]]]):
        pulumi.set(self, "home_directory_mappings", value)

    @property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        """
        return pulumi.get(self, "home_directory_type")

    @home_directory_type.setter
    def home_directory_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory_type", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> Optional[pulumi.Input['AccessPosixProfileArgs']]:
        """
        Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        """
        return pulumi.get(self, "posix_profile")

    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input['AccessPosixProfileArgs']]):
        pulumi.set(self, "posix_profile", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)


class Access(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessHomeDirectoryMappingArgs']]]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input[pulumi.InputType['AccessPosixProfileArgs']]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a AWS Transfer Access resource.

        ## Example Usage
        ### Basic S3

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.transfer.Access("example",
            external_id="S-1-1-12-1234567890-123456789-1234567890-1234",
            server_id=aws_transfer_server["example"]["id"],
            role=aws_iam_role["example"]["arn"],
            home_directory=f"/{aws_s3_bucket['example']['id']}/")
        ```
        ### Basic EFS

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.transfer.Access("test",
            external_id="S-1-1-12-1234567890-123456789-1234567890-1234",
            server_id=aws_transfer_server["test"]["id"],
            role=aws_iam_role["test"]["arn"],
            home_directory=f"/{aws_efs_file_system['test']['id']}/",
            posix_profile=aws.transfer.AccessPosixProfileArgs(
                gid=1000,
                uid=1000,
            ))
        ```

        ## Import

        Transfer Accesses can be imported using the `server_id` and `external_id`, e.g.

        ```sh
         $ pulumi import aws:transfer/access:Access example s-12345678/S-1-1-12-1234567890-123456789-1234567890-1234
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] external_id: The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        :param pulumi.Input[str] home_directory: The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessHomeDirectoryMappingArgs']]]] home_directory_mappings: Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        :param pulumi.Input[str] home_directory_type: The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        :param pulumi.Input[pulumi.InputType['AccessPosixProfileArgs']] posix_profile: Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        :param pulumi.Input[str] role: Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a AWS Transfer Access resource.

        ## Example Usage
        ### Basic S3

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.transfer.Access("example",
            external_id="S-1-1-12-1234567890-123456789-1234567890-1234",
            server_id=aws_transfer_server["example"]["id"],
            role=aws_iam_role["example"]["arn"],
            home_directory=f"/{aws_s3_bucket['example']['id']}/")
        ```
        ### Basic EFS

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.transfer.Access("test",
            external_id="S-1-1-12-1234567890-123456789-1234567890-1234",
            server_id=aws_transfer_server["test"]["id"],
            role=aws_iam_role["test"]["arn"],
            home_directory=f"/{aws_efs_file_system['test']['id']}/",
            posix_profile=aws.transfer.AccessPosixProfileArgs(
                gid=1000,
                uid=1000,
            ))
        ```

        ## Import

        Transfer Accesses can be imported using the `server_id` and `external_id`, e.g.

        ```sh
         $ pulumi import aws:transfer/access:Access example s-12345678/S-1-1-12-1234567890-123456789-1234567890-1234
        ```

        :param str resource_name: The name of the resource.
        :param AccessArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessHomeDirectoryMappingArgs']]]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input[pulumi.InputType['AccessPosixProfileArgs']]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessArgs.__new__(AccessArgs)

            if external_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_id'")
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["home_directory"] = home_directory
            __props__.__dict__["home_directory_mappings"] = home_directory_mappings
            __props__.__dict__["home_directory_type"] = home_directory_type
            __props__.__dict__["policy"] = policy
            __props__.__dict__["posix_profile"] = posix_profile
            __props__.__dict__["role"] = role
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
        super(Access, __self__).__init__(
            'aws:transfer/access:Access',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            external_id: Optional[pulumi.Input[str]] = None,
            home_directory: Optional[pulumi.Input[str]] = None,
            home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessHomeDirectoryMappingArgs']]]]] = None,
            home_directory_type: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            posix_profile: Optional[pulumi.Input[pulumi.InputType['AccessPosixProfileArgs']]] = None,
            role: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None) -> 'Access':
        """
        Get an existing Access resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] external_id: The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        :param pulumi.Input[str] home_directory: The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessHomeDirectoryMappingArgs']]]] home_directory_mappings: Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        :param pulumi.Input[str] home_directory_type: The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        :param pulumi.Input[pulumi.InputType['AccessPosixProfileArgs']] posix_profile: Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        :param pulumi.Input[str] role: Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessState.__new__(_AccessState)

        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["home_directory"] = home_directory
        __props__.__dict__["home_directory_mappings"] = home_directory_mappings
        __props__.__dict__["home_directory_type"] = home_directory_type
        __props__.__dict__["policy"] = policy
        __props__.__dict__["posix_profile"] = posix_profile
        __props__.__dict__["role"] = role
        __props__.__dict__["server_id"] = server_id
        return Access(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        The SID of a group in the directory connected to the Transfer Server (e.g. `S-1-1-12-1234567890-123456789-1234567890-1234`)
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[str]]:
        """
        The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        """
        return pulumi.get(self, "home_directory")

    @property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.AccessHomeDirectoryMapping']]]:
        """
        Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. See Home Directory Mappings below.
        """
        return pulumi.get(self, "home_directory_mappings")

    @property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
        """
        return pulumi.get(self, "home_directory_type")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> pulumi.Output[Optional['outputs.AccessPosixProfile']]:
        """
        Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. See Posix Profile below.
        """
        return pulumi.get(self, "posix_profile")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        return pulumi.get(self, "server_id")

