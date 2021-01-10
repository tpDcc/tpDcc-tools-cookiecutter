#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{cookiecutter.tool_description}} toolset implementation
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.widgets import toolset


class {{cookiecutter.tool_class}}Toolset(toolset.ToolsetWidget):
    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Toolset, self).__init__(*args, **kwargs)

    def contents(self):
        return []
