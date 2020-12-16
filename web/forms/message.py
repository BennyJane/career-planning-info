# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/16 12:12
# Warning    ：The Hard Way Is Easier
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import Length
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    email = StringField("邮箱", default="", description="需要单独回复，请输入个人邮箱")
    body = TextAreaField("留言内容", description="留言内容限制为300字",
                         validators=[DataRequired(), Length(1.200)])
    submit = SubmitField("提交")
