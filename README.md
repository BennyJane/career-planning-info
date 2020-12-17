# career-planning-info
Python的职位信息


### 项目文件结构说明
```text
/web/crawl/
    职位数据抓取功能，采用无头浏览器
/web/indexData/
    首页数据配置
/web/views/
    项目路由



```



### docker 
```shell script
docker build -t career-plan:v1.0 .
docker run -it --name career_plan -p 8010:8010 career-plan:v1.0


```