"""Aga grades assignments: a library for easily producing autograders for code.

Anything not explicitly documented here should not be used directly by clients and is
only exposed for testing, the CLI, and type hinting.
"""

from .core import problem, test_case

__all__ = ("problem", "test_case")
