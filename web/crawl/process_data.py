# -*- coding: utf-8 -*-
# @Time : 2020/11/8
# @Author : Benny Jane
# @Email : 暂无
# @File : dealData.py
# @Project : career-planning-info
import json

import pandas as pd

from web.crawl.utils import clean_demand

"""
功能：
- 抓取数据的清理
- 数据格式整理
- 数据存储到数据库
"""


def strToJson(x):
    demands = x.replace("[", "").replace("]", "").split("\', ")
    demands = [i.strip("'").strip() for i in demands]
    return json.dumps(demands, ensure_ascii=False)


class ProcessData(object):
    saved_path = './cleaned'

    def __init__(self, path="./job_20201108.csv"):
        self.path = path
        self.df = pd.read_csv(path)

    def core(self):
        # print(self.df)
        res = self.df['jobDemand'].unique().tolist()
        # print(res)
        all_demand = []
        for item in res:
            demands = json.loads(item)
            all_demand.extend(demands)
            # break
        print(set(all_demand))
        # print(res)

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
    pro = ProcessData()
    # pro.core()
    pro.demands_to_csv()
    # pro.correct()
