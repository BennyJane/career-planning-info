# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : crawl_data.py
# @Project : career-planning-info
import datetime
import json
import logging
import random
import time
from pprint import pprint

import pandas as pd
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

CHROME_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

columns = ["name", "salary", "site", "years", "school", "tags", "updateTime", "companyName", "jobDemand", "companyInfo",
           "address", "url"]

df = pd.DataFrame(columns=columns)


class Crawl:
    # origin_url = "https://m.zhipin.com/wapi/zpgeek/mobile/jobs.json?query=python%E5%BC%80%E5%8F%91&page={}&city=100010000&query=python%E5%BC%80%E5%8F%91"
    origin_url = "https://m.zhipin.com/c100010000/?query=python%E5%BC%80%E5%8F%91&page={}"
    # origin_url = 'https://m.zhipin.com/job_detail/c2e3ca074472dc5a0XZ529-7E1M~.html'

    # 详情页面的url前缀
    detail_url_prefix = 'https://m.zhipin.com'
    token = {
        # 登录状态的cookie
        "Cookie": "lastCity=101200100; _bl_uid=U2kbygbzfyv8CUrp33tpuqwysyj1; t=PGJsCaAUwh54GG7h; wt=PGJsCaAUwh54GG7h; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1603895866,1603907976,1604498060,1604708969; JSESSIONID=""; __c=1604498060; __l=l=%2Fm.zhipin.com%2Fjob_detail%2F&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.a00000KEJeCxDFezE_mHhxCP0_fBj-g4bqmwBIedaqGUARXHdGAjHCFS6jf9-x1b9vbUQtV1pRNCW3P6av_5MBzDWq7pGwYg0VB97UB0U2x2x8sGhXZbG1_Wkvusp_UNH4QSs1ZdUqTUBXzFi21sUr3godwPm8OKQ3Qkjs275FTQrcV_h30L_8wH3ZCr09R_FK_KFOqkn0u-1Me8SLZwqpvvybUh.DY_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMks4OgSWS534Oqo4yunOogEOtZV_zyUr1oWC_kng8WWsSXOj__seOU9tOZjEen5Vvmx5u9qEdse5-dsw5Cnmx5Gse5gjEqT5M_se2trOudeRlrKYd1AZ1vmxyEj_lT5M33IOZjeXrZ1tT5ot_rSEj4qrZul3IOo9tqhZug9Ler_nU_DY2yQLfYQS_zUM1F9CnNR2Ar5jkq8ZFqTrHltZKsXgjROASFAZFqmYlTrHldvTd2s1f_TX1_lIz6.U1Yk0ZDqVohslVgfko60TA-W5H00Ijvv8UjJ1xWNYnp30A-V5HczPfKM5yqbXWD0Iybqmh7GuZR0TA-b5HDv0APGujY1P1D0UgfqnH0krNtknjDLg1csPH7xnH0vnNt1PW0k0AVG5H00TMfqQHD0mhbqnHRdg1Ddr7tznjwxnWDL0AdW5HDsnj7xnH6vPHmYrHbvn-tznjRkg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5Hc0TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyPV0A-bm1dRfsKYmgFMugfqPWPxn7tkPHn0IZN15H6vrjRknW6vPW0dn1TYPWT3nHn0ThNkIjYkPW0YPjb3njRdrHfv0ZPGujd9uHnLPhDsmW0snjD1PjTv0AP1UHY3wW0sP1-APbcswRRYfYfs0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KbugwxmLK95H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tYn1DsrHbdg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KbmvPb5fKYTh7buHYLPW0znjc0mhwGujY0UvnqnfKBIjYs0Aq9IZTqn0KEIjYk0AqzTZfqnBnsc1Dsc1cWrj0zrHnsnWDWnWDsnj0WnWDsnj08nj0snj0sc1DWnBnsczYWna3snH0sP1cWni3snj0knj00TNqv5H08rHFxna3sn7tsQW0sg108nW9xna3kPNtsQWn10AF1gLKzUvwGujYs0APzm1YzP1bvPf%26word%3D%26ck%3D7953.1.91.866.150.867.158.375%26shh%3Dwww.baidu.com%26us%3D1.0.1.0.0.0.0%26wd%3D%26bc%3D110101&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3Dboss%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%26unit%3D%25E6%258B%259B%25E8%2581%2598%26keyword%3D%25E8%25B1%2586%25E7%2593%25A3%25E7%25BD%2591%25E6%258B%259B%25E8%2581%2598%26bd_vid%3D4447578348948207790%26csource%3Dboctb&friend_source=0&friend_source=0; __a=52560607.1603032689.1603895866.1604498060.208.5.11.11; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1604764198; __zp_stoken__=7226bWGJ5FHALXxI8ZmNgI3J4GS45CA18DiFndhU7LjFICxIEdBAlWX9THC5rfik6LTsPNToGNhNMPA8PcypAbFRDRw0BQ2JPDkEzEEIdEEoZbn94VT87E30pfytneUcBK2oFJnVnRGdnQDBsDQ%3D%3D"
    }

    def __init__(self, page_total=10):
        self.page_list = []
        self.root = None
        self.driver = None
        self.page_total = page_total

    def startWebDriver(self):
        # 启动无头浏览器
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(firefox_options=options)  # Firefox浏览器
        wait = WebDriverWait(self.driver, 3)  # 超时时长为10s

    def getPageList(self):
        self.startWebDriver()
        for i in range(5, self.page_total):
            pageUrl = self.origin_url.format(i)
            # pageUrl = self.origin_url
            try:
                self.driver.get(pageUrl)  # 这次返回的是 521 相关的防爬js代码
                # driver.get(pageUrl)  # 调用2次 browser.get 解决 521 问题
                page_html = self.driver.page_source
                self.root = etree.HTML(page_html)
                page_job_urls = self.jobUrl()
                for url in page_job_urls:
                    content_url = self.detail_url_prefix + url
                    self.driver.get(content_url)
                    content_html = self.driver.page_source
                    self.root = etree.HTML(content_html)
                    self.parse(url)
                    time.sleep(10 + random.random() * 1.2)
            except Exception as e:
                logging.info(e)
            finally:
                self.save()

        self.save()

    def parse(self, url):
        name = self.jobName()
        salary = self.salary()
        site = self.site()
        years = self.years()
        school = self.school()
        tags = self.tags()
        updateTime = self.updateTime()
        companyName = self.companyName()
        jobDemand = self.jobDemand()
        companyInfo = self.companyInfo()
        address = self.address()

        params = dict(**locals())
        del params['self']
        # del params['f']
        pprint(params)

        isExit = df[df['url'] == url]
        # print('=================', isExit)
        if isExit.shape[0] == 0:
            if all([name, salary, site, jobDemand]):
                df.loc[df.shape[0] + 1] = [name, salary, site, years, school, tags, updateTime, companyName, jobDemand,
                                           companyInfo, address, url]

    def save(self):
        if df.shape[0] != 0:
            date = datetime.datetime.now()
            date = str(date)[:10]
            path = f'./result/job_{date}.csv'
            df.to_csv(path, index=None)

    def jobUrl(self):
        res = self.root.xpath("//li[@class='item']/a/@href")
        return res

    def jobName(self):
        res = self.root.xpath("//div[@class='job-banner']/h1/text()")
        if res:
            res = res[0].strip()
        return res

    def salary(self):
        res = self.root.xpath("//div[@class='job-banner']/h1/span/text()")
        if res:
            res = res[0].strip()
        return res

    def site(self):
        res = self.root.xpath("//div[@class='job-banner']/p/a/text()")
        if res:
            res = res[0].strip()
        return res

    def years(self):
        res = self.root.xpath("//div[@class='job-banner']/p//text()")
        if res:
            res = [item.strip() for item in res if item.strip()]
            res = res[1]
        return res

    def school(self):
        res = self.root.xpath("//div[@class='job-banner']/p//text()")
        if res:
            res = [item.strip() for item in res if item.strip()]
            res = res[-1]
        return res

    def tags(self):
        res = self.root.xpath("//div[@class='job-banner']/div[@class='job-tags']//text()")
        if res:
            res = [item.strip() for item in res if item.strip()]
            res = json.dumps(res, ensure_ascii=False)
        return res

    def updateTime(self):
        res = self.root.xpath("//div[@class='job-banner']/div[@class='time']/text()")
        if res:
            res = res[0].strip()
        return res

    def companyName(self):
        res = self.root.xpath("//div[@class='job-author']/div[@class='info-primary']/p/text()")
        if res:
            res = res[0].strip()
        return res

    def jobDemand(self):
        res = self.root.xpath("//div[@class='job-detail']/div[@class='detail-content']/div/div[@class='text']//text()")
        if res:
            res = [item.strip().strip('\r\n').replace(' ', '').replace('\n', '') for item in res if item.strip()]
            res = json.dumps(res, ensure_ascii=False)
        return res

    def companyInfo(self):
        res = self.root.xpath("//div[@class='job-detail']/div[@class='detail-content']/div[2]/p//text()")
        if res:
            res = [item.strip().strip('\r\n').replace(' ', '').replace('\n', '') for item in res if item.strip()]
            res = '\n'.join(res)
        return res

    def address(self):
        res = self.root.xpath(
            "//div[@class='job-detail']/div[@class='detail-content']/div[@class='job-sec']/div[@class='job-location']//text()")
        if res:
            res = [item.strip().strip('\r\n').replace(' ', '').replace('\n', '') for item in res if item.strip()]
            res = '\n'.join(res)
        return res

    def testIndex(self):
        with open("./targetHtml/index.html", 'r', encoding='utf-8') as f:
            html = f.read()
            self.root = etree.HTML(html)
            # print(html)
        self.jobUrl()

    def testContent(self):
        with open("./targetHtml/content.html", 'r', encoding='utf-8') as f:
            html = f.read()
            self.root = etree.HTML(html)

        name = self.jobName()
        salary = self.salary()
        site = self.site()
        years = self.years()
        school = self.school()
        tags = self.tags()
        updateTime = self.updateTime()
        companyName = self.companyName()
        jobDemand = self.jobDemand()
        companyInfo = self.companyInfo()
        address = self.address()

        params = dict(**locals())
        del params['html']
        del params['f']
        pprint(params)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.getPageList()
    # crawl.testIndex()
    # crawl.testContent()
