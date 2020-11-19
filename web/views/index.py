# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
# @Project : ProjectStruct-3-simple

from flask import Blueprint, render_template, request
from ..indexData.fourthChart import fourth_chart
from ..utils.decorator import statPageView

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@statPageView
def index():
    return render_template('index.html', fourthChart=fourth_chart)


@index_bp.route('/link')
def link():
    """用户点赞"""


@index_bp.route('/share')
def share():
    """分享网站链接"""
