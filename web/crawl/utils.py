# -*- coding: utf-8 -*-
# @Time : 2020/11/8
# @Author : Benny Jane
# @Email : 暂无
# @File : utils.py
# @Project : career-planning-info
# import re
import json
import re

from .CONST import KeyWords, StopParagraph, StopWords

ignore_words = ["岗位职责：", "【岗位要求】", ]


def clean_demand(x):
    res = re.sub(r"\d、", "", x)
    res = re.sub(r"\d.", "", res)

    for w in ignore_words:
        res = res.replace(f"{w}", "")
    return res


def strToJson(x):
    demands = x.replace("[", "").replace("]", "").split("\', ")
    demands = [i.strip("'").strip() for i in demands]
    return json.dumps(demands, ensure_ascii=False)


def lowerSalary(item):
    min_salary = item.split('-')[0]
    return int(min_salary)


def keyWordMatch(word):
    lower_word = word.lower()
    return KeyWords.get(lower_word, lower_word)


def dealDemand(data):
    result = []
    src = json.loads(data)
    src = set(src)  # 借助set,集合的属性去除停用内容
    diff = src.difference(StopParagraph)
    for para in diff:
        for word in StopWords:
            if word in para or len(para) < 6:
                break
        else:  # 只有当上面for循环没有触发break,才会执行下面的逻辑
            indexSign = ['.', '、', '）', '.', '．']
            for sign in indexSign:
                para = para.split(sign)[1] if sign in para[:3] else para
            extraSign = ['\\xa0', '\r\n', '；', '\\t', '。']
            for extra in extraSign: para = para.replace(extra, "")
            para = para.strip()
            result.append(para)
    return result


def joinDemand(data):
    res = dealDemand(data)
    return '</br>'.join(res)
