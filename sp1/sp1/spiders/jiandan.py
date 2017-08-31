# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.selector import Selector, HtmlXPathSelector
import requests,time

class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net/ooxx']
    start_urls = ['http://jandan.net/ooxx/']
    img_num=0
    img_path="img/"
    def parse(self, response):
        xsm = HtmlXPathSelector(response)
        # img_list = xsm.select("//div[@class='text']//img/@src").extract()
        img_list = xsm.select("//div[@class='text']//a[@class='view_img_link']/@href").extract()
        for img_url in img_list:
            if "jpg" in img_url:
                callback=self.img_jpg
            elif "gif" in img_url:
                callback=self.img_gif
            else:
                callback=self.img_jpg
            yield Request("http:"+img_url,
                          callback=callback,
                          dont_filter=True,
                          headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400",
                                   "Referer":"http://jandan.net/ooxx",
                                   "Host":"ws2.sinaimg.cn",
                                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                                   }
                          )
        next_url=xsm.select("//div[@class='comments']//div[@class='cp-pagenavi']//a[@class='previous-comment-page']/@href").extract_first()
        yield Request(next_url,callback=self.parse,dont_filter=True)
    def img_jpg(self, response):
        print("..............正在下载第%s张图片"%(self.img_num+1))
        with open(self.img_path+"%s.jpg"%(self.img_num),"wb") as f:
            f.write(response.body)
        self.img_num+=1
    def img_gif(self, response):
        print("..............正在下载第%s张图片"%(self.img_num+1))
        with open(self.img_path+"%s.gif"%(self.img_num),"wb") as f:
            f.write(response.body)
        self.img_num+=1