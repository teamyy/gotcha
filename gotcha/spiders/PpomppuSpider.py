# -*- coding: utf-8 -*-

from time import localtime, strftime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from gotcha.items import GotchaItem


class PpomppuSpider(CrawlSpider):
    name = u"PpomppuSpider"
    identity_params = [u'no', u'id']
    allowed_domains = [u"www.ppomppu.co.kr"]
    start_urls = [
        u'http://www.ppomppu.co.kr/zboard/zboard.php?id=humor',
    ]
    rules = (
        Rule(LinkExtractor(allow=(u'/zboard/zboard\.php\?.*id=humor.*&.*page=[0-9]+.*', ),
                           deny=(u'/zboard/view\.php\?.*id=humor.*&.*no=[0-9]+.*', )), follow=True),
        Rule(LinkExtractor(allow=(u'/zboard/view\.php\?.*id=humor.*&.*no=[0-9]+.*', )), callback='parse_humor', follow=True),
    )

    def parse_humor(self, response):
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//font[contains(@class, "view_title2")]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//td[@id="realArticleView"]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//font[contains(@class, "view_name")]//text()').extract()).strip()
        item['writed_at'] = u"".join(
            response.xpath('//table[contains(@class, "info_bg")]/tr[3]//td[contains(@class, "han")][2]//text()')
                    .re(u'등록일: (\d{4}-\d{2}-\d{2} \d{2}:\d{2})')).strip()
        item['url'] = unicode(response.url)
        item['category'] = u'humor'
        item['image_urls'] = response.xpath('//td[@id="realArticleView"]//img/@src').extract()

        log_msg = "Parsed: url=%(url)s content_size=%(cont_size)d image_count=%(img_cnt)d crawled_at=%(crawled_at)s"
        log_args = {
            "url": item['url'],
            'cont_size': len(item['content']),
            'img_cnt': len(item['image_urls']),
            'crawled_at': strftime("%Y-%m-%d %H:%M:%S", localtime()),
        }
        self.logger.info(log_msg, log_args)

        return item
