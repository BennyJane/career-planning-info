# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/25 15:59
# Warning    ：The Hard Way Is Easier
from flask import Blueprint
from web.extension import redis_manager

extra_bp = Blueprint('extra', __name__)


@extra_bp.route('/cache/del/<string:page>')
def cache_del(page):
    """删除页面缓存"""
    key = f"html:{page}"
    redis_manager.conn.delete(key)
    print(redis_manager.conn.get(key), page)
    return f"{page}: 缓存已经删除"
