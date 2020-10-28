# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : models.py
# @Project : ProjectStruct-3-simple
import datetime

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
    create_at = column(db.DateTime, default=datetime.datetime.utcnow)
    update_at = column(db.DateTime, default=datetime.datetime.utcnow)


# 将原始信息拆分为单条工作要求来展示
class Point(db.Model):
    id = column(db.String(32), primary_key=True)
    salary = column(db.Integer, default=0)
    site = column(db.String(32), default="")
    year = column(db.String(32), default="")
    requirement = column(db.Text, default="")
