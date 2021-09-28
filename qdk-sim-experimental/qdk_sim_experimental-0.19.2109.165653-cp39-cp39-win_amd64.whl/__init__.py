#!/bin/env python
# -*- coding: utf-8 -*-
##
# __init__.py: Root for the qdk_sim_experimental package.
##
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
##

## IMPORTS ##

from typing import Dict, List, Union
from enum import Enum
import enum
import json

import qdk_sim_experimental._qdk_sim_rs as _native
try:
    import qdk_sim_experimental.version as _version
except ImportError:
    # This could happen if setup.py was not run.
    _version = None

## EXPORTS ##

__all__ = [
    "Tableau", "NoiseModel", "Instrument", "State", "Process",
    "Pauli"
]

# Re-export native classes.
from qdk_sim_experimental._qdk_sim_rs import (
    Tableau, NoiseModel, Instrument, State, Process
)

class Pauli(enum.Enum):
    I = 0
    X = 1
    Y = 3
    Z = 2

## BUILD METADATA ##

# Re-export the autogenerated version.
__version__ = getattr(_version, "__version__", "<unknown>")
_is_conda = getattr(_version, "_is_conda", False)

def build_info() -> Dict[str, Union[List[str], str]]:
    """
    Returns information about the environment in which this
    module was built.
    """
    return json.loads(_native.build_info_json())
