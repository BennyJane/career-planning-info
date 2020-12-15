# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier
import random
from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from web.utils.modelSql import msgList
from web.utils.modelSql import addMsg
from web.utils.modelSql import getUser

message_bp = Blueprint('messages', __name__, url_prefix='/msg')


@message_bp.route('/')
def index():
    msgs = msgList()
    return render_template('messages/content.html', msgs=msgs)


@message_bp.route('/add')
def add_msg():
    """添加留言"""
    email = request.form.get("email")
    msg_body = request.form.get("msg_body")
    user = None
    if email:
        user = getUser(email)

    msg_info = {
        "email": email if email else "",
        "email": msg_body,
    }
    addMsg(msg_info, user=user)
    return redirect(url_for(".index"))
