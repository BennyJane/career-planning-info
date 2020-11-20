import datetime
from sqlalchemy import func
from web.models import StatBrowse
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
    return dict(total=total, browses=browses)
