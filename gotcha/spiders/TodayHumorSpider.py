# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gotcha.items import GotchaItem

class TodayHumorSpider(CrawlSpider):
    name = "TodayHumorSpider"
    allowed_domains = ["www.todayhumor.co.kr"]
    start_urls = [
        'http://www.todayhumor.co.kr/board/list.php?table=humordata',
    ]

    rules = (
        Rule(LinkExtractor(allow=('/board/view\.php\?.*table=humordata.*', ), deny=('/board/view\.php\?.*no_tag=1.*', )), callback='parse_humor'),
    )

    def parse_humor(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//div[@id="containerInner"]//div[contains(@class, "viewSubjectDiv")]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//div[@id="containerInner"]//div[contains(@class, "viewContent")]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[@id="containerInner"]//div[contains(@class, "writerInfoContents")]/div[2]//font//text()').extract()).strip()
        item['created_at'] = u"{}-{}-{} {}:{}:{}".format(*response.xpath('//div[@id="containerInner"]//div[contains(@class, "writerInfoContents")]/div[7]//text()').re(u'\d+'))
        item['url'] = response.url
        item['category'] = 'humor'

        return item
