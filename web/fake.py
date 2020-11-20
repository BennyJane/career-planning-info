# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
import random
from faker import Faker
from .models import StatBrowse
from .utils.com import produceId

fake = Faker()


def fake_ip():
    def num():
        return int(random.random() * 255)

    ip = f"{num()}.{num()}.{num()}.{num()}"
    return ip


fake.ip = fake_ip


def faker_browse(db):
    for _ in range(200):
        browse = StatBrowse(id=produceId(),
                            ip=fake.ip(),
                            origin='index.index',
                            create_at=fake.date_time_this_year()
                            )
        db.session.add(browse)
    db.session.commit()


def core(db):
    faker_browse(db)


if __name__ == '__main__':
    core()
