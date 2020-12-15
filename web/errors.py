# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 20:08
# Warning    ：The Hard Way Is Easier
from flask import render_template


def register_errors(app):
    app.errorhandler(400)(bad_request)
    app.errorhandler(404)(page_not_found)
    app.errorhandler(500)(internal_server_error)


def bad_request(e):
    return render_template('errors/400.html'), 400


def page_not_found(e):
    return render_template('errors/404.html'), 404


def internal_server_error(e):
    return render_template('errors/500.html'), 500
