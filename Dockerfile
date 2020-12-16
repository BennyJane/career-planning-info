FROM python:3.6.6-slim

MAINTAINER Benny Jane

WORKDIR /web

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
EXPOSE 8010 22 80
# 需要设置host为 0.0.0.0
# 通过-p设置端口映射: 外部端口:内部端口；外部访问端口可以不用和内部一致
# 运行: docker run -it -p 8001:8010 image:v
# docker run -d -p 8010:8010 image:v
CMD ["flask", "run", "-p" , "8010", "-h", "0.0.0.0"]