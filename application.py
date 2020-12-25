# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : app.py
# @Project : ProjectStruct-3-simple
import os
from flask import Flask
from config import config
from web.cli import register_cli
from web.views import register_bp
from web.log import register_logging
from web.extension import register_ext
from web.errors import register_errors
from web.template_ext import register_template_ext

base_dir = os.path.abspath(os.path.dirname(__file__))
static_file = os.path.join(base_dir, 'static')

config_name = os.getenv("FLASK_CONFIG", 'development')
app = Flask(__name__, static_folder=static_file, root_path=base_dir)
app.config.from_object(config[config_name])
HOST = app.config.get('HOST')
PORT = app.config.get('PORT')

register_logging(app)
register_ext(app)
register_bp(app)
register_cli(app)
register_errors(app)
register_template_ext(app)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
