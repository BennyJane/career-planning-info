# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : __init__.py.py

from web.indexData.tags import TAGS
from web.indexData.tags import EXTRAS
from web.indexData.jobs import JOBS_INFO
from web.indexData.demand import DEMANDS
from web.indexData.profile import AUTHOR
from web.indexData.profile import PROJECTS
from web.indexData.profile import TARGET_JOB
from web.indexData.learnFiles import WEB_DATA
from web.indexData.projectInfo import PROJECT_HISTORY

__all__ = (PROJECT_HISTORY, AUTHOR, TARGET_JOB, DEMANDS,
           TAGS, EXTRAS, WEB_DATA, JOBS_INFO)
