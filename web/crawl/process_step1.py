# -*- coding: utf-8 -*-
# @Time : 2020/11/8
# @Author : Benny Jane
# @Email : 暂无
# @File : dealData.py
# @Project : career-planning-info
import json

import pandas as pd
from pprint import pprint
from web.crawl.utils import strToJson, keyWordMatch, lowerSalary, dealDemand
from collections import Counter

"""
提供页面展示信息：
- 优先去重复
"""


class ProcessStep1(object):
    saved_path = './cleaned'
    yearCategory = ['3-5年', '5-10年', '1-3年', '1年以内']
    salary_limit = [10, 20, 50]

    def __init__(self, path="./job_20201108.csv"):
        self.path = path
        self.df = pd.read_csv(path)
        self.dropDuplicated()

    def dropDuplicated(self):
        self.df = self.df.drop_duplicates(subset=['name', 'salary', 'tags', 'companyName', 'url'], keep='first')

    def core(self):
        total_chart = self.totalChart()
        year_chart = self.yearChart()
        tag_chart = self.tagCount()
        demand_chart = self.jobDemand()
        # pprint(locals())
        return dict(**locals())

    def totalChart(self):
        rowNum = self.df.shape[0]
        # todo 原始数据需要处理,按照更新时间降序排列
        df = self.df.groupby(by=['updateTime']).count()
        df = df.iloc[-10:, :1]
        last_update = []
        for item in df.itertuples():
            last_update.append({
                "date": item[0],
                "name": item[1]
            })
        totalStat = {
            "total": rowNum,
            "barData": last_update,
        }
        return totalStat

    def yearChart(self):
        # yearCategory = self.df['years'].unique().tolist()
        result = {}
        for year in self.yearCategory:
            result[year] = []
            df = self.df[self.df['years'] == year]
            res = df.to_dict(orient='records')
            # print(res)
            for row in res:
                result[year].append({
                    "company": row['companyName'],
                    "job": row['name'],
                    "salary": row['salary'],
                    "site": row['site'],
                    "tags": row['tags'],
                    "url": row['url'],
                })
        return result

    def tagCount(self):
        allTags = self.df['tags'].tolist()
        tags = []
        for item in allTags:
            for word in json.loads(item):
                tags.append(keyWordMatch(word))
        tagCounts = Counter(tags)
        result = sorted(tagCounts.items(), key=lambda x: x[1], reverse=True)
        return result

    def jobDemand(self):
        result = {
            "first": [],
            "second": [],
            "third": []
        }
        df = self.df.loc[:, ['salary', 'site', 'jobDemand']]
        df['stage'] = df.apply(func=lambda x: lowerSalary(x['salary']), axis=1)
        for item in df.itertuples():
            stage = item[-1]
            jobDemand = dealDemand(item[3])
            temp = {
                "salary": item[1],
                "site": item[2],
                "demands": jobDemand
            }
            if stage <= self.salary_limit[0]:
                result['first'].append(temp)
            elif stage <= self.salary_limit[1]:
                result['second'].append(temp)
            elif stage <= self.salary_limit[2]:
                result['third'].append(temp)
        # pprint(result)
        return result


if __name__ == '__main__':
    pro = ProcessStep1()
    pro.core()
