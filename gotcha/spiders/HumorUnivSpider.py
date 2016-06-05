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
        item['title'] = u"".join(response.xpath('//span[@id="ai_cm_title"]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//span[@id="ai_cm_content"]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[@id="if_wrt"]//span[contains(@class, "hu_nick_txt")]//text()').extract()).strip()
        item['writed_at'] = u"".join(response.xpath('//div[@id="if_date"]/span[1]//text()').extract()).strip()
        item['url'] = unicode(response.url)
        item['category'] = u'humor'
        item['image_urls'] = response.xpath('//div[@id="cnts"]//div[contains(@id, "wrap_img")]//img/@src').extract()
        return item
