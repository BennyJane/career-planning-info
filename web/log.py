# -*- coding: utf-8 -*-
# @Time : 2020/9/26
# @Author : Benny Jane
# @Email : 暂无
# @File : command.py
# @Project : Flask-Demo
import os
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler

from flask import request

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
project_name = os.path.split(os.path.dirname(__file__))[1]


def register_logging(app):
    class RequestFormatter(logging.Formatter):
        # 通过继承，修改打印信息： 报错的url 与 远程地址
        def format(self, record):
            record.url = request.url
            record.remote_addr = request.remote_addr
            return super(RequestFormatter, self).format(record)

    request_formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log_path = os.path.join(basedir, f'logs/{project_name}')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    file_handler = RotatingFileHandler("{}/career_plan.log".format(log_path),
                                       maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # 需要设置整个日志的等级，开发调试模式下，默认为debug； 没有设置会导致无法输出日志
    app.logger.setLevel(logging.INFO)
    if not app.debug:
        # 生产模式下，需要设置合适等级
        # app.logger.setLevel(logging.ERROR)
        app.logger.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
