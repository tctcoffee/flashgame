#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: spiders/flashgame_spider.py
# Author: YourName
# mail: YourEmail
# Created Time: 2016-05-16

from scrapy.spider import Spider
from scrapy.selector import Selector
from flashgame.items import FlashgameItem
#from scrapy.contrib.spiders import CrawlSpider,Rule
#from scrapy.contrib.linkextractors import LinkExtractor
import codecs

class FlashgameSpider(Spider):
    name = "flashgame"
    allow_domains = ["psy525.cn"]
    start_urls = []
    for i in range(1,81):
        newurl="http://www.psy525.cn/game/"+str(i)+".html"
        start_urls.append(newurl)

    def parse(self,response):
        sel = Selector(response)
        items = FlashgameItem()
        items["name"] = sel.xpath('//div[@id="gameTxt"]/h1/text()').extract()[0].encode('utf-8')
        items["description"] = sel.xpath('//div[@id="gameTxt"]/span/em/text()').extract()[0].encode('utf-8')
        items["flash_url"] = sel.xpath('//div[@id="gbody"]/embed/@src').extract()[0].encode('utf-8')
        items["flash_name"] = items["flash_url"].split('/')[-1]
        return items
