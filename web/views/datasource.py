# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
# @Project : ProjectStruct-3-simple

from flask import Blueprint, render_template, request

data_bp = Blueprint('data', __name__)


@data_bp.route('/')
def index():
    print(request.blueprint)
    return render_template('datasource/content.html')


@data_bp.route('/download')
def download():
    """提供数据下载接口, 用来下载csv文件"""
    # TODO 添加异步任务,提供下载进度条 ==> celery
    # TODO 添加次数记录, 下载IP记录
    NotImplementedError()


@data_bp.route('/download/report')
def JobReport():
    """提供数据分析报告"""


@data_bp.route('/upload')
def upload():
    """允许用户上传招聘信息csv文件"""
