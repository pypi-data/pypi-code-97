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


@cli.command(cli_util.override('blockchain.blockchain_root_group.command_name', 'blockchain'), cls=CommandGroupWithAlias, help=cli_util.override('blockchain.blockchain_root_group.help', """Blockchain Platform Control Plane API"""), short_help=cli_util.override('blockchain.blockchain_root_group.short_help', """Blockchain Platform Control Plane API"""))
@cli_util.help_option_group
def blockchain_root_group():
    pass


@click.command(cli_util.override('blockchain.blockchain_platform_group.command_name', 'blockchain-platform'), cls=CommandGroupWithAlias, help="""Blockchain Platform Instance Description.""")
@cli_util.help_option_group
def blockchain_platform_group():
    pass


@click.command(cli_util.override('blockchain.peer_group.command_name', 'peer'), cls=CommandGroupWithAlias, help="""A Peer details""")
@cli_util.help_option_group
def peer_group():
    pass


@click.command(cli_util.override('blockchain.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('blockchain.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('blockchain.osn_group.command_name', 'osn'), cls=CommandGroupWithAlias, help="""An Ordering Service Node details""")
@cli_util.help_option_group
def osn_group():
    pass


@click.command(cli_util.override('blockchain.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


blockchain_root_group.add_command(blockchain_platform_group)
blockchain_root_group.add_command(peer_group)
blockchain_root_group.add_command(work_request_error_group)
blockchain_root_group.add_command(work_request_log_entry_group)
blockchain_root_group.add_command(osn_group)
blockchain_root_group.add_command(work_request_group)


@blockchain_platform_group.command(name=cli_util.override('blockchain.change_blockchain_platform_compartment.command_name', 'change-compartment'), help=u"""Change Blockchain Platform Compartment \n[Command Reference](changeBlockchainPlatformCompartment)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the new compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_blockchain_platform_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, compartment_id, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.change_blockchain_platform_compartment(
        blockchain_platform_id=blockchain_platform_id,
        change_blockchain_platform_compartment_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.create_blockchain_platform.command_name', 'create'), help=u"""Creates a new Blockchain Platform. \n[Command Reference](createBlockchainPlatform)""")
@cli_util.option('--display-name', required=True, help=u"""Platform Instance Display name, can be renamed""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--platform-role', required=True, help=u"""Role of platform - founder or participant""")
@cli_util.option('--compute-shape', required=True, help=u"""Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE""")
@cli_util.option('--idcs-access-token', required=True, help=u"""IDCS access token with Identity Domain Administrator role""")
@cli_util.option('--description', help=u"""Platform Instance Description""")
@cli_util.option('--is-byol', type=click.BOOL, help=u"""Bring your own license""")
@cli_util.option('--federated-user-id', help=u"""Identifier for a federated user""")
@cli_util.option('--ca-cert-archive-text', help=u"""Base64 encoded text in ASCII character set of a Thirdparty CA Certificates archive file. The Archive file is a zip file containing third part CA Certificates, the ca key and certificate files used when issuing enrollment certificates (ECerts) and transaction certificates (TCerts). The chainfile (if it exists) contains the certificate chain which should be trusted for this CA, where the 1st in the chain is always the root CA certificate. File list in zip file [ca-cert.pem,ca-key.pem,ca-chain.pem(optional)].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'blockchain', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'blockchain', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'blockchain', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'blockchain', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_blockchain_platform(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, platform_role, compute_shape, idcs_access_token, description, is_byol, federated_user_id, ca_cert_archive_text, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['platformRole'] = platform_role
    _details['computeShape'] = compute_shape
    _details['idcsAccessToken'] = idcs_access_token

    if description is not None:
        _details['description'] = description

    if is_byol is not None:
        _details['isByol'] = is_byol

    if federated_user_id is not None:
        _details['federatedUserId'] = federated_user_id

    if ca_cert_archive_text is not None:
        _details['caCertArchiveText'] = ca_cert_archive_text

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.create_blockchain_platform(
        create_blockchain_platform_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.create_osn.command_name', 'create-osn'), help=u"""Create Blockchain Platform Osn \n[Command Reference](createOsn)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--ad', required=True, help=u"""Availability Domain to place new OSN""")
@cli_util.option('--ocpu-allocation-param', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.wrap_exceptions
def create_osn(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, ad, ocpu_allocation_param, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ad'] = ad

    if ocpu_allocation_param is not None:
        _details['ocpuAllocationParam'] = cli_util.parse_json_parameter("ocpu_allocation_param", ocpu_allocation_param)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.create_osn(
        blockchain_platform_id=blockchain_platform_id,
        create_osn_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.create_peer.command_name', 'create-peer'), help=u"""Create Blockchain Platform Peer \n[Command Reference](createPeer)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--role', required=True, help=u"""Peer role""")
@cli_util.option('--ocpu-allocation-param', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ad', required=True, help=u"""Availability Domain to place new peer""")
@cli_util.option('--alias', help=u"""peer alias""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.wrap_exceptions
def create_peer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, role, ocpu_allocation_param, ad, alias):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['role'] = role
    _details['ocpuAllocationParam'] = cli_util.parse_json_parameter("ocpu_allocation_param", ocpu_allocation_param)
    _details['ad'] = ad

    if alias is not None:
        _details['alias'] = alias

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.create_peer(
        blockchain_platform_id=blockchain_platform_id,
        create_peer_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.delete_blockchain_platform.command_name', 'delete'), help=u"""Delete a particular of a Blockchain Platform \n[Command Reference](deleteBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_blockchain_platform(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.delete_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.delete_osn.command_name', 'delete-osn'), help=u"""Delete a particular OSN of a Blockchain Platform \n[Command Reference](deleteOsn)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--osn-id', required=True, help=u"""OSN identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_osn(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, osn_id, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    if isinstance(osn_id, six.string_types) and len(osn_id.strip()) == 0:
        raise click.UsageError('Parameter --osn-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.delete_osn(
        blockchain_platform_id=blockchain_platform_id,
        osn_id=osn_id,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.delete_peer.command_name', 'delete-peer'), help=u"""Delete a particular peer of a Blockchain Platform \n[Command Reference](deletePeer)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--peer-id', required=True, help=u"""Peer identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_peer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, peer_id, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    if isinstance(peer_id, six.string_types) and len(peer_id.strip()) == 0:
        raise click.UsageError('Parameter --peer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.delete_peer(
        blockchain_platform_id=blockchain_platform_id,
        peer_id=peer_id,
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


@work_request_group.command(name=cli_util.override('blockchain.delete_work_request.command_name', 'delete'), help=u"""Attempts to cancel the work request with the given ID. \n[Command Reference](deleteWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_work_request(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.delete_work_request(
        work_request_id=work_request_id,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.get_blockchain_platform.command_name', 'get'), help=u"""Gets information about a Blockchain Platform identified by the specific id \n[Command Reference](getBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'BlockchainPlatform'})
@cli_util.wrap_exceptions
def get_blockchain_platform(ctx, from_json, blockchain_platform_id):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.get_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@osn_group.command(name=cli_util.override('blockchain.get_osn.command_name', 'get'), help=u"""Gets information about an OSN identified by the specific id \n[Command Reference](getOsn)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--osn-id', required=True, help=u"""OSN identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'Osn'})
@cli_util.wrap_exceptions
def get_osn(ctx, from_json, blockchain_platform_id, osn_id):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    if isinstance(osn_id, six.string_types) and len(osn_id.strip()) == 0:
        raise click.UsageError('Parameter --osn-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.get_osn(
        blockchain_platform_id=blockchain_platform_id,
        osn_id=osn_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@peer_group.command(name=cli_util.override('blockchain.get_peer.command_name', 'get'), help=u"""Gets information about a peer identified by the specific id \n[Command Reference](getPeer)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--peer-id', required=True, help=u"""Peer identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'Peer'})
@cli_util.wrap_exceptions
def get_peer(ctx, from_json, blockchain_platform_id, peer_id):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    if isinstance(peer_id, six.string_types) and len(peer_id.strip()) == 0:
        raise click.UsageError('Parameter --peer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.get_peer(
        blockchain_platform_id=blockchain_platform_id,
        peer_id=peer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('blockchain.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@blockchain_platform_group.command(name=cli_util.override('blockchain.list_blockchain_platforms.command_name', 'list'), help=u"""Returns a list Blockchain Platform Instances in a compartment \n[Command Reference](listBlockchainPlatforms)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "SCALING", "INACTIVE", "FAILED"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'BlockchainPlatformCollection'})
@cli_util.wrap_exceptions
def list_blockchain_platforms(ctx, from_json, all_pages, page_size, compartment_id, display_name, page, limit, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_blockchain_platforms,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_blockchain_platforms,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_blockchain_platforms(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@osn_group.command(name=cli_util.override('blockchain.list_osns.command_name', 'list'), help=u"""List Blockchain Platform OSNs \n[Command Reference](listOsns)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'OsnCollection'})
@cli_util.wrap_exceptions
def list_osns(ctx, from_json, all_pages, page_size, blockchain_platform_id, display_name, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_osns,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_osns,
            limit,
            page_size,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    else:
        result = client.list_osns(
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@peer_group.command(name=cli_util.override('blockchain.list_peers.command_name', 'list'), help=u"""List Blockchain Platform Peers \n[Command Reference](listPeers)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'PeerCollection'})
@cli_util.wrap_exceptions
def list_peers(ctx, from_json, all_pages, page_size, blockchain_platform_id, display_name, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_peers,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_peers,
            limit,
            page_size,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    else:
        result = client.list_peers(
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('blockchain.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('blockchain.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
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


@work_request_group.command(name=cli_util.override('blockchain.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeStarted", "workRequestId"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMESTARTED is descending. Default order for WORKREQUESTID is ascending. If no value is specified TIMESTARTED is default.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'blockchain', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, blockchain_platform_id, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            blockchain_platform_id=blockchain_platform_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@blockchain_platform_group.command(name=cli_util.override('blockchain.preview_scale_blockchain_platform.command_name', 'preview-scale'), help=u"""Preview Scale Blockchain Platform \n[Command Reference](previewScaleBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--add-osns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""new OSNs to add

This option is a JSON list with items of type CreateOsnDetails.  For documentation on CreateOsnDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/blockchainplatform/20191010/datatypes/CreateOsnDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--add-replicas', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--add-peers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""new Peers to add

This option is a JSON list with items of type CreatePeerDetails.  For documentation on CreatePeerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/blockchainplatform/20191010/datatypes/CreatePeerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--add-storage', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--modify-peers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""modify ocpu allocation to existing Peers

This option is a JSON list with items of type ModifyPeerDetails.  For documentation on ModifyPeerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/blockchainplatform/20191010/datatypes/ModifyPeerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--remove-replicas', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--remove-osns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""OSN id list to remove""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--remove-peers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Peer id list to remove""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'add-osns': {'module': 'blockchain', 'class': 'list[CreateOsnDetails]'}, 'add-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'add-peers': {'module': 'blockchain', 'class': 'list[CreatePeerDetails]'}, 'add-storage': {'module': 'blockchain', 'class': 'ScaleStorageDetails'}, 'modify-peers': {'module': 'blockchain', 'class': 'list[ModifyPeerDetails]'}, 'remove-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'remove-osns': {'module': 'blockchain', 'class': 'list[string]'}, 'remove-peers': {'module': 'blockchain', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'add-osns': {'module': 'blockchain', 'class': 'list[CreateOsnDetails]'}, 'add-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'add-peers': {'module': 'blockchain', 'class': 'list[CreatePeerDetails]'}, 'add-storage': {'module': 'blockchain', 'class': 'ScaleStorageDetails'}, 'modify-peers': {'module': 'blockchain', 'class': 'list[ModifyPeerDetails]'}, 'remove-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'remove-osns': {'module': 'blockchain', 'class': 'list[string]'}, 'remove-peers': {'module': 'blockchain', 'class': 'list[string]'}}, output_type={'module': 'blockchain', 'class': 'ScaledBlockchainPlatformPreview'})
@cli_util.wrap_exceptions
def preview_scale_blockchain_platform(ctx, from_json, blockchain_platform_id, add_osns, add_replicas, add_peers, add_storage, modify_peers, remove_replicas, remove_osns, remove_peers):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if add_osns is not None:
        _details['addOsns'] = cli_util.parse_json_parameter("add_osns", add_osns)

    if add_replicas is not None:
        _details['addReplicas'] = cli_util.parse_json_parameter("add_replicas", add_replicas)

    if add_peers is not None:
        _details['addPeers'] = cli_util.parse_json_parameter("add_peers", add_peers)

    if add_storage is not None:
        _details['addStorage'] = cli_util.parse_json_parameter("add_storage", add_storage)

    if modify_peers is not None:
        _details['modifyPeers'] = cli_util.parse_json_parameter("modify_peers", modify_peers)

    if remove_replicas is not None:
        _details['removeReplicas'] = cli_util.parse_json_parameter("remove_replicas", remove_replicas)

    if remove_osns is not None:
        _details['removeOsns'] = cli_util.parse_json_parameter("remove_osns", remove_osns)

    if remove_peers is not None:
        _details['removePeers'] = cli_util.parse_json_parameter("remove_peers", remove_peers)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.preview_scale_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
        scale_blockchain_platform_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@blockchain_platform_group.command(name=cli_util.override('blockchain.scale_blockchain_platform.command_name', 'scale'), help=u"""Scale Blockchain Platform \n[Command Reference](scaleBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--add-osns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""new OSNs to add

This option is a JSON list with items of type CreateOsnDetails.  For documentation on CreateOsnDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/blockchainplatform/20191010/datatypes/CreateOsnDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--add-replicas', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--add-peers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""new Peers to add

This option is a JSON list with items of type CreatePeerDetails.  For documentation on CreatePeerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/blockchainplatform/20191010/datatypes/CreatePeerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--add-storage', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--modify-peers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""modify ocpu allocation to existing Peers

This option is a JSON list with items of type ModifyPeerDetails.  For documentation on ModifyPeerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/blockchainplatform/20191010/datatypes/ModifyPeerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--remove-replicas', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--remove-osns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""OSN id list to remove""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--remove-peers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Peer id list to remove""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'add-osns': {'module': 'blockchain', 'class': 'list[CreateOsnDetails]'}, 'add-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'add-peers': {'module': 'blockchain', 'class': 'list[CreatePeerDetails]'}, 'add-storage': {'module': 'blockchain', 'class': 'ScaleStorageDetails'}, 'modify-peers': {'module': 'blockchain', 'class': 'list[ModifyPeerDetails]'}, 'remove-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'remove-osns': {'module': 'blockchain', 'class': 'list[string]'}, 'remove-peers': {'module': 'blockchain', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'add-osns': {'module': 'blockchain', 'class': 'list[CreateOsnDetails]'}, 'add-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'add-peers': {'module': 'blockchain', 'class': 'list[CreatePeerDetails]'}, 'add-storage': {'module': 'blockchain', 'class': 'ScaleStorageDetails'}, 'modify-peers': {'module': 'blockchain', 'class': 'list[ModifyPeerDetails]'}, 'remove-replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'remove-osns': {'module': 'blockchain', 'class': 'list[string]'}, 'remove-peers': {'module': 'blockchain', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def scale_blockchain_platform(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, add_osns, add_replicas, add_peers, add_storage, modify_peers, remove_replicas, remove_osns, remove_peers, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if add_osns is not None:
        _details['addOsns'] = cli_util.parse_json_parameter("add_osns", add_osns)

    if add_replicas is not None:
        _details['addReplicas'] = cli_util.parse_json_parameter("add_replicas", add_replicas)

    if add_peers is not None:
        _details['addPeers'] = cli_util.parse_json_parameter("add_peers", add_peers)

    if add_storage is not None:
        _details['addStorage'] = cli_util.parse_json_parameter("add_storage", add_storage)

    if modify_peers is not None:
        _details['modifyPeers'] = cli_util.parse_json_parameter("modify_peers", modify_peers)

    if remove_replicas is not None:
        _details['removeReplicas'] = cli_util.parse_json_parameter("remove_replicas", remove_replicas)

    if remove_osns is not None:
        _details['removeOsns'] = cli_util.parse_json_parameter("remove_osns", remove_osns)

    if remove_peers is not None:
        _details['removePeers'] = cli_util.parse_json_parameter("remove_peers", remove_peers)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.scale_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
        scale_blockchain_platform_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.start_blockchain_platform.command_name', 'start'), help=u"""Start a Blockchain Platform \n[Command Reference](startBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_blockchain_platform(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.start_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.stop_blockchain_platform.command_name', 'stop'), help=u"""Stop a Blockchain Platform \n[Command Reference](stopBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_blockchain_platform(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.stop_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.update_blockchain_platform.command_name', 'update'), help=u"""Update a particular of a Blockchain Platform \n[Command Reference](updateBlockchainPlatform)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--description', help=u"""Platform Description""")
@cli_util.option('--storage-size-in-tbs', help=u"""Storage size in TBs""")
@cli_util.option('--replicas', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--total-ocpu-capacity', type=click.INT, help=u"""Number of total OCPUs to allocate""")
@cli_util.option('--load-balancer-shape', help=u"""Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'freeform-tags': {'module': 'blockchain', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'blockchain', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'replicas': {'module': 'blockchain', 'class': 'ReplicaDetails'}, 'freeform-tags': {'module': 'blockchain', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'blockchain', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_blockchain_platform(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, description, storage_size_in_tbs, replicas, total_ocpu_capacity, load_balancer_shape, freeform_tags, defined_tags, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')
    if not force:
        if replicas or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to replicas and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if storage_size_in_tbs is not None:
        _details['storageSizeInTBs'] = storage_size_in_tbs

    if replicas is not None:
        _details['replicas'] = cli_util.parse_json_parameter("replicas", replicas)

    if total_ocpu_capacity is not None:
        _details['totalOcpuCapacity'] = total_ocpu_capacity

    if load_balancer_shape is not None:
        _details['loadBalancerShape'] = load_balancer_shape

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.update_blockchain_platform(
        blockchain_platform_id=blockchain_platform_id,
        update_blockchain_platform_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.update_osn.command_name', 'update-osn'), help=u"""Update Blockchain Platform OSN \n[Command Reference](updateOsn)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--osn-id', required=True, help=u"""OSN identifier.""")
@cli_util.option('--ocpu-allocation-param', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.wrap_exceptions
def update_osn(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, osn_id, ocpu_allocation_param, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    if isinstance(osn_id, six.string_types) and len(osn_id.strip()) == 0:
        raise click.UsageError('Parameter --osn-id cannot be whitespace or empty string')
    if not force:
        if ocpu_allocation_param:
            if not click.confirm("WARNING: Updates to ocpu-allocation-param will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ocpuAllocationParam'] = cli_util.parse_json_parameter("ocpu_allocation_param", ocpu_allocation_param)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.update_osn(
        blockchain_platform_id=blockchain_platform_id,
        osn_id=osn_id,
        update_osn_details=_details,
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


@blockchain_platform_group.command(name=cli_util.override('blockchain.update_peer.command_name', 'update-peer'), help=u"""Update Blockchain Platform Peer \n[Command Reference](updatePeer)""")
@cli_util.option('--blockchain-platform-id', required=True, help=u"""Unique service identifier.""")
@cli_util.option('--peer-id', required=True, help=u"""Peer identifier.""")
@cli_util.option('--ocpu-allocation-param', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ocpu-allocation-param': {'module': 'blockchain', 'class': 'OcpuAllocationNumberParam'}})
@cli_util.wrap_exceptions
def update_peer(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, blockchain_platform_id, peer_id, ocpu_allocation_param, if_match):

    if isinstance(blockchain_platform_id, six.string_types) and len(blockchain_platform_id.strip()) == 0:
        raise click.UsageError('Parameter --blockchain-platform-id cannot be whitespace or empty string')

    if isinstance(peer_id, six.string_types) and len(peer_id.strip()) == 0:
        raise click.UsageError('Parameter --peer-id cannot be whitespace or empty string')
    if not force:
        if ocpu_allocation_param:
            if not click.confirm("WARNING: Updates to ocpu-allocation-param will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ocpuAllocationParam'] = cli_util.parse_json_parameter("ocpu_allocation_param", ocpu_allocation_param)

    client = cli_util.build_client('blockchain', 'blockchain_platform', ctx)
    result = client.update_peer(
        blockchain_platform_id=blockchain_platform_id,
        peer_id=peer_id,
        update_peer_details=_details,
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
