# -*- coding: utf-8 -*-
# @Time : 2020/11/8
# @Author : Benny Jane
# @Email : 暂无
# @File : utils.py
# @Project : career-planning-info
# import re
import re

ignore_words = ["岗位职责：", "【岗位要求】", ]


def clean_demand(x):
    res = re.sub(r"\d、", "", x)
    res = re.sub(r"\d.", "", res)

    for w in ignore_words:
        res = res.replace(f"{w}", "")
    return res
