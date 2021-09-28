#!/usr/bin/env python
# coding=utf-8

import sys

from ....cli import click
from ....providers.bytom.htlc import HTLC
from ....providers.bytom.transaction import FundTransaction
from ....providers.bytom.utils import amount_unit_converter
from ....providers.config import bytom as config


@click.command("fund", options_metavar="[OPTIONS]",
               short_help="Select Bytom Fund transaction builder.")
@click.option("-a", "--address", type=str, required=True, help="Set Bytom sender address.")
@click.option("-ca", "--contract-address", type=str, required=True,
              help="Set Bytom Hash Time Lock Contract (HTLC) address.")
@click.option("-am", "--amount", type=float, required=True, help="Set Bytom fund amount.")
@click.option("-u", "--unit", type=str, default=config["unit"],
              help="Set Bytom amount unit.", show_default=True)
@click.option("-as", "--asset", type=str, default=config["asset"],
              help="Set Bytom asset id.", show_default=True)
@click.option("-n", "--network", type=str, default=config["network"],
              help="Set Bytom network.", show_default=True)
def fund(address: str, contract_address: str, amount: int, unit: str, asset: str, network: str):
    try:
        _htlc: HTLC = HTLC(
            network=network, contract_address=contract_address
        )
        _amount: int = (
            int(amount) if unit == "NEU" else amount_unit_converter(
                amount=amount, unit_from=f"{unit}2NEU"
            )
        )
        click.echo(
            FundTransaction(
                network=network
            ).build_transaction(
                address=address, htlc=_htlc, amount=_amount, asset=asset
            ).transaction_raw()
        )
    except Exception as exception:
        click.echo(click.style("Error: {}")
                   .format(str(exception)), err=True)
        sys.exit()
