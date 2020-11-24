FROM python:3.6.6-slim

MAINTAINER Benny Jane

WORKDIR /web

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
EXPOSE 8010 22 80

CMD ["flask", "run", "-p" , "8010"]