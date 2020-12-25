# career-planning-info
Python的职位信息；
项目网站URL：http://career.pygorun.com/

### 项目文件结构说明
```text
/_compat             版本、平台兼容处理
/deploy/             部署配置文件
/logs/               日志文件
/static/             静态文件
/templates/          模板文件
/web
    /crawl/          招聘数据抓取功能
    /forms/          页面表单
    /indexData/      首页数据配置
    /models/         项目数据模型
    /utils/          工具类
    /views/          项目路由
    /__init__.py     APP创建函数
    /cli.py          自定义终端命令
    /constant.py     项目常量
    /errors.py       异常处理
    /fake.py         测试数据生成
    /log.py          项目日志配置
    /template_ext.py 模板函数与过滤器添加
.env                 环境变量
.flaskenv            环境变量
application.py       app实例创建
config.py            项目配置信息
gunicorn.conf.py     gunicorn的配置信息

```

### 本地运行
1. 搭建本地PY环境
```bash
pip install -r requirement.txt
```
2. 本地需要运行MYSQL、Redis
3. 更改配置信息
```shell script
# 主要修改下面两处
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:password@localhost:3306/career_plan_service?charset=utf8mb4
WEBHOOK="企业微信机器人URL"
```

4. 运行
```shell script
flask run
```


### 使用docker运行项目
```shell script
# docker 运行项目： 本地测试使用
docker build -t career-plan:v1.0 .
docker run -it --name career_plan -p 8010:8010 career-plan:v1.0
docker run -it --name career -p 8010:8010 career-plan:v1.0

# docker-compose 运行项目： 线上部署使用
docker-compose build .
docker-compose up -d
```

### TODO
- 后端数据库由Mysql改为Redis
- 优化页面加载速度