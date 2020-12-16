# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : ProjectStruct-3-simple
from .fake import forge_browse
from .fake import forge_message


def register_cli(app):
    cli_func = [forge_message, forge_browse]

    for f in cli_func:
        app.cli.command()(f)
