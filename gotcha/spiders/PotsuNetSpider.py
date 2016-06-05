# -*- coding: utf-8 -*-

from time import gmtime, strftime

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
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//div[contains(@class, "top_area")]//h1//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//div[re:test(@class, "document_.+")]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[contains(@class, "rd_hd")]//a[re:test(@class, "member_.+")]//text()').extract()).strip()
        item['writed_at'] = u"".join(response.xpath('//div[contains(@class, "rd_hd")]//span[contains(@class, "date")]//text()').extract()).strip()
        item['url'] = unicode(response.url)
        item['category'] = u'humor'
        item['image_urls'] = response.xpath('//div[re:test(@class, "document_.+")]//img/@src').extract()

        log_msg = "Parsed: url=%(url)s\tcontent_size=%(cont_size)d\timage_count=%(img_cnt)d\tcrawled_at=%(crawled_at)s"
        log_args = {
            "url": item['url'],
            'cont_size': len(item['content']),
            'img_cnt': len(item['image_urls']),
            'crawled_at': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        }
        self.logger.info(log_msg, log_args)

        return item
