FROM python:3.6.6-slim

MAINTAINER Benny Jane

# 设置工作目录； 在镜像内部创建下面文件目录，并作为工作目录
# 创建日志目录
RUN mkdir -p /usr/src/career \
    && mkdir -p /usr/src/logs/gunicorn \
    && mkdir -p /usr/src/logs/web
WORKDIR /usr/src/career

COPY . .
RUN pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -U setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install gunicorn -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install gevent -i https://pypi.tuna.tsinghua.edu.cn/simple
# 全部合并到一个 RUN指令中，可能会出现请求超时的情况；适当拆分
RUN pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

VOLUME

EXPOSE 8010
# 需要设置host为 0.0.0.0
# 通过-p设置端口映射: 外部端口:内部端口；外部访问端口可以不用和内部一致
# 创建镜像： docker build -t name:v1.0 .
# 运行: docker run -it -p 8001:8010 image:v
# docker run -d -p 8010:8010 image:v
CMD ["gunicorn", "-c", "gunicorn.conf.py","application:app"]
