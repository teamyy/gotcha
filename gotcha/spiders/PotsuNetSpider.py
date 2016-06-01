# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gotcha.items import GotchaItem


class PotsuNetSpider(CrawlSpider):
    name = "PotsuNetSpider"
    allowed_domains = ["potsu.net"]
    start_urls = [
        'http://potsu.net/index.php?mid=humor',
    ]

    rules = (
        Rule(LinkExtractor(allow=('/index\.php\?.*mid=humor.*&.*document_srl=[0-9]+.*', )), callback='parse_humor'),
    )

    def parse_humor(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//div[contains(@class, "top_area")]//h1//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//div[re:test(@class, "document_.+")]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[contains(@class, "rd_hd")]//a[re:test(@class, "member_.+")]//text()').extract()).strip()
        item['writed_at'] = u"".join(response.xpath('//div[contains(@class, "rd_hd")]//span[contains(@class, "date")]//text()').extract()).strip()
        item['url'] = response.url
        item['category'] = 'humor'
        return item
