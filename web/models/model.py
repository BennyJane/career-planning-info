# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:52
# Warning    ：The Hard Way Is Easier
from datetime import datetime
from web.extension import db
from web.models import Column
from web.models import BaseMixin


# 抓取的原始数据
class JobInfo(db.Model, BaseMixin):
    __tablename__ = 'job_info'
    id = Column(db.String(32), primary_key=True)
    name = Column(db.String(128), nullable=False)
    salary = Column(db.Integer, nullable=False, default=0)
    year = Column(db.String(32), nullable=False, default="")
    site = Column(db.String(32), nullable=False, default="")
    responsibility = Column(db.Text, nullable=False, default="")
    demand = Column(db.Text, nullable=False, default="")
    other = Column(db.Text, nullable=False, default="")
    source = Column(db.Text, nullable=False, default="")
    source_id = Column(db.String(32), nullable=False, default="")
    source_url = Column(db.Text, nullable=False, default="")


class WarningPara(db.Model, BaseMixin):
    __tablename__ = 'warning_para'
    id = Column(db.String(32), primary_key=True)
    para = Column(db.Text, default="")


class StatInfo(db.Model):
    __tablename__ = 'stat_info'
    id = Column(db.String(32), primary_key=True)
    ip = Column(db.String(120), default="")
    action = Column(db.String(32), default='', comment="访客行为: like-点赞, download-下载")
    count = Column(db.INTEGER, default=0, comment="统计单个IP下载次数")  # 允许无限下载
    create_at = Column(db.DateTime, default=datetime.now)
    update_at = Column(db.DateTime, default=datetime.now)

    __mapper_args__ = {'order_by': [create_at.desc()]}


class StatBrowse(db.Model):
    """使用mysql的锁机制; 统计网站浏览数据"""
    id = Column(db.String(32), primary_key=True)
    ip = Column(db.String(120), default="")
    # page_views = Column(db.BigInteger, default=0)
    origin = Column(db.String(120), default="", comment="网站视图函数名称")
    create_at = Column(db.DateTime, default=datetime.now)
    update_at = Column(db.DateTime, default=datetime.now)

    __mapper_args__ = {'order_by': [create_at.desc()]}


class Comment(db.Model, BaseMixin):
    id = Column(db.String(32), primary_key=True)
    author = db.Column(db.String(32))
    email = db.Column(db.String(254))
