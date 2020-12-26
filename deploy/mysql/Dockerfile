ARG MYSQL_VER

FROM mysql:${MYSQL_VER}

# 设置时区为上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Ubuntu软件源选择中国的服务器
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# 更新安装依赖包
RUN apt-get update && apt-get install -y \
        vim \
        wget
#ADD setup.sh /mysql/setup.sh
#ADD create.sql /mysql/create.sql
# 初始化的时候运行create.sql脚本
ADD create.sql /docker-entrypoint-initdb.d

#CMD ["sh", "/mysql/setup,sh"]


