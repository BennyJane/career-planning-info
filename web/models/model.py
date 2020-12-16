# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 21:52
# Warning    ：The Hard Way Is Easier
from datetime import datetime
from web.extension import db
from web.models import Column
from web.models import TimeMixin
from web.constant import ROLE_INFO
from web.utils.libs import produceId


class User(db.Model, TimeMixin):
    __tablename__ = 'user'
    id = Column(db.String(32), primary_key=True)
    username = Column(db.String(32))
    email = Column(db.String(64), default="", comment="留言者的邮箱")
    avatar = Column(db.Text, default="", comment="base64格式存储的用户头像")
    is_admin = Column(db.Boolean, default=False, comment="是否是网站的管理者")

    messages = db.relationship("Message", back_populates='user')

    def __init__(self, *args, **kwargs):
        if "id" not in args and "id" not in kwargs:
            _id = produceId()
            kwargs["id"] = _id
        super().__init__(*args, **kwargs)

    @staticmethod
    def insert_data():
        """添加默认信息"""
        for role in ROLE_INFO:
            user = User.query.filter(User.email == role.email).first()
            if user is None:
                user.username = role.name
                user.email = role.email
                user.avatar = role.avatar
                user.is_admin = role.role
            else:
                user = User(username=role.name, email=role.email, avatar=role.avatar, is_admin=role.role)
            db.session.add(user)
        db.session.commit()


class Message(db.Model, TimeMixin):
    __tablename__ = 'message'
    id = Column(db.String(32), primary_key=True)
    body = Column(db.Text, comment="留言内容")
    reviewed = Column(db.Boolean, default=False, comment="是否已经被审核")

    user_id = Column(db.String(32), db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates='messages')

    def __init__(self, *args, **kwargs):
        if "id" not in args and "id" not in kwargs:
            _id = produceId()
            kwargs["id"] = _id
        super().__init__(*args, **kwargs)

    @property
    def msg_params(self):
        meg_info = {
            "id": self.id,
            "name": self.user.username,
            "email": self.user.email,
            "avatar": self.user.avatar,
            "body": self.body,
            "reviewed": self.reviewed,
            "from_admin": self.user.is_admin  # 是否为网站维护者
        }
        return meg_info


class WarningPara(db.Model, TimeMixin):
    __tablename__ = 'warning_para'
    id = Column(db.String(32), primary_key=True)
    para = Column(db.Text, default="")

    def __init__(self, *args, **kwargs):
        if "id" not in args and "id" not in kwargs:
            _id = produceId()
            kwargs["id"] = _id
        super().__init__(*args, **kwargs)


class StatInfo(db.Model):
    __tablename__ = 'stat_info'
    id = Column(db.String(32), primary_key=True)
    ip = Column(db.String(120), default="")
    action = Column(db.String(32), default='', comment="访客行为: like-点赞, download-下载")
    count = Column(db.INTEGER, default=0, comment="统计单个IP下载次数")  # 允许无限下载
    create_at = Column(db.DateTime, default=datetime.now)
    update_at = Column(db.DateTime, default=datetime.now)

    __mapper_args__ = {'order_by': [create_at.desc()]}

    def __init__(self, *args, **kwargs):
        if "id" not in args and "id" not in kwargs:
            _id = produceId()
            kwargs["id"] = _id
        super().__init__(*args, **kwargs)


class StatBrowse(db.Model):
    """使用mysql的锁机制; 统计网站浏览数据"""
    id = Column(db.String(32), primary_key=True)
    ip = Column(db.String(120), default="")
    # page_views = Column(db.BigInteger, default=0)
    origin = Column(db.String(120), default="", comment="网站视图函数名称")
    create_at = Column(db.DateTime, default=datetime.now)
    update_at = Column(db.DateTime, default=datetime.now)

    __mapper_args__ = {'order_by': [create_at.desc()]}

    def __init__(self, *args, **kwargs):
        if "id" not in args and "id" not in kwargs:
            _id = produceId()
            kwargs["id"] = _id
        super().__init__(*args, **kwargs)
