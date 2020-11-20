# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
# @Project : ProjectStruct-3-simple

from flask import Blueprint, render_template
from web.models import StatBrowse
from web.utils.decorator import statPageView
from web.common.modelSql import statBrowses

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@statPageView
def index():
    from web.indexData import TARGET_JOB, DEMANDS, PROJECT_HISTORY

    fourthChart = DEMANDS  # 工作要求，分年限
    targetJob = TARGET_JOB  # 目标工作
    pageViews = statBrowses()
    projectHistory = reversed(PROJECT_HISTORY)  # 项目更新日志
    return render_template('index.html', **locals())


@index_bp.route('/link')
def link():
    """用户点赞"""


@index_bp.route('/share')
def share():
    """分享网站链接"""
