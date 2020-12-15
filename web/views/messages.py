# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier

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
