# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
import time
import random
from faker import Faker
from .models import StatBrowse
from .models import User
from .models import Message
from .utils.libs import produceId
from .constant import USER_NAME

fake = Faker()


def fake_ip():
    def num():
        return int(random.random() * 255)

    ip = f"{num()}.{num()}.{num()}.{num()}"
    return ip


fake.ip = fake_ip


def forge_browse():
    """添加浏览测试数据"""
    from web.extension import db
    for _ in range(200):
        time.sleep(0.1)
        browse = StatBrowse(id=produceId(),
                            ip=fake.ip(),
                            origin='index.index',
                            create_at=fake.date_time_this_year()
                            )
        db.session.add(browse)
    db.session.commit()


def forge_message():
    """添加留言测试数据"""
    from web.extension import db
    for _ in range(100):
        user = User(username=random.choice(USER_NAME), email=fake.email())
        msg = Message(body=fake.sentence())
        if len(msg.body) < 1:
            continue
        msg.user = user
        db.session.add_all([user, msg])
        db.session.commit()


if __name__ == '__main__':
    forge_browse()
