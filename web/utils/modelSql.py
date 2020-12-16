# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier
import random
import datetime
from sqlalchemy import func
from sqlalchemy import and_

from web.extension import db
from web.models import User
from web.models import Message
from web.models import StatInfo
from web.models import StatBrowse
from web.constant import USER_NAME
from web.utils.libs import produceId
from web.utils.libs import getFormatDate

"""
from sqlalchemy import func
sqlite3: 中使用func.day() 报错,func没有该方法
"""


def statBrowses():
    total = StatBrowse.query.count()
    browses = {}
    now = datetime.datetime.utcnow()
    day_before_10days = now + datetime.timedelta(days=-10)
    all_browses = StatBrowse.query.filter(StatBrowse.create_at > day_before_10days) \
        .order_by(StatBrowse.create_at).all()
    for item in all_browses:
        date = getFormatDate(item.create_at, _format="%Y-%m-%d")
        if date not in browses:
            browses[date] = 1
        else:
            browses[date] = browses[date] + 1
    max_pv = max(browses.values()) * 1.2
    browses_ratio = []
    for key, value in browses.items():
        browses_ratio.append({
            "date": key,
            "ratio": round(int(value) / max_pv * 100, 1),
            "count": value,
        })
    return dict(total=total, browses=browses_ratio)


def statInfoAction(ip, action='like'):
    # 两种行为的初始化操作一致
    isExist = StatInfo.query.filter(StatInfo.ip == ip).filter(StatInfo.action == action).first()
    if not isExist:
        print("add download ....")
        info = StatInfo(id=produceId(), ip=ip, action=action, count=1)
        db.session.add(info)
        db.session.commit()
    else:
        print("add like ....")
        if action == 'like':
            isExist.count = 0 if isExist.count == 1 else 1  # 不需要add
        elif action == 'download':
            isExist.count += 1  # 不需要add
        db.session.add(isExist)
        db.session.commit()


def statSum(action='download'):
    """统计点赞或者下载量"""
    if action == 'like':
        return StatInfo.query.filter(and_(StatInfo.action == action, StatInfo.count == 1)).count()
    downloads = db.session.query(func.sum(StatInfo.count)).filter(StatInfo.action == action).first()[0]
    return downloads if downloads is not None else 0


def isLike(ip):
    """判断当前IP是否已经点赞"""
    isExist = StatInfo.query.filter(and_(StatInfo.ip == ip, StatInfo.action == 'like', StatInfo.count == 1)).first()
    return 'true' if isExist is not None else 'false'


"""
========================================================================================================================
留言界面得sql
========================================================================================================================
"""


def msgList():
    res = []
    msgs = Message.query.all()
    for msg in msgs:
        res.append(msg.msg_params)
    return res


def addMsg(body, user=None):
    msg = Message(body=body)
    msg.user = user
    db.session.add(msg)
    db.session.commit()


def addUser(email=""):
    random_name = random.choice(USER_NAME)
    user = User(username=random_name, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def getUser(email):
    user = User.query.filter(User.email == email).first()
    return user