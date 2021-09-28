import logging
from inspect import stack
from pathlib import Path

import click
from click import BadParameter
from pandas import DataFrame, ExcelWriter, read_excel

from com.enovation.toolbox.predictability.bean import PredictabilityBean
from com.enovation.toolbox.predictability.dp_date_predictability.dp_persister import DatePredictabilityPersister

_logger: logging.Logger = logging.getLogger(__name__)


@click.command('dp_persist')
@click.pass_context
@click.argument('alias', type=str)
@click.argument('file', type=click.Path(exists=False))
def dp_write_bean_date_predictability(ctx_context, alias, file):
    _logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is called")

    if alias not in ctx_context.obj:
        raise BadParameter(
            message=f"Cannot persist '{alias}', as this alias could not be found in context.",
            param_hint=f"Ensure you effectively computed a date predictability bean, and labelled it with the alias "
                       f"'{alias}'.",
            ctx=ctx_context
        )

    if not isinstance(ctx_context.obj[alias], PredictabilityBean):
        raise BadParameter(
            message=f"Cannot persist '{alias}', as this alias is of type '{type(ctx_context.obj[alias])}' while "
                    f"'PredictabilityBean' is expected.",
            param_hint=f"Ensure you effectively provide an instance of 'PredictabilityBean' to persist.",
            ctx=ctx_context
        )

    obj_the_data: PredictabilityBean = ctx_context.obj[alias]

    DatePredictabilityPersister().persist(
        obj_bean_to_persist=obj_the_data,
        p_file_path=Path(file),
    )

    _logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is returning")


@click.command('dp_load')
@click.pass_context
@click.argument('file', type=click.Path(exists=True))
@click.argument('alias', type=str, default='csv')
def dp_load_bean_date_predictability(ctx_context, file, alias):
    _logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is called")

    if alias in ctx_context.obj:
        _logger.warning(
            f"Warning: another object with alias '{alias}' already exists, of type {type(alias)}. This data "
            f"will be overridden with an instance of 'PredictabilityBean' from file '{file}'."
        )

    obj_the_bean: PredictabilityBean = DatePredictabilityPersister().load(
            p_file_path=Path(file),
    )

    # We update the context data store
    ctx_context.obj[alias] = obj_the_bean
    ctx_context.obj["_" + alias] = {
        "path": file,
        "src": "load_predictability_bean"
    }

    _logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is returning")
