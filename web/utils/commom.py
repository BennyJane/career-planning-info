import os
import time
import hashlib


def produceId():
    filePath = os.getcwd()
    src = filePath + str(time.time())
    m = hashlib.md5()
    m.update(src.encode('utf-8'))
    return m.hexdigest()
