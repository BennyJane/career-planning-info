# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : app.py
import os
import sys
from _compat import win, modifyPath

# 考虑直接使用app的root_path 路径
baseDir = os.path.abspath(os.path.dirname(__file__))

if win:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    PROJECT_NAME = "career-plane"
    HOST = "0.0.0.0"
    PORT = 8010

    SECRET_KEY = os.getenv("SECRET_KEY", 'dey key')
    IS_DEBUG = True

    # 静态文件版本
    RELEASE_VERSION = "20201215:V1.0"

    SQLALCHEMY_DATABASE_URI = prefix + ":memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    BROWSE_GAP = 30  # 统计用户浏览量的时间间隔

    TABLE_ROWS = 15
    SHOW_FIELDS = ['name', 'salary', 'site', 'companyName', 'jobDemand']  # 表单显示的字段列表

    CSV_PATH = modifyPath('web/crawl/job_20201108.csv')
    WORD_PATH = modifyPath('web/crawl/job_20201108.csv')

    PER_PAGE = 20
    HALF_PAGE_DISPLAY = 8


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    print("mysql", SQLALCHEMY_DATABASE_URI)
    if not os.getenv("SQLALCHEMY_DATABASE_URI"):  # 没有添加mysql数据库连接时，创建sqlite数据库连接
        SQLALCHEMY_DATABASE_URI = prefix + os.path.join(baseDir, 'data-dev.db')

    BROWSE_GAP = 1


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    print("mysql", SQLALCHEMY_DATABASE_URI)
    if not os.getenv("SQLALCHEMY_DATABASE_URI"):  # 没有添加mysql数据库连接时，创建sqlite数据库连接
        SQLALCHEMY_DATABASE_URI = prefix + os.path.join(baseDir, 'data.db')

    pageView_blackIp = ['127.0.0.1']
    BROWSE_GAP = 1


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(baseDir, 'data-test.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
