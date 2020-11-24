import os
import time
import datetime
import hashlib
from _compat import win


def produceId():
    filePath = os.getcwd()
    src = filePath + str(time.time())
    m = hashlib.md5()
    m.update(src.encode('utf-8'))
    return m.hexdigest()


def getFormatDate(date=None, _format="%Y-%m-%d %H:%M:%S"):
    if date is None:
        date = datetime.datetime.now()
    return date.strftime(_format)
