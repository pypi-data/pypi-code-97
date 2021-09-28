# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('oda.oda_root_group.command_name', 'oda'), cls=CommandGroupWithAlias, help=cli_util.override('oda.oda_root_group.help', """API to create and maintain Oracle Digital Assistant service instances."""), short_help=cli_util.override('oda.oda_root_group.short_help', """Digital Assistant Service Instance API"""))
@cli_util.help_option_group
def oda_root_group():
    pass


@click.command(cli_util.override('oda.oda_instance_group.command_name', 'oda-instance'), cls=CommandGroupWithAlias, help="""Description of `OdaServiceInstance` object.""")
@cli_util.help_option_group
def oda_instance_group():
    pass


@click.command(cli_util.override('oda.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""Description of the unexpected error that prevented completion of the request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('oda.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('oda.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The description of work request, including its status.""")
@cli_util.help_option_group
def work_request_group():
    pass


oda_root_group.add_command(oda_instance_group)
oda_root_group.add_command(work_request_error_group)
oda_root_group.add_command(work_request_log_entry_group)
oda_root_group.add_command(work_request_group)


@oda_instance_group.command(name=cli_util.override('oda.change_oda_instance_compartment.command_name', 'change-compartment'), help=u"""Moves an Digital Assistant instance into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeOdaInstanceCompartment)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""Identifier of the compartment into which the Digital Assistant instance should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_oda_instance_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, compartment_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.change_oda_instance_compartment(
        oda_instance_id=oda_instance_id,
        change_oda_instance_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.create_oda_instance.command_name', 'create'), help=u"""Starts an asynchronous job to create a Digital Assistant instance.

To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`. \n[Command Reference](createOdaInstance)""")
@cli_util.option('--compartment-id', required=True, help=u"""Identifier of the compartment.""")
@cli_util.option('--shape-name', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEVELOPMENT", "PRODUCTION"]), help=u"""Shape or size of the instance.""")
@cli_util.option('--display-name', help=u"""User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.""")
@cli_util.option('--description', help=u"""Description of the Digital Assistant instance.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'OdaInstance'})
@cli_util.wrap_exceptions
def create_oda_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, shape_name, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['shapeName'] = shape_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.create_oda_instance(
        create_oda_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(client, 'get_oda_instance') and callable(getattr(client, 'get_oda_instance')) and hasattr(result.data, 'oda_instance_id'):
                    result = client.get_oda_instance(result.data.oda_instance_id)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.delete_oda_instance.command_name', 'delete'), help=u"""Starts an asynchronous job to delete the specified Digital Assistant instance. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestID}`. \n[Command Reference](deleteOdaInstance)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_oda_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.delete_oda_instance(
        oda_instance_id=oda_instance_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.get_oda_instance.command_name', 'get'), help=u"""Gets the specified Digital Assistant instance. \n[Command Reference](getOdaInstance)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'OdaInstance'})
@cli_util.wrap_exceptions
def get_oda_instance(ctx, from_json, oda_instance_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.get_oda_instance(
        oda_instance_id=oda_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('oda.get_work_request.command_name', 'get'), help=u"""Gets information about the work request with the specified ID, including its status.

You can use this operation to monitor the status of jobs that you requested to create, delete, and update instances. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The identifier of the asynchronous work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.list_oda_instances.command_name', 'list'), help=u"""Returns a page of Digital Assistant instances that belong to the specified compartment.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listOdaInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""List the Digital Assistant instances that belong to this compartment.""")
@cli_util.option('--display-name', help=u"""List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change.

Example: `My new resource`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the Digital Assistant instances that are in this lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'list[OdaInstanceSummary]'})
@cli_util.wrap_exceptions
def list_oda_instances(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_oda_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_oda_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_oda_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('oda.list_work_request_errors.command_name', 'list'), help=u"""Returns a page of errors for the specified work request.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The identifier of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["CODE", "TIMESTAMP"]), help=u"""The field to sort by. You can specify only one sort order. If no value is specified, then the default is `TIMESTAMP`.

The default sort order for both `TIMESTAMP` and `CODE` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('oda.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a page of of log messages for a given work request.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The identifier of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["MESSAGE", "TIMESTAMP"]), help=u"""The field to sort by. You can specify only one sort order. If no value is specified, then the default is `TIMESTAMP`.

The default sort order for both `TIMESTAMP` and `MESSAGE` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('oda.list_work_requests.command_name', 'list'), help=u"""Returns a page of work requests for the specified compartment.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""List the Digital Assistant instances that belong to this compartment.""")
@cli_util.option('--oda-instance-id', help=u"""List only the information for this Digital Assistant instance.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["OPERATION_TYPE", "STATUS", "TIME_ACCEPTED", "TIME_STARTED", "TIME_FINISHED"]), help=u"""The field to sort by. You can specify only one sort order. If no value is specified, then the default is `TIME_ACCEPTED`.

The default sort order for the time fields is descending. The default order for `DISPLAYNAME` and `STATUS` is ascending.default: TIME_ACCEPTED""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, oda_instance_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if oda_instance_id is not None:
        kwargs['oda_instance_id'] = oda_instance_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.start_oda_instance.command_name', 'start'), help=u"""Starts an inactive Digital Assistant instance. Once active, the instance will be accessible and metering of requests will be started again. \n[Command Reference](startOdaInstance)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_oda_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.start_oda_instance(
        oda_instance_id=oda_instance_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.stop_oda_instance.command_name', 'stop'), help=u"""Stops an active Digital Assistant instance. Once inactive, the instance will not be accessible and metering of requests will be stopped until the instance is started again. Data associated with the instance is not affected. \n[Command Reference](stopOdaInstance)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_oda_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.stop_oda_instance(
        oda_instance_id=oda_instance_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@oda_instance_group.command(name=cli_util.override('oda.update_oda_instance.command_name', 'update'), help=u"""Updates the specified Digital Assistant instance with the information in the request body. \n[Command Reference](updateOdaInstance)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--display-name', help=u"""User-friendly name for the Digital Assistant instance.""")
@cli_util.option('--description', help=u"""Description of the Digital Assistant instance.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'OdaInstance'})
@cli_util.wrap_exceptions
def update_oda_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'oda', ctx)
    result = client.update_oda_instance(
        oda_instance_id=oda_instance_id,
        update_oda_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_oda_instance') and callable(getattr(client, 'get_oda_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_oda_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
