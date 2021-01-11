# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 19:59
# Warning    ：The Hard Way Is Easier
from flask import request
from flask import current_app
from functools import wraps
from threading import Thread

from web.utils.modelSql import insert_ip
from web.extension import redis_manager


def statPageView(f):
    """统计页面访问次数"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 　TODO 改为异步非阻塞执行
        # 获取访问页面的视图函数名称,包含蓝图名称
        origin_view_func = request.endpoint
        ip = request.remote_addr
        is_stated = redis_manager.browse_stat(ip=ip)
        if is_stated:
            return f(*args, **kwargs)
        # 增加一条记录; 异步执行
        app = current_app._get_current_object()
        Thread(target=insert_ip, args=(app, ip, origin_view_func)).start()
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
            redis_manager.conn.set(key, html, ex=60 * 60 * 12)
            return html
        # 计算缓存字符串长度
        # import sys
        # print(len(res) / 1024 / 1024)
        # print(sys.getsizeof(res))
        return res

    return wrapper
