#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpRigToolkit-tools-{{cookiecutter.tool_name}}
"""

import pytest

from tpRigToolkit.tools.{{cookiecutter.tool_name}} import __version__


def test_version():
    assert __version__.get_version()
