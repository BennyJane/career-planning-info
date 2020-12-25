# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 19:59
# Warning    ：The Hard Way Is Easier

import datetime
from flask import request
from flask import current_app
from functools import wraps
from web.extension import db
from web.models import StatBrowse
from web.utils.libs import produceId
from web.extension import redis_manager


def statPageView(f):
    """统计页面访问次数: 使用消息队列"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 　TODO 向消息队列中添加访问数据; 修改该逻辑,减少服务器压力
        now = datetime.datetime.utcnow()
        minutes_before_30m = now + datetime.timedelta(minutes=-30)
        # 获取访问页面的视图函数名称,包含蓝图名称
        origin_view_func = request.endpoint
        ip = request.remote_addr
        # 间隔超过30分钟增加一个浏览量
        is_browsed = StatBrowse.query.filter_by(ip=ip) \
            .filter(StatBrowse.create_at >= minutes_before_30m).first()
        if not is_browsed:
            brose = StatBrowse(id=produceId(), ip=ip, origin=origin_view_func)
            db.session.add(brose)
            db.session.commit()
        return f(*args, **kwargs)

    return wrapper


def cache_by_redis(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        view_endpoint = request.endpoint
        key = f"html:{view_endpoint}"
        try:
            res = redis_manager.conn.get(key)
        except Exception as e:
            res = ""
            current_app.logger.debug(e)
        if not res:
            html = f(*args, **kwargs)
            redis_manager.conn.set(key, html, ex=60 * 60 * 24)
            return html
        # 计算缓存字符串长度
        # import sys
        # print(len(res) / 1024 / 1024)
        # print(sys.getsizeof(res))
        return res

    return wrapper
