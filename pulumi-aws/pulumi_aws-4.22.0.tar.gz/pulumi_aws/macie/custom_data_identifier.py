# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CustomDataIdentifierArgs', 'CustomDataIdentifier']

@pulumi.input_type
class CustomDataIdentifierArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 ignore_words: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 maximum_match_distance: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 regex: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CustomDataIdentifier resource.
        :param pulumi.Input[str] description: A custom description of the custom data identifier. The description can contain as many as 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ignore_words: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keywords: An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        :param pulumi.Input[int] maximum_match_distance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] regex: The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ignore_words is not None:
            pulumi.set(__self__, "ignore_words", ignore_words)
        if keywords is not None:
            pulumi.set(__self__, "keywords", keywords)
        if maximum_match_distance is not None:
            pulumi.set(__self__, "maximum_match_distance", maximum_match_distance)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A custom description of the custom data identifier. The description can contain as many as 512 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ignoreWords")
    def ignore_words(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        """
        return pulumi.get(self, "ignore_words")

    @ignore_words.setter
    def ignore_words(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ignore_words", value)

    @property
    @pulumi.getter
    def keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        """
        return pulumi.get(self, "keywords")

    @keywords.setter
    def keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "keywords", value)

    @property
    @pulumi.getter(name="maximumMatchDistance")
    def maximum_match_distance(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        """
        return pulumi.get(self, "maximum_match_distance")

    @maximum_match_distance.setter
    def maximum_match_distance(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_match_distance", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[str]]:
        """
        The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        """
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "regex", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _CustomDataIdentifierState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ignore_words: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 maximum_match_distance: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 regex: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering CustomDataIdentifier resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the custom data identifier.
        :param pulumi.Input[str] created_at: The date and time, in UTC and extended RFC 3339 format, when the Amazon Macie account was created.
        :param pulumi.Input[str] description: A custom description of the custom data identifier. The description can contain as many as 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ignore_words: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keywords: An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        :param pulumi.Input[int] maximum_match_distance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] regex: The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ignore_words is not None:
            pulumi.set(__self__, "ignore_words", ignore_words)
        if keywords is not None:
            pulumi.set(__self__, "keywords", keywords)
        if maximum_match_distance is not None:
            pulumi.set(__self__, "maximum_match_distance", maximum_match_distance)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the custom data identifier.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time, in UTC and extended RFC 3339 format, when the Amazon Macie account was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A custom description of the custom data identifier. The description can contain as many as 512 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ignoreWords")
    def ignore_words(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        """
        return pulumi.get(self, "ignore_words")

    @ignore_words.setter
    def ignore_words(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ignore_words", value)

    @property
    @pulumi.getter
    def keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        """
        return pulumi.get(self, "keywords")

    @keywords.setter
    def keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "keywords", value)

    @property
    @pulumi.getter(name="maximumMatchDistance")
    def maximum_match_distance(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        """
        return pulumi.get(self, "maximum_match_distance")

    @maximum_match_distance.setter
    def maximum_match_distance(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_match_distance", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[str]]:
        """
        The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        """
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "regex", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
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


class CustomDataIdentifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ignore_words: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 maximum_match_distance: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 regex: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a resource to manage an [AWS Macie Custom Data Identifier](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-id.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_account = aws.macie2.Account("exampleAccount")
        example_custom_data_identifier = aws.macie.CustomDataIdentifier("exampleCustomDataIdentifier",
            regex="[0-9]{3}-[0-9]{2}-[0-9]{4}",
            description="DESCRIPTION",
            maximum_match_distance=10,
            keywords=["keyword"],
            ignore_words=["ignore"],
            opts=pulumi.ResourceOptions(depends_on=[aws_macie2_account["test"]]))
        ```

        ## Import

        `aws_macie2_custom_data_identifier` can be imported using the id, e.g.

        ```sh
         $ pulumi import aws:macie/customDataIdentifier:CustomDataIdentifier example abcd1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A custom description of the custom data identifier. The description can contain as many as 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ignore_words: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keywords: An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        :param pulumi.Input[int] maximum_match_distance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] regex: The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CustomDataIdentifierArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage an [AWS Macie Custom Data Identifier](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-id.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_account = aws.macie2.Account("exampleAccount")
        example_custom_data_identifier = aws.macie.CustomDataIdentifier("exampleCustomDataIdentifier",
            regex="[0-9]{3}-[0-9]{2}-[0-9]{4}",
            description="DESCRIPTION",
            maximum_match_distance=10,
            keywords=["keyword"],
            ignore_words=["ignore"],
            opts=pulumi.ResourceOptions(depends_on=[aws_macie2_account["test"]]))
        ```

        ## Import

        `aws_macie2_custom_data_identifier` can be imported using the id, e.g.

        ```sh
         $ pulumi import aws:macie/customDataIdentifier:CustomDataIdentifier example abcd1
        ```

        :param str resource_name: The name of the resource.
        :param CustomDataIdentifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomDataIdentifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ignore_words: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 maximum_match_distance: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 regex: Optional[pulumi.Input[str]] = None,
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
            __props__ = CustomDataIdentifierArgs.__new__(CustomDataIdentifierArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["ignore_words"] = ignore_words
            __props__.__dict__["keywords"] = keywords
            __props__.__dict__["maximum_match_distance"] = maximum_match_distance
            __props__.__dict__["name"] = name
            __props__.__dict__["name_prefix"] = name_prefix
            __props__.__dict__["regex"] = regex
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["tags_all"] = None
        super(CustomDataIdentifier, __self__).__init__(
            'aws:macie/customDataIdentifier:CustomDataIdentifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ignore_words: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            maximum_match_distance: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            regex: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'CustomDataIdentifier':
        """
        Get an existing CustomDataIdentifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the custom data identifier.
        :param pulumi.Input[str] created_at: The date and time, in UTC and extended RFC 3339 format, when the Amazon Macie account was created.
        :param pulumi.Input[str] description: A custom description of the custom data identifier. The description can contain as many as 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ignore_words: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keywords: An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        :param pulumi.Input[int] maximum_match_distance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] regex: The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomDataIdentifierState.__new__(_CustomDataIdentifierState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["ignore_words"] = ignore_words
        __props__.__dict__["keywords"] = keywords
        __props__.__dict__["maximum_match_distance"] = maximum_match_distance
        __props__.__dict__["name"] = name
        __props__.__dict__["name_prefix"] = name_prefix
        __props__.__dict__["regex"] = regex
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return CustomDataIdentifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the custom data identifier.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date and time, in UTC and extended RFC 3339 format, when the Amazon Macie account was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A custom description of the custom data identifier. The description can contain as many as 512 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ignoreWords")
    def ignore_words(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters. Ignore words are case sensitive.
        """
        return pulumi.get(self, "ignore_words")

    @property
    @pulumi.getter
    def keywords(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An array that lists specific character sequences (keywords), one of which must be within proximity (`maximum_match_distance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3 - 90 characters. Keywords aren't case sensitive.
        """
        return pulumi.get(self, "keywords")

    @property
    @pulumi.getter(name="maximumMatchDistance")
    def maximum_match_distance(self) -> pulumi.Output[int]:
        """
        The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 50.
        """
        return pulumi.get(self, "maximum_match_distance")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[str]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter
    def regex(self) -> pulumi.Output[Optional[str]]:
        """
        The regular expression (regex) that defines the pattern to match. The expression can contain as many as 512 characters.
        """
        return pulumi.get(self, "regex")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of key-value pairs that specifies the tags to associate with the custom data identifier.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

