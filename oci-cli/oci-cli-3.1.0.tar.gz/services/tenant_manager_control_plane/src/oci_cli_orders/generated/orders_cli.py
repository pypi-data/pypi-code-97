# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('orders.orders_root_group.command_name', 'orders'), cls=CommandGroupWithAlias, help=cli_util.override('orders.orders_root_group.help', """The Organizations API allows you to consolidate multiple OCI tenancies into an organization, and centrally manage your tenancies and its resources."""), short_help=cli_util.override('orders.orders_root_group.short_help', """Organizations API"""))
@cli_util.help_option_group
def orders_root_group():
    pass


@click.command(cli_util.override('orders.order_group.command_name', 'order'), cls=CommandGroupWithAlias, help="""Order Details for Console plugin display""")
@cli_util.help_option_group
def order_group():
    pass


organizations_service_cli.organizations_service_group.add_command(orders_root_group)
orders_root_group.add_command(order_group)


@order_group.command(name=cli_util.override('orders.activate_order.command_name', 'activate'), help=u"""Triggers an order activation workflow on behalf of the tenant given by compartment id in the body. \n[Command Reference](activateOrder)""")
@cli_util.option('--compartment-id', required=True, help=u"""Tenant Id to activate the Order.""")
@cli_util.option('--activation-token', required=True, help=u"""Activation Token containing an order id. JWT RFC 7519 formatted string.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def activate_order(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, activation_token):

    if isinstance(activation_token, six.string_types) and len(activation_token.strip()) == 0:
        raise click.UsageError('Parameter --activation-token cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('tenant_manager_control_plane', 'orders', ctx)
    result = client.activate_order(
        activation_token=activation_token,
        activate_order_details=_details,
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


@order_group.command(name=cli_util.override('orders.get_order.command_name', 'get'), help=u"""Returns the Order Details given by the order id in the JWT \n[Command Reference](getOrder)""")
@cli_util.option('--activation-token', required=True, help=u"""Activation Token containing an order id. JWT RFC 7519 formatted string.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'Order'})
@cli_util.wrap_exceptions
def get_order(ctx, from_json, activation_token):

    if isinstance(activation_token, six.string_types) and len(activation_token.strip()) == 0:
        raise click.UsageError('Parameter --activation-token cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'orders', ctx)
    result = client.get_order(
        activation_token=activation_token,
        **kwargs
    )
    cli_util.render_response(result, ctx)
