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
from web.utils.modelSql import addUser
from web.forms.message import MessageForm

message_bp = Blueprint('messages', __name__, url_prefix='/msg')


@message_bp.route('/', methods=["GET", "POST"])
def index():
    form = MessageForm()
    if request.method == "POST":
        email = request.form.get("email")
        msg_body = request.form.get("msg_body")
        if email:
            user = getUser(email)
        else:
            user = addUser()
        addMsg(msg_body, user=user)
        return redirect(url_for(".index"))
    msgs = msgList()
    return render_template('messages/content.html', msgs=msgs, form=form)


@message_bp.route('/add', methods=['POST'])
def add_msg():
    """添加留言"""
    return redirect(url_for(".index"))
