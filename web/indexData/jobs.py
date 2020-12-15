# -*- coding: utf-8 -*-
# @Time : 2020/11/21
# @Author : Benny Jane
# @Email : 暂无
# @File : jobs.py
# @Project : career-planning-info
from collections import namedtuple

base_info = namedtuple("job", "name tags salary company url year")

wh_jobs = [
    base_info("后端研发工程师", "多进程、多线程、MongoDB、后端开发", "8-13K", "回车换行",
              "https://www.zhipin.com/job_detail/9356400c3f3e978f1nV609u8E1VY.html?ka=search_list_jname_3_blank&lid=aJaujhU90uw.search.3",
              "1-3"),
    base_info("Python", "Mysql、PostgreSQL、Django、容器", "7-14K", "康博嘉",
              "https://www.zhipin.com/job_detail/e60d96a2dd1365ed1nR_3N24FVNR.html?ka=search_list_jname_4_blank&lid=aJaujhU90uw.search.4",
              "1-3"),
    base_info("python开发工程师", "linux、Django、容器", "8-15K", "北京深瞐",
              "https://www.zhipin.com/job_detail/0ebec478d448e6731XJy39q1FVI~.html?ka=search_list_jname_54_blank&lid=aJjNythRBcD.search.54",
              "1-3"),
    base_info("python开发工程师", "linux、Django、容器", "9-12K", "易佰网络武汉分公司",
              "https://www.zhipin.com/job_detail/9356400c3f3e978f1nV609u8E1VY.html?ka=search_list_jname_5_blank&lid=aJtHH1gnqwa.search.5",
              "1-3"),
    base_info("初级Python开发工程师", "Redis、Django、MongoDB、后端开发", "9-12K", "武汉摩博",
              "https://www.zhipin.com/job_detail/680ca4dd081b188c1nR53tq6GVBQ.html?ka=comp_joblist_1", "1-3"),
    base_info("Python工程师", "Redis、微服务架构、MongoDB、后端开发", "7-12K", "乐知加教育",
              "https://www.zhipin.com/job_detail/d9f4abd3f051b6413nN_3t-0F1c~.html?ka=search_list_jname_24_blank&lid=aJtHH1gnqwa.search.24",
              "1-3"),
]

sh_jobs = [
    base_info("Python工程师", "网络服务 python开发 Django", "10-15K", "盛迭",
              "https://www.zhipin.com/job_detail/62f6f061b0b870990HV92di4GFQ~.html?ka=search_list_jname_7_blank&lid=aJIhcWHC9B1.search.7",
              "1-3"),
    base_info("python", "Python Linux Flask RESTful", "10-15K·13薪", "汉朔公司",
              "https://www.zhipin.com/job_detail/81271351dc08de951nR939W4ElRU.html?ka=search_list_jname_11_blank&lid=aJIhcWHC9B1.search.11",
              "1-3年"),
    base_info("python", "Python web后端开发 技术方案实施", "9-14K", "黑板报",
              "https://www.zhipin.com/job_detail/ca477aa90edbfc151nV729m5FVBQ.html?ka=search_list_jname_9_blank&lid=aJIhcWHC9B1.search.9",
              "3-5"),
    base_info("python开发", "Python C++ Shell Web框架 Flask", "12-24K·13薪", "渡仁",
              "https://www.zhipin.com/job_detail/184ec43dd74838c81nRz0t67FlJX.html?ka=search_list_jname_14_blank&lid=aJIhcWHC9B1.search.14",
              "1-3年"),
    base_info("python后端开发工程师", "后端开发 精通python Django", "11-18K·16薪", "上海猛犸",
              "https://www.zhipin.com/job_detail/cf48a4390f386fa33nxy2tW_E1o~.html?ka=search_list_jname_20_blank&lid=aJIhcWHC9B1.search.20",
              "1-3年"),
    base_info("python开发工程师", "精通Flask|Mysql", "10-15K·13薪", "驻云科技",
              "https://www.zhipin.com/job_detail/08665ae9c1d996321nV72d-4FFpT.html?ka=search_list_jname_24_blank&lid=aJIhcWHC9B1.search.24",
              "1-3年"),
    # base_info("python后端开发工程师", "web后端开发 Django框架 api设计", "13-20K", "姚记科技股份",
    #           "https://www.zhipin.com/job_detail/9ab29c64d0328ddf1nR53d-5GVpR.html?ka=search_list_jname_51_blank&lid=aJIhcWHC9B1.search.51",
    #           "3-5年"),

]

JOBS_INFO = {
    "wuhan": wh_jobs,
    "shanghai": sh_jobs,
}
