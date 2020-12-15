# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : ProjectStruct-3-simple


def register_cli(app, db):
    command1(app, db)


def command1(app, db):
    @app.cli.command()
    def forge():
        from web.fake import core
        core(db)
