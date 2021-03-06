# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GotchaItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    writer = scrapy.Field()
    writed_at = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    images = scrapy.Field()
