#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: spiders/flashgame_spider.py
# Author: YourName
# mail: YourEmail
# Created Time: 2016-05-16

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.selector import Selector
from flashgame.items import FlashgameItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import codecs

class FlashgameSpider(CrawlSpider):
    name = "flashgame"
    allow_domains = ["psy525.cn"]
    start_urls = [
            "http://www.psy525.cn/cath/game0_0.html",
            "http://www.psy525.cn/cath/game0_16.html",
            "http://www.psy525.cn/cath/game0_32.html",
            "http://www.psy525.cn/cath/game0_48.html",
            "http://www.psy525.cn/cath/game0_64.html"
            ]
    rules = [Rule(SgmlLinkExtractor(allow=(r'http://www.psy525.cn/game/\d{1,2}\.html')),callback="parse_url",follow=True)]

    #for i in range(1,81):
    #    newurl="http://www.psy525.cn/game/"+str(i)+".html"
    #    start_urls.append(newurl)

    def parse_url(self,response):
        sel = Selector(response)
        base_url = get_base_url(response)
        print base_url
        items = FlashgameItem()
        items["name"] = sel.xpath('//div[@id="gameTxt"]/h1/text()').extract()[0].encode('utf-8')
        items["description"] = sel.xpath('//div[@id="gameTxt"]/span/em/text()').extract()[0].encode('utf-8')
        items["flash_url"] = sel.xpath('//div[@id="gbody"]/embed/@src').extract()[0].encode('utf-8')
        items["flash_name"] = items["flash_url"].split('/')[-1]
        return items
