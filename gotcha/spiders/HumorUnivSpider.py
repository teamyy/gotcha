# -*- coding: utf-8 -*-

from time import localtime, strftime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from gotcha.items import GotchaItem


class HumorUnivSpider(CrawlSpider):
    name = "HumorUnivSpider"
    identity_params = ['table', 'number']
    allowed_domains = ["web.humoruniv.com"]
    start_urls = [
        'http://web.humoruniv.com/board/humor/list.html?table=pds',
    ]

    rules = (
        Rule(LinkExtractor(allow=('/board/humor/list\.html\?.*table=pds.*&.*pg=[0-9]+.*', ),
                           deny=('/board/humor/read\.html\?.*table=pds.*', )), follow=True),
        Rule(LinkExtractor(allow=('/board/humor/read\.html\?.*table=pds.*', )), callback='parse_pds', follow=True),
    )

    def parse_pds(self, response):
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//span[@id="ai_cm_title"]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//span[@id="ai_cm_content"]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[@id="if_wrt"]//span[contains(@class, "hu_nick_txt")]//text()').extract()).strip()
        item['writed_at'] = u"".join(response.xpath('//div[@id="if_date"]/span[1]//text()').extract()).strip()
        item['url'] = unicode(response.url)
        item['category'] = u'humor'
        item['image_urls'] = response.xpath('//div[@id="cnts"]//div[contains(@id, "wrap_img")]//img/@src').extract()

        log_msg = "Parsed: url=%(url)s content_size=%(cont_size)d image_count=%(img_cnt)d crawled_at=%(crawled_at)s"
        log_args = {
            "url": item['url'],
            'cont_size': len(item['content']),
            'img_cnt': len(item['image_urls']),
            'crawled_at': strftime("%Y-%m-%d %H:%M:%S", localtime()),
        }
        self.logger.info(log_msg, log_args)

        return item
