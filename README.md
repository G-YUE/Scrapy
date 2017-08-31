## 安装

scrapy 框架安装方法

	1、pip3 install wheel 有请跳过；
	
	2、安装关联模块pypiwin32：pip3 install pypiwin32 有请跳过；
	
	3、在http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 
	
		下载 然后pip3 install 文件路径 安装 twisted
	
	4、pip3 install scrapy 
	
	5、python import scrapy 报错:from .. import etree ImportError: DLL load failed: 找不到指定的程序。
	
		解决办法：由于本地缺少lxml文件或是lxml文件不符
		pip3 uninstall lxml  先卸载已经安装的lxml
		官网下载新的lxml：http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml 
	
	 	下载然后 pip3 install 文件路径 安装 lxml



![](http://i.imgur.com/MpsgCCM.png)



## 基本使用

### 基本命令

	1. scrapy startproject 项目名称
	   - 在当前目录中创建中创建一个项目文件（类似于Django）
	 
	2. scrapy genspider [-t template] <name> <domain>
	   - 创建爬虫应用
	   如：
	      scrapy gensipider -t basic oldboy oldboy.com
	      scrapy gensipider -t xmlfeed autohome autohome.com.cn
	   PS:
	      查看所有命令：scrapy gensipider -l
	      查看模板命令：scrapy gensipider -d 模板名称
	 
	3. scrapy list
	   - 展示爬虫应用列表
	 
	4. scrapy crawl 爬虫应用名称
	   - 运行单独爬虫应用


### 项目结构以及爬虫应用

	project_name/

	   scrapy.cfg

	   project_name/
	       __init__.py
	       items.py
	       pipelines.py
	       settings.py
	       spiders/
	           __init__.py
	           爬虫1.py
	           爬虫2.py
	           爬虫3.py


#### 文件说明

	scrapy.cfg  项目的主配置信息。（真正爬虫相关的配置信息在settings.py文件中）
	items.py    设置数据存储模板，用于结构化数据，如：Django的Model
	pipelines    数据处理行为，如：一般结构化的数据持久化
	settings.py 配置文件，如：递归的层数、并发数，延迟下载等
	spiders      爬虫目录，如：创建文件，编写爬虫规则

例子

	import scrapy
	 
	class XiaoHuarSpider(scrapy.spiders.Spider):
	    name = "xiaohuar"                            # 爬虫名称 *****
	    allowed_domains = ["xiaohuar.com"]  # 允许的域名
	    start_urls = [
	        "http://www.xiaohuar.com/hua/",   # 其实URL
	    ]
	 
	    def parse(self, response):
			print(response.text) #字符串
			print(response.body) #字节 ,windows容易涉及到编码问题
	        # 访问起始URL并获取结果后的回调函数

关于windows编码问题：
	
	import sys,os
	sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')