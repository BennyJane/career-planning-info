# -*- coding: utf-8 -*-
# @Time : 2020/11/21
# @Author : Benny Jane
# @Email : 暂无
# @File : webData.py
# @Project : career-planning-info


PY = [
    {
        "name": "《Python Cookbook》",
        "brief": "python3-cookbook,核心还是关于语法讲解，由浅入深，内容全面，讲解深入",
        "recommend": "4.5",
        "progress": "45%",
        "url": "https://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html",
    },
    {
        "name": "《流畅的python》",
        "brief": "进阶数据",
        "recommend": "4.7",
        "progress": "50%",
        "url": "",
    },
    {
        "name": "PythonTip",
        "brief": "算是一个python论坛，提供了在线编程、设计模式代码、算法练习题目等。（网课没看过）",
        "recommend": "3",
        "progress": "1%",
        "url": "http://www.pythontip.com/coding/code_oj",
    },
    {
        "name": "廖雪峰Python教程",
        "brief": "入门教程，面广",
        "recommend": "3.5",
        "progress": "70%",
        "url": "https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640",
    },
]

GO = [

]

GITHUB = [
    {
        "name": "incubator-superset",
        "brief": "基于python实现的数据可视化开源项目，web框架是基于Flask开发",
        "base": "python, react",
        "url": "https://github.com/apache/incubator-superset",
    },
    {
        "name": "incubator-echarts",
        "brief": "开源可视化框架，<a href='echarts.apache.org/'>echarts官网连接</a>",
        "base": "TypeScript, JavaScript",
        "url": "https://github.com/apache/incubator-echarts",
    },
]
WEB_DATA = {
    "python": sorted(PY, key=lambda x: x['recommend'], reverse=True),
    "go": GO,
    "github": GITHUB,
}
