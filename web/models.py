# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : models.py
# @Project : ProjectStruct-3-simple
from datetime import datetime

from extension import db

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


# 将原始信息拆分为单条工作要求来展示
class Point(db.Model):
    id = column(db.String(32), primary_key=True)
    salary = column(db.Integer, default=0)
    site = column(db.String(32), default="")
    year = column(db.String(32), default="")
    requirement = column(db.Text, default="")


class StatInfo(db.Model):
    __tablename__ = 'stat_info'
    id = column(db.String(32), primary_key=True)
    ip = column(db.String(120), default="")
    link = column(db.Boolean, default=False)  # 同一个IP在一定时间内,只允许贡献一个赞
    download = column(db.Boolean, default=False)  # 允许无限下载
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)


class WarningPara(db.Model):
    __tablename__ = 'warning_para'
    id = column(db.String(32), primary_key=True)
    para = column(db.Text, default="")
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)


class StatBrowse(db.Model):
    """使用mysql的锁机制; 统计网站浏览数据"""
    id = column(db.String(32), primary_key=True)
    ip = column(db.String(120), default="")
    # page_views = column(db.BigInteger, default=0)
    origin = column(db.String(120), default="", comment="网站视图函数名称")
    create_at = column(db.DateTime, default=datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.utcnow)
