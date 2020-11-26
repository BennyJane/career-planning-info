# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : index.py
# @Project : ProjectStruct-3-simple

from flask import Blueprint, render_template

message_bp = Blueprint('messages', __name__)


@message_bp.route('/')
def index():
    return render_template('messages/content.html')


@message_bp.route('/list')
def download():
    """添加招聘信息"""
    # TODO 开放招聘信息展示页面,允许外部人员添加招聘信息
    NotImplementedError()
