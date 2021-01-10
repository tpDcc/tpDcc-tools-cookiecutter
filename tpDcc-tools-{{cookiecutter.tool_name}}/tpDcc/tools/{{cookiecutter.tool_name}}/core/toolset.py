#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tpDc-tools-{{cookiecutter.tool_name}} toolset implementation
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.widgets import toolset

from tpDcc.tools.{{cookiecutter.tool_name}} import model, view, controller


class {{cookiecutter.tool_class}}Toolset(toolset.ToolsetWidget):
    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Toolset, self).__init__(*args, **kwargs)

    def contents(self):
        _model = model.NodePipeModel()
        _controller = controller.NodePipeController(client=self.client, model=_model)
        _view = view.NodePipeView(model=_model, controller=_controller, parent=self)

        return [_view]
