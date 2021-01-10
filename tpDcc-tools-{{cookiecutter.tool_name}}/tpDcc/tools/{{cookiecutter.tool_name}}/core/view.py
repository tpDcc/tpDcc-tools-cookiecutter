#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
tpDcc-tools-{{cookiecutter.tool_name}} widget view class implementation
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.core import base


class {{cookiecutter.tool_class}}View(base.BaseWidget, object):
    def __init__(self, model, controller, parent=None):

        self._model = model
        self._controller = controller

        super({{cookiecutter.tool_class}}View, self).__init__(parent=parent)

    # =================================================================================================================
    # PROPERTIES
    # =================================================================================================================

    @property
    def model(self):
        return self._model

    @property
    def controller(self):
        return self._controller
