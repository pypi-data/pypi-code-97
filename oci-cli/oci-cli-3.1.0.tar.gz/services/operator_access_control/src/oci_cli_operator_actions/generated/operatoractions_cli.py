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
from services.operator_access_control.src.oci_cli_operator_access_control.generated import opctl_service_cli


@click.command(cli_util.override('operator_actions.operator_actions_root_group.command_name', 'operator-actions'), cls=CommandGroupWithAlias, help=cli_util.override('operator_actions.operator_actions_root_group.help', """Operator Access Control enables you to control the time duration and the actions an Oracle operator can perform on your Exadata Cloud@Customer infrastructure.
Using logging service, you can view a near real-time audit report of all actions performed by an Oracle operator.

Use the table of contents and search tool to explore the OperatorAccessControl API."""), short_help=cli_util.override('operator_actions.operator_actions_root_group.short_help', """OperatorAccessControl API"""))
@cli_util.help_option_group
def operator_actions_root_group():
    pass


@click.command(cli_util.override('operator_actions.operator_action_group.command_name', 'operator-action'), cls=CommandGroupWithAlias, help="""Details of the operator action. Operator actions are a pre-defined set of commands available to the operator on different layers of the infrastructure. Although the groupings may differ depending on the infrastructure layers, the groups are designed to enable the operator access to commands to resolve a specific set of issues. The infrastructure layers controlled by the Operator Control include Dom0, CellServer, and Control Plane Server (CPS).

There are five groups available to the operator. x-obmcs-top-level-enum: '#/definitions/OperatorActionCategories' enum: *OPERATORACTIONCATEGORIES

The following infrastructure layers are controlled by the operator actions x-obmcs-top-level-enum: '#/definitions/InfrastructureLayers' enum: *INFRASTRUCTURELAYERS""")
@cli_util.help_option_group
def operator_action_group():
    pass


opctl_service_cli.opctl_service_group.add_command(operator_actions_root_group)
operator_actions_root_group.add_command(operator_action_group)


@operator_action_group.command(name=cli_util.override('operator_actions.get_operator_action.command_name', 'get'), help=u"""Gets the operator action associated with the specified operator action ID. \n[Command Reference](getOperatorAction)""")
@cli_util.option('--operator-action-id', required=True, help=u"""Unique Oracle supplied identifier associated with the operator action.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'OperatorAction'})
@cli_util.wrap_exceptions
def get_operator_action(ctx, from_json, operator_action_id):

    if isinstance(operator_action_id, six.string_types) and len(operator_action_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-action-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_actions', ctx)
    result = client.get_operator_action(
        operator_action_id=operator_action_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operator_action_group.command(name=cli_util.override('operator_actions.list_operator_actions.command_name', 'list'), help=u"""Lists all the OperatorActions available in the system. \n[Command Reference](listOperatorActions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""A filter to return only resources whose lifecycleState matches the given OperatorAction lifecycleState.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'OperatorActionCollection'})
@cli_util.wrap_exceptions
def list_operator_actions(ctx, from_json, all_pages, page_size, compartment_id, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
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
    client = cli_util.build_client('operator_access_control', 'operator_actions', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operator_actions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operator_actions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_operator_actions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
