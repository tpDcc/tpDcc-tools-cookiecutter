#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
tpDcc-tools-{{cookiecutter.tool_name}} widget controller class implementation
"""

from __future__ import print_function, division, absolute_import


class {{cookiecutter.tool_class}}Controller(object):
    def __init__(self, client, model):
        super({{cookiecutter.tool_class}}Controller, self).__init__()

        self._client = client
        self._model = model

    # =================================================================================================================
    # PROPERTIES
    # =================================================================================================================

    @property
    def client(self):
        return self._client

    @property
    def model(self):
        return self._model
