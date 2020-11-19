from flask import request
from functools import wraps


def statPageView(f):
    """统计页面访问次数"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        pass
        source = request.endpoint
        print(source)
        return f(*args, **kwargs)

    return wrapper
