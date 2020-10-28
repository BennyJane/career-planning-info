# -*- coding: utf-8 -*-
# @Time : 2020/10/28
# @Author : Benny Jane
# @Email : 暂无
# @File : crawl_data.py
# @Project : career-planning-info
import re
from lxml import etree

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
driver = webdriver.Firefox(firefox_options=options)  # Firefox浏览器
CHROME_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'


class Crawl:
    origin_url = "https://m.zhipin.com/job_detail/?city=101200100&source=10&query=python%E5%BC%80%E5%8F%91"
    # origin_url = "ttps://m.zhipin.com/job_detail/?city=101200100&source=10&query=python%E5%BC%80%E5%8F%91"
    # origin_url = 'https://m.zhipin.com/job_detail/a0cb67d51aa33f023nVz2N25GFs~.html?ka=job_sug_6'
    token = {
        "Cookie": "lastCity=101200100; _bl_uid=U2kbygbzfyv8CUrp33tpuqwysyj1; t=PGJsCaAUwh54GG7h; wt=PGJsCaAUwh54GG7h; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1603105640,1603625109,1603895866,1603907976; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1603908003; __c=1603895866; __l=l=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%252Fc101210100%26bd_vid%3D7123686881180887714%26csource%3D&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.060000KKXYb9K48fSegrv6TQbIdx5jcO3if8iQcvCQDKAqjq2Mg0J_0XNaRT1S-_NTy6W5cM4k-vv2Io2-p-Jnz19OcH-NqUgS0KzjQKSTP-xFns_CXQVURMbloD-LKaHvEO3E1j1VD5CXJreSL-RGzDBLl2aEETA8YNpikef5WDgyV-SVC2U_JUXdmnR1Qj8l3kK8aaqEWgHtk_SF2fIAgH6pJk.Db_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMsSXej_SyZu43x5I9LtTrzEj4e_r14mIOVsSxW9LOQjlOy1FepqMO6qVMH3eS8rB1Dk9tqhZvd3IMs3x5_sS81jEq8Z1LmxU43IOVsSxH9vXLjELut5M8seSrZug9tOZj_L3IMsqTDHlj7eC3t5M33IOo9qX1j4enrzEjEvIXdrW6IPTksTZK4TPHtU3bffdvN42e2eQr_zUM1F9CnNR2Ar5Od663rj6t8AGSPticcYlm2erp-muCyrrO_tpd0.U1Yk0ZDqmhq1TsKspynqn0KsTv-MUWYsPW--nAPbrHPhnvw9mHFBmyDYuH64rjFbuWcLnW6YrfKY5gILIzRzwgGCpgKGUBRzwyPEUiRzwhnknjDznH0knj00pyYqnWcd0ATqTZn10ZNG5yF9pywd0ZKGujYkP6KWpyfqn1Tk0AdY5HDsnH-xnH0kPdtznjRkg1csPWFxnH0zndt1nj0Lg1nvnjD0pvbqn0KzIjYVnfKBpHYkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PWRvPjb4nWPxnW0dnNtkrjRzn104nHRYn-tkg1DsnNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1Qy4J0A-bm1dri6KYmgFMugfqPWPxn7t1nj00IZN15H6snWTzrjDsn1RLPjnknWTsrHR0ThNkIjYkPW01rH0LrHT1PWDv0ZPGujdhP1u-nWczuH0snjP-Pvmz0AP1UHdDfYwjwbP7rj0LwjN7PW6s0A7W5HD0IZNY5HD0TA3qn0KkUgfqn0KkUgnqn0KbugwxmLK95H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn7t1nj0zg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7tsg1fkP1n4nj7xn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0KlTAkdT1Ys0A7buhk9u1Y30Akhm1Ys0AwWmvfq0Zwzmyw-5HTvnjcsn6KBuA-b5fKEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBnzPjcvrHcsnin1nj0sc1nsnj08nj0snj0sc1DWnBnsc1Dsc108nj0vPHbzc1D8nj0snH0s0Z7xIWYsQWT1g108njKxna3sn7tsQWc4g108nWwxna3zrfKBTdqsThqbpyfqn0KWThnqPWRYPjm%26ck%3D1634.4.117.292.175.542.274.126%26shh%3Dwww.baidu.com%26us%3D1.0.1.0.0.0.0%26wd%3D%26bc%3D110101&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%252Fc101210100%26bd_vid%3D7123686881180887714%26csource%3D&friend_source=0&friend_source=0; __a=52560607.1603032689.1603625114.1603895866.187.4.94.10; __zp_stoken__=9405bPDx4XVxkQDoPVFAEZytjfCwzE0wBSVgvalIxe0ogajs3YRJoFHgeV3wxNhZBfkdKUXMYVURObTkkQWoRZ2QrHHo5KS5mVwdtVHVMKFkMcnYcOzgvJSx%2FLy9GaH0BeBZAQmBnJD9PZAlHOQ%3D%3D"
    }

    def __init__(self):
        self.page_list = []

    def getPageList(self):

        pageUrl = self.origin_url
        wait = WebDriverWait(driver, 3)  # 超时时长为10s
        driver.get(pageUrl)  # 这次返回的是 521 相关的防爬js代码
        # driver.get(pageUrl)  # 调用2次 browser.get 解决 521 问题
        Html = driver.page_source
        print(Html)
        root = etree.HTML(Html)

        print(root)
        return root

    def job_page(self, src):
        res = re.findall(r"<a href=\"(^[\"]*)\" ka=", src)
        print(res)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.getPageList()
