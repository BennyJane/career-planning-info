import time
import datetime
from flask import request
from functools import wraps
from web.models import StatBrowse
from extension import db
from .commom import produceId


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
        print(is_browsed, 'is browsed')
        if not is_browsed:
            brose = StatBrowse(id=produceId(), ip=ip, origin=origin_view_func)
            db.session.add(brose)
            db.session.commit()
        return f(*args, **kwargs)

    return wrapper
