# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : models.py
# @Project : ProjectStruct-3-simple
from datetime import datetime

from web.extension import db

column = db.Column


# 抓取的原始数据
class JobInfo(db.Model):
    __tablename__ = 'job_info'
    id = column(db.String(32), primary_key=True)
    name = column(db.String(128), nullable=False)
    salary = column(db.Integer, nullable=False, default=0)
    year = column(db.String(32), nullable=False, default="")
    site = column(db.String(32), nullable=False, default="")
    responsibility = column(db.Text, nullable=False, default="")
    demand = column(db.Text, nullable=False, default="")
    other = column(db.Text, nullable=False, default="")
    source = column(db.Text, nullable=False, default="")
    source_id = column(db.String(32), nullable=False, default="")
    source_url = column(db.Text, nullable=False, default="")
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)


class WarningPara(db.Model):
    __tablename__ = 'warning_para'
    id = column(db.String(32), primary_key=True)
    para = column(db.Text, default="")
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)


class StatInfo(db.Model):
    __tablename__ = 'stat_info'
    id = column(db.String(32), primary_key=True)
    ip = column(db.String(120), default="")
    action = column(db.String(32), default='', comment="访客行为: like-点赞, download-下载")
    count = column(db.INTEGER, default=0, comment="统计单个IP下载次数")  # 允许无限下载
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)

    __mapper_args__ = {'order_by': [create_at.desc()]}


class StatBrowse(db.Model):
    """使用mysql的锁机制; 统计网站浏览数据"""
    id = column(db.String(32), primary_key=True)
    ip = column(db.String(120), default="")
    # page_views = column(db.BigInteger, default=0)
    origin = column(db.String(120), default="", comment="网站视图函数名称")
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)

    __mapper_args__ = {'order_by': [create_at.desc()]}
