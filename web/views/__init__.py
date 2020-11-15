# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : ProjectStruct-3-simple
from .index import index_bp
from ..utils.indexPart import dateInfo


def register_bp(app):
    app.register_blueprint(index_bp, url_prefix="")

    @app.context_processor
    def add_template_context():
        dateDict = dateInfo()

        return dict(**locals())
