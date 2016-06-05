# -*- coding: utf-8 -*-

from time import gmtime, strftime

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
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//span[@id="ai_cm_title"]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//span[@id="ai_cm_content"]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[@id="if_wrt"]//span[contains(@class, "hu_nick_txt")]//text()').extract()).strip()
        item['writed_at'] = u"".join(response.xpath('//div[@id="if_date"]/span[1]//text()').extract()).strip()
        item['url'] = response.url
        item['category'] = 'humor'

        log_msg = "Parsed: url=%(url)s\tcontent_size=%(cont_size)d\timage_count=%(img_cnt)d\tcrawled_at=%(crawled_at)s"
        log_args = {
            "url": item['url'],
            'cont_size': len(item['content']),
            'img_cnt': len(item['image_urls']),
            'crawled_at': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        }
        self.logger.info(log_msg, log_args)
        return item
