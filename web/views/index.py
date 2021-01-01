# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template

from web.utils.modelSql import isLike
from web.utils.modelSql import statSum
from web.utils.decorator import statPageView
from web.utils.modelSql import statInfoAction
from web.utils.decorator import cache_by_redis
from web.extension import redis_manager

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@cache_by_redis
@statPageView
def index():
    from web.indexData import TARGET_JOB, DEMANDS, PROJECT_HISTORY, \
        TAGS, EXTRAS, WEB_DATA, JOBS_INFO

    fourthChart = DEMANDS  # 工作要求，分年限
    jobInfo = JOBS_INFO  # 第一行
    webData = WEB_DATA  # 第二行
    tags = TAGS  # 第三行
    extras = EXTRAS  # 第三行
    likeSum = statSum(action='like')
    likeStatus = isLike(request.remote_addr)
    targetJob = TARGET_JOB  # 目标工作
    pageViews = redis_manager.bar_table_data()
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
