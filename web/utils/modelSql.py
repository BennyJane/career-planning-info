# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:51
# Warning    ：The Hard Way Is Easier
import random
import datetime
from sqlalchemy import func
from sqlalchemy import and_
from flask import current_app

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
    # todo 使用group by根据时间字段的年月日来分组
    all_browses = StatBrowse.query.order_by(StatBrowse.create_at.desc()).all()
    for item in all_browses:
        date = getFormatDate(item.create_at, _format="%Y-%m-%d")
        if date not in browses:
            if len(browses.keys()) >= 10:  # 只需要找出最近10天的数据
                break
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
    browses_ratio.sort(key=lambda x: x['date'])
    return dict(total=total, browses=browses_ratio)


def insert_ip(app, ip, funcName):
    with app.app_context():
        brose = StatBrowse(id=produceId(), ip=ip, origin=funcName)
        db.session.add(brose)
        db.session.commit()


def statInfoAction(ip, action='like'):
    """点赞与下载量统计，逻辑基本一致，需要考虑并发情况,使用with_for_update"""
    try:
        isExist = StatInfo.query.filter(StatInfo.ip == ip).filter(StatInfo.action == action).with_for_update().first()
        if not isExist:
            info = StatInfo(id=produceId(), ip=ip, action=action, count=1)
            db.session.add(info)
        else:
            if action == 'like':
                isExist.count = 0 if isExist.count == 1 else 1  # 不需要add
            elif action == 'download':
                isExist.count += 1  # 不需要add
            db.session.add(isExist)
        db.session.commit()
    except Exception as e:
        db.session.rollback()


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


def addMsg(body, user=None):
    db.session.execute()
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
