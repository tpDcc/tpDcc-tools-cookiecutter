#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDcc-tools-{{cookiecutter.tool_name}}
"""

from __future__ import print_function, division, absolute_import

import os
import logging.config


def create_logger(dev=False):
    """
    Creates logger for current tpDcc-tools-{{cookiecutter.tool_name}} package
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs', 'tools'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger('tpDcc-tools-{{cookiecutter.tool_name}}')
    dev = os.getenv('TPDCC_DEV', dev)
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


create_logger()
