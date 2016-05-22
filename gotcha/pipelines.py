# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urlparse import urlparse

from scrapy.exceptions import DropItem


class GotchaPipeline(object):
    def process_item(self, item, spider):
        return item


class PotsuNetAdminArticleDropPipeline(object):
    def process_item(self, item, spider):
        writer = item['writer']
        domain = urlparse(item['url']).netloc

        if domain in [u"potsu.net", "potsu.net"] and writer in [u"potsu", "potsu"]:
            raise DropItem("Admin's article in potsu.net was dropped (url: %s)" % item['url'])

        return item
