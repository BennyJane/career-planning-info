# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py

from web.indexData.demand import DEMANDS
from web.indexData.jobs import JOBS_INFO
from web.indexData.profile import PROJECTS, TARGET_JOB
from web.indexData.projectInfo import PROJECT_HISTORY
from web.indexData.tags import TAGS, EXTRAS
from web.indexData.webData import WEB_DATA

__all__ = (PROJECT_HISTORY, TARGET_JOB, DEMANDS,
           TAGS, EXTRAS, WEB_DATA, JOBS_INFO)
