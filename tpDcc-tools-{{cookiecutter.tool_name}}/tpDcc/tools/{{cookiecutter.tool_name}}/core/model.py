#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
tpDcc-tools-{{cookiecutter.tool_name}} widget model class implementation
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import QObject


class {{cookiecutter.tool_class}}Model(QObject, object):
    def __init__(self):
        super({{cookiecutter.tool_class}}Model, self).__init__()
