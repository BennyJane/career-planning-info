# -*- coding: utf-8 -*-
# @Time : 2020/11/8
# @Author : Benny Jane
# @Email : 暂无
# @File : dealData.py
# @Project : career-planning-info
import json

import pandas as pd
from pprint import pprint
from web.crawl.utils import clean_demand

"""
提供页面展示信息：
- 优先去重复
"""


def strToJson(x):
    demands = x.replace("[", "").replace("]", "").split("\', ")
    demands = [i.strip("'").strip() for i in demands]
    return json.dumps(demands, ensure_ascii=False)


class ProcessStep1(object):
    saved_path = './cleaned'

    def __init__(self, path="./job_20201108.csv"):
        self.path = path
        self.df = pd.read_csv(path)
        self.dropDuplicated()

    def dropDuplicated(self):
        self.df = self.df.drop_duplicates(subset=['name', 'salary', 'tags', 'companyName', 'url'], keep='first')

    def core(self):
        total_chart = self.totalChart()
        year_chart = self.yearChart()
        pprint(locals())
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
        yearCategory = ['3-5年', '5-10年', '1-3年', '1年以内']
        result = {}

        for year in yearCategory:
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

    def correct(self):
        self.deal_job_demand()
        print(self.df['jobDemand'])
        self.df.to_csv('./job_20201108.csv', index=None)

    def deal_job_demand(self):
        self.df['jobDemand'] = self.df.apply(func=lambda x: strToJson(x['jobDemand']), axis=1)
        self.df['tags'] = self.df.apply(func=lambda x: strToJson(x['tags']), axis=1)

    def demands_to_csv(self):
        demand_df = pd.DataFrame(columns=['name', 'years', 'salary', 'demand'])
        row_num = self.df.shape[0]
        for index in range(row_num):
            years = self.df.loc[index, 'years']
            salary = self.df.loc[index, 'salary']
            name = self.df.loc[index, 'name']
            jobDemand = self.df.loc[index, 'jobDemand']
            demands = json.loads(jobDemand)
            for demand in demands:
                cleaned_res = clean_demand(demand)
                if not cleaned_res:
                    continue
                demand_df.loc[demand_df.shape[0] + 1] = [name, years, salary, cleaned_res]

        print(demand_df)
        demand_df.to_csv('./cleaned/demand_20201108.csv', index=None)


if __name__ == '__main__':
    pro = ProcessStep1()
    pro.core()
