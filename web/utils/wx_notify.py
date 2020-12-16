# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/16 20:49
# Warning    ：The Hard Way Is Easier
from pprint import pprint
import json
import requests
from web.constant import NOTIFY_NEW_MESSAGE_TEMPLATE
from _compat import get_key_form_env


class WXNotify:
    """无法单独使用，必须在Flask上线文中才能获取环境变量"""
    webhook = get_key_form_env("WEBHOOK")
    if not webhook:
        raise Exception("请在环境变量中配置微信机器人的URL：WEBHOOK=URL ")
    headers = {
        "Content-Type": "application/json"
    }

    markdown_type = {
        "msgtype": "markdown",
        "markdown": {
            "content": ""}
    }

    def __init__(self):
        """"""

    def new_message(self, params):
        self.markdown_type["markdown"]["content"] = NOTIFY_NEW_MESSAGE_TEMPLATE.format(**params).strip()
        message_params = json.dumps(self.markdown_type, ensure_ascii=True)  # 需要转化为JSON格式数据
        res = requests.post(self.webhook, headers=self.headers, data=message_params)
        if res.status_code != 200:
            raise Exception("企业微信通知消息发送失败： {}".format(params))
        return True


wx_notify = WXNotify()

if __name__ == '__main__':
    test_data = {
        "msg": "测试消息",
        "name": "benny jane",
        "email": "",
    }
    n = WXNotify()
    n.new_message(test_data)
