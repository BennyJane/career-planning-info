# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py
# @Project : ProjectStruct-3-simple
import datetime
import random

from dateutil import parser

timeWarnings = [
    "人生天地之间，若白驹过隙，忽然而已",
    "逝者如斯夫，不舍昼夜",
    "时间检验一切",
    "莫等闲，白了少年头，空悲切",
    "以前我做错了，现在我想做个好人",
    "老了才明白，Time flies",
]


def dateInfo():
    now = datetime.datetime.now()
    year = now.year
    end = datetime.datetime(year, 12, 31)
    start = datetime.datetime(year, 1, 1)

    # 就算剩余天数与整年的进度
    remaining = (end - now).days  # 剩余天数
    used = now.strftime('%j')  # 已使用天数
    total = (end - start).days  # 总共天数
    percent = round((total - remaining) / total * 100, 2)

    # 修改当天日期的格式
    now = now.strftime('%d %B')
    warning = random.choice(timeWarnings)

    # print(locals())
    return dict(**locals())


def lastUpdate(date: str):
    last_time = parser.parse(date)
    now = datetime.datetime.now()
    remaining = (now - last_time).days
    if remaining == 0:
        info = {
            "date": "刚刚更新",
            "info": "好巧！正好遇到你，我们这么有缘分，可以给项目点个赞吗？",
        }
    elif remaining <= 7:
        info = {
            "date": "7天内更新过",
            "info": "主人还没跑路，点赞鼓励一下呗"
        }
    else:
        info = {
            "date": "该项目{}天没有更新过了！".format(remaining),
            "info": "主人跑路了吗？点赞，催更了"
        }
    return info


if __name__ == '__main__':
    # dateInfo()
    lastUpdate('2020-11-19')
