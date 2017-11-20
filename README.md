# scrapy_medical
最近毕设，想要做一个疾病诊断系统，需要爬一些数据，正好想要学习一下scrapy框架，因此使用scrapy框架爬取了[问医网](http://jibing.wenyw.com)上的一些医疗疾病数据，里面涉及到了分页，分块，多级嵌套爬取，贴出来和大家一起学习

# 安装scrapy 和 mongodb
- pip install scrapy
- brew install mongodb

# 创建一个scrapy工程
- scrapy startproject yourproject
创建好的工程目录结构如下：
 ```
 yourproject/
    scrapy.cfg
    yourproject/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            ...
 ```
 **其中**
 - scrapy.cfg所在的目录为根目录
 - items.py为你自己需要定义的爬虫爬下来的格式
 - pipelines.py为数据的处理和导出
 - spider目录为你自己需要定义的蜘蛛的目录
 
 具体的实现可参考本工程
 
 # other
 该工程的爬虫是按照疾病的拼音，爬取所有的疾病信息，包括：病因，概述，症状，化验检查，治疗方法，并发症，如何预防，饮食保健。数据最终存储在本地的mongodb中，格式如下：
 ![](https://github.com/baiyyang/scrapy_medical/mongodb_data.png)
