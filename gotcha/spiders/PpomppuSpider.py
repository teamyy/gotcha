# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gotcha.items import GotchaItem


class PpomppuSpider(CrawlSpider):
    name = "PpomppuSpider"
    allowed_domains = ["www.ppomppu.co.kr"]
    start_urls = [
        'http://www.ppomppu.co.kr/zboard/zboard.php?id=humor',
    ]

    rules = (
        Rule(LinkExtractor(allow=('/zboard/view\.php\?.*id=humor.*&.*no=[0-9]+.*', )), callback='parse_humor'),
    )

    def parse_humor(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//font[contains(@class, "view_title2")]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//td[@id="realArticleView"]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//font[contains(@class, "view_name")]//text()').extract()).strip()
        item['created_at'] = u"".join(
            response.xpath('//table[contains(@class, "info_bg")]/tr[3]//td[contains(@class, "han")][2]//text()')
                    .re(u'등록일: (\d{4}-\d{2}-\d{2} \d{2}:\d{2})')).strip()
        item['url'] = response.url
        item['category'] = 'humor'
        return item
