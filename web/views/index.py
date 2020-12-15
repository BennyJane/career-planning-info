# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
# @Project : ProjectStruct-3-simple
from flask import jsonify
from flask import Blueprint, render_template, request, url_for, redirect

from web.utils.decorator import statPageView
from web.utils.modelSql import statBrowses, statInfoAction, statSum, isLike

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@statPageView
def index():
    from web.indexData import TARGET_JOB, DEMANDS, PROJECT_HISTORY, TAGS, EXTRAS, WEB_DATA, JOBS_INFO

    fourthChart = DEMANDS  # 工作要求，分年限
    jobInfo = JOBS_INFO  # 第一行
    webData = WEB_DATA  # 第二行
    tags = TAGS  # 第三行
    extras = EXTRAS  # 第三行
    likeSum = statSum(action='like')
    likeStatus = isLike(request.remote_addr)
    targetJob = TARGET_JOB  # 目标工作
    pageViews = statBrowses()
    projectHistory = reversed(PROJECT_HISTORY)  # 项目更新日志
    return render_template('index.html', **locals())


@index_bp.route('/like/click/<string:action>')
def like(action):
    """用户点赞"""
    ip = request.remote_addr
    if action == 'click':  #
        statInfoAction(ip=ip, action='like')

    likeSum = statSum(action='like')
    likeStatus = isLike(request.remote_addr)
    data = dict(likeSum=likeSum, likeStatus=likeStatus)
    return jsonify(data)


@index_bp.route('/share')
def share():
    """分享网站链接"""
