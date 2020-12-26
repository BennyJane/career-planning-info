# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/24 14:51
# Warning    ：The Hard Way Is Easier
import redis
import logging
import datetime
from flask import Flask
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class RedisManager(object):
    def __init__(self, app=None):
        self.conn = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """通过调用init_app()方法，绑定到app实例"""
        config = app.config
        pools = redis.ConnectionPool.from_url(config.get("REDIS_URI"))
        self.conn = redis.Redis(connection_pool=pools)


@contextmanager
def redis_lock(conn, action_name, timeout=20 * 60 * 60):
    try:
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")
        key = f"{action_name}:lock:{today_str}"
        # 只有不存在的键key，才能执行成功 ==》 如果有客户端已经设置该键，则其他客户端不可操作
        _lock = conn.set(key, value=1, nx=True, ex=timeout)
        yield _lock  # # 新增键会返回True; 键已存在，返回None
    except KeyError as e:  # 捕获未获取锁的异常
        logger.info(e)
        return
    except Exception as e:  # 捕获获取锁，但执行过程中报错的情况
        logger.debug(e)
    logger.info("释放锁 ...")
    conn.delete(key)  # 释放锁，只有获取锁的线程才需要释放锁
