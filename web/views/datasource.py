# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
import os

import pandas as pd
from flask import Blueprint, render_template, request, current_app, send_from_directory, flash

from web.crawl.utils import joinDemand
from web.utils.modelSql import statInfoAction, statSum

data_bp = Blueprint('data', __name__)


@data_bp.route('/')
def index():
    config = current_app.config
    table_rows = config.get('TABLE_ROWS', 10)
    csv_path = config['CSV_PATH']
    show_columns = config.get('SHOW_FIELDS', ['name', 'salary', 'site', 'companyName', 'jobDemand'])
    app_root_path = current_app.root_path

    target_file_path = os.path.join(app_root_path, csv_path)

    df = pd.read_csv(target_file_path)
    df.columns = [col.strip() for col in df.columns]
    df = df.iloc[:table_rows, :]
    df['jobDemand'] = df.apply(func=lambda x: joinDemand(x['jobDemand']), axis=1)
    table_data = df.to_dict(orient='records')

    downloads = statSum(action='download')
    return render_template('datasource/content.html', table_data=table_data,
                           downloads=downloads, show_columns=show_columns)


@data_bp.route('/download/origin/<string:file>')
def download(file):
    """提供数据下载接口, 用来下载csv文件"""
    # TODO 添加异步任务,提供下载进度条 ==> celery
    # TODO 添加次数记录, 下载IP记录
    app_root_path = current_app.root_path
    file_path = current_app.config[f'{file.upper()}_PATH']
    if file_path:
        target_file_path = os.path.join(app_root_path, file_path)  # 兼容win linux 平台
        filePath, filename = os.path.split(target_file_path)
        if os.path.isfile(target_file_path):
            # 统计下载量
            ip = request.remote_addr
            statInfoAction(ip, action='download')
            return send_from_directory(filePath, filename, as_attachment=True)
    flash("文件不存在~")


@data_bp.route('/download/template')
def downloadTemp():
    """下载上传数据的ＣＳＶ模板"""


@data_bp.route('/upload')
def upload():
    """允许用户上传招聘信息csv文件"""
