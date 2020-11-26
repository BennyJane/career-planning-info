# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : ProjectStruct-3-simple
from .datasource import data_bp
from .index import index_bp
from .messages import message_bp
from ..utils.index import dateInfo


def register_bp(app):
    app.register_blueprint(index_bp, url_prefix="")
    app.register_blueprint(data_bp, url_prefix="/data")
    app.register_blueprint(message_bp, url_prefix="/msg")

    @app.context_processor
    def add_template_context():
        dateDict = dateInfo()
        return dict(**locals())
