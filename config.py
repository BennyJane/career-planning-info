# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : app.py
# @Project : ProjectStruct-3-simple

import os
import sys

# 考虑直接使用app的root_path 路径
baseDir = os.path.abspath(os.path.dirname(__file__))

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    PROJECT_NAME = 'blogDog'

    SECRET_KEY = os.getenv("SECRET_KEY", 'dey key')
    IS_DEBUG = True

    SQLALCHEMY_DATABASE_URI = prefix + ":memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    BROWSE_GAP = 30  # 统计用户浏览量的时间间隔

    TABLE_ROWS = 15
    SHOW_FIELDS = ['name', 'salary', 'site', 'companyName', 'jobDemand']  # 表单显示的字段列表


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(baseDir, 'data-dev.db')

    # 添加celery配置
    broker_url = 'redis://localhost:6379'
    result_backend = 'redis://localhost:6379'
    imports = ('tasks')

    BROWSE_GAP = 1


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(baseDir, 'data-test.db')


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(baseDir, 'data.db')

    pageView_blackIp = ['127.0.0.1']


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
