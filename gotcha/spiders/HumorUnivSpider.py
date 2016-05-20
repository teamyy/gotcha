# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gotcha.items import GotchaItem

class HumorUnivSpider(CrawlSpider):
    name = "HumorUnivSpider"
    allowed_domains = ["web.humoruniv.com"]
    start_urls = [
        'http://web.humoruniv.com/board/humor/list.html?table=pds',
    ]

    rules = (
        Rule(LinkExtractor(allow=('/board/humor/read\.html\?.*table=pds.*', )), callback='parse_pds'),
    )

    def parse_pds(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        item = GotchaItem()
        item['title'] = response.css('#ai_cm_title::text').extract()
        item['content'] = response.css('#ai_cm_content::text').extract()
        item['writer'] = response.css('#if_wrt .hu_nick_txt::text').extract()
        item['created_at'] = response.css('#if_date:first-child::text').extract()
        item['url'] = response.url
        item['category'] = 'humor'

        self.logger.info(str(item))
        return item
