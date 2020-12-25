# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier
from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import current_app
from flask import render_template

from web.models import Message
from web.utils.common import iPagination
from web.utils.modelSql import addMsg
from web.utils.modelSql import getUser
from web.utils.modelSql import addUser
from web.forms.message import MessageForm
from web.utils.wx_notify import wx_notify

message_bp = Blueprint('messages', __name__, url_prefix='/msg')


@message_bp.route('/', methods=["GET", "POST"])
def index():
    form = MessageForm()
    if request.method == "POST":
        # TODO 添加功能：限制同IP的10分钟内的留言次数上限为20条, 通过本地缓存函数实现
        email = request.form.get("email")
        msg_body = request.form.get("msg_body")
        user = None
        if email:
            user = getUser(email)
        if not user:
            user = addUser()
        addMsg(msg_body, user=user)

        try:
            # 通过企业微信机器人发送消息通知
            params = {"msg": msg_body, "name": user.username, "email": user.email}
            wx_notify.new_message(params)
        except Exception as e:
            current_app.logger.debug(str(e))

        return redirect(url_for(".index"))
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['PER_PAGE']  # 考虑字符串问题
    half_page_display = int(current_app.config["HALF_PAGE_DISPLAY"])
    query = Message.query.order_by(Message.create_at.desc())
    page_params = {
        'total': query.count(),
        'page_size': per_page,
        'half_page_display': half_page_display,
        'page': page,
        'url': request.full_path.replace('&page={}'.format(page), "")  # 清空页码
    }
    page_params = iPagination(page_params)
    # 筛选当前页面的数据
    offset = (page - 1) * per_page
    msgs = query.offset(offset).limit(per_page).all()
    msgs = [msg.msg_params for msg in msgs]
    return render_template('messages/content.html', msgs=msgs, form=form, page_params=page_params)
