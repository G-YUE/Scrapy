# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com/hua']
    start_urls = ['http://xiaohuar.com/hua/']

    def parse(self, response):
        hxs=HtmlXPathSelector(response)
        result=hxs.select("//div[@class='item masonry_brick']").extract()
        print(result)
