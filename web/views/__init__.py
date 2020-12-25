# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier
from .datasource import data_bp
from .index import index_bp
from .messages import message_bp
from .extra import extra_bp
from ..utils.index import dateInfo


def register_bp(app):
    app.register_blueprint(index_bp, url_prefix="")
    app.register_blueprint(data_bp, url_prefix="/data")
    app.register_blueprint(message_bp, url_prefix="/msg")
    app.register_blueprint(extra_bp, url_prefix="/extra")

    @app.context_processor
    def add_template_context():
        dateDict = dateInfo()
        return dict(**locals())
