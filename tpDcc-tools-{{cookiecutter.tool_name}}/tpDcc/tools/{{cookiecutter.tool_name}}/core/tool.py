#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{cookiecutter.tool_description}} tool implementation
"""

from __future__ import print_function, division, absolute_import
import os
import sys

from tpDcc.core import tool

from tpDcc.tools.{{cookiecutter.tool_name}}.core import toolset


class {{cookiecutter.tool_class}}Tool(tool.DccTool, object):

    ID = 'tpDcc-tools-{{cookiecutter.tool_name}}'
    TOOLSET_CLASS = toolset.{{cookiecutter.tool_class}}Toolset

    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Tool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': '{{cookiecutter.tool_nice_name}}',
            'id': cls.ID,
            'supported_dccs': {{cookiecutter.supported_dccs}},
            'icon': '{{cookiecutter.tool_icon}}',
            'tooltip': '{{cookiecutter.tool_description}}',
            'tags': {{cookiecutter.tool_tags}},
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': '{{cookiecutter.tool_nice_name}}', 'load_on_startup': False, 'color': '', 'background_color': ''},
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


if __name__ == '__main__':
    import tpDcc.loader
    from tpDcc.managers import tools

    tool_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    if tool_path not in sys.path:
        sys.path.append(tool_path)

    tpDcc.loader.init(dev=False)

    tools.ToolsManager().launch_tool_by_id('tpDcc-tools-{{cookiecutter.tool_name}}')
