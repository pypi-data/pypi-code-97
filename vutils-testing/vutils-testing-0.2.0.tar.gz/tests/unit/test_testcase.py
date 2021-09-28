#                                                         -*- coding: utf-8 -*-
# File:    ./tests/unit/test_testcase.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2021-09-11 08:30:17 +0200
# Project: vutils-testing: Auxiliary library for writing tests
#
# SPDX-License-Identifier: MIT
#
"""Test `vutils.testing.testcase` module."""

import unittest.mock

from vutils.testing.testcase import TestCase
from vutils.testing.utils import cover_typing

from .common import SYMBOLS

cover_typing("vutils.testing.testcase", SYMBOLS)


class TestCaseTestCase(TestCase):
    """Test case for `TestCase`."""

    __slots__ = ()

    def test_called_with(self):
        """Test `TestCase.assert_called_with` method."""
        mock = unittest.mock.Mock()

        mock.foo()
        self.assert_called_with(mock.foo)

        mock.foo(1, 2)
        self.assert_called_with(mock.foo, 1, 2)

        mock.foo(bar=3, baz=4)
        self.assert_called_with(mock.foo, bar=3, baz=4)

        mock.foo(5, quux=6)
        self.assert_called_with(mock.foo, 5, quux=6)
