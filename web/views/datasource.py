# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
import os

import pandas as pd
from flask import Blueprint, render_template, request, current_app

from web.crawl.utils import joinDemand

data_bp = Blueprint('data', __name__)


@data_bp.route('/')
def index():
    print(request.blueprint)
    config = current_app.config
    table_rows = config.get('TABLE_ROWS', 10)
    app_root_path = current_app.root_path
    # todo 处理系统平台的兼容
    csv_path = os.path.join(app_root_path, 'web\\crawl\\job_20201108.csv')
    df = pd.read_csv(csv_path)
    df.columns = [col.strip() for col in df.columns]
    df = df.iloc[:table_rows, :]
    df['jobDemand'] = df.apply(func=lambda x: joinDemand(x['jobDemand']), axis=1)
    table_data = df.to_dict(orient='records')
    show_columns = ['name', 'salary', 'site', 'company', 'jobDemand', 'url']
    return render_template('datasource/content.html', table_data=table_data, show_columns=show_columns)


@data_bp.route('/download/origin')
def download():
    """提供数据下载接口, 用来下载csv文件"""
    # TODO 添加异步任务,提供下载进度条 ==> celery
    # TODO 添加次数记录, 下载IP记录
    NotImplementedError()


@data_bp.route('/download/template')
def downloadTemp():
    """下载上传数据的ＣＳＶ模板"""


@data_bp.route('/download/report')
def JobReport():
    """提供数据分析报告"""


@data_bp.route('/upload')
def upload():
    """允许用户上传招聘信息csv文件"""
