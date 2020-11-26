# -*- coding: utf-8 -*-
# @Time : 2020/11/21
# @Author : Benny Jane
# @Email : 暂无
# @File : webData.py
# @Project : career-planning-info
from collections import namedtuple

py_info = namedtuple('py', 'name brief recommend progress url')

PY = [
    py_info("《Python Cookbook》", "python3-cookbook,核心还是关于语法讲解，由浅入深，内容全面，讲解深入", "4.5", "45%",
            "https://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html"),
    py_info("《流畅的python》", "进阶数据", "4.7", "50%", ""),
    py_info("PythonTip", "算是一个python论坛，提供了在线编程、设计模式代码、算法练习题目等。（网课没看过）", "3", "1%",
            "http://www.pythontip.com/coding/code_oj"),
    py_info("廖雪峰Python教程", "入门教程，面广", "3.5", "70%",
            "https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640"),
]

GO = [

]

git_info = namedtuple('git', 'name brief base url')

GITHUB = [
    git_info("incubator-superset", "基于python实现的数据可视化开源项目，web框架是基于Flask开发", "python, react",
             "https://github.com/apache/incubator-superset"),
    git_info("incubator-echarts", "开源可视化框架，<a href='echarts.apache.org/'>echarts官网连接</a>", "TypeScript, JavaScript",
             "https://github.com/apache/incubator-echarts"),
    git_info("", "", "", ""),
]
WEB_DATA = {
    "python": sorted(PY, key=lambda x: x.recommend, reverse=True),
    "go": GO,
    "github": GITHUB,
}
