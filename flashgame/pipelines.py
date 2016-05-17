# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
import os

class FlashgamePipeline(object):

    def process_item(self, item, spider):
        url = item['flash_url']
        local = os.path.join('/root/share/python/scrapy/flashgame/downloads',item['flash_name'])
        urllib.urlretrieve(url,local)
        return item

    
