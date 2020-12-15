# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : career-planning-info
# Time       ：2020/12/15 19:46
# Warning    ：The Hard Way Is Easier
import time
from flask import current_app
from _compat import win


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        release_version = current_app.config.get('RELEASE_VERSION')
        release_version = str(int(time.time())) if not release_version else release_version
        path = "/static{}?ver={}".format(path, release_version)
        return UrlManager.buildUrl(path)

    @staticmethod
    def buildImageUrl(path):
        app_config = current_app.config['APP']
        # 默认Linux环境下
        upload_path = current_app.config['UPLOAD']['prefix_url']
        if win:
            upload_path = current_app.config['UPLOAD']['win_prefix_url']

        url = "{}{}{}".format(app_config['domain'], upload_path, path)
        return url