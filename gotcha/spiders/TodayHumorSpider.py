# -*- coding: utf-8 -*-

from time import localtime, strftime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from gotcha.items import GotchaItem


class TodayHumorSpider(CrawlSpider):
    name = u"TodayHumorSpider"
    identity_params = [u'no', u'table']
    allowed_domains = [u"www.todayhumor.co.kr"]
    start_urls = [
        u'http://www.todayhumor.co.kr/board/list.php?table=humordata',
    ]

    rules = (
        Rule(LinkExtractor(allow=(u'/board/list\.php\?.*table=humordata.*&.*page=[0-9]+.*', ),
                           deny=(u'/board/view\.php\?.*table=humordata.*', '/board/view\.php\?.*no_tag=1.*', )), follow=True),
        Rule(LinkExtractor(allow=(u'/board/view\.php\?.*table=humordata.*', ), deny=('/board/view\.php\?.*no_tag=1.*', )), callback='parse_humor', follow=True),
    )

    def parse_humor(self, response):
        item = GotchaItem()
        item['title'] = u"".join(response.xpath('//div[@id="containerInner"]//div[contains(@class, "viewSubjectDiv")]//text()').extract()).strip()
        item['content'] = u"".join(response.xpath('//div[@id="containerInner"]//div[contains(@class, "viewContent")]//text()').extract()).strip()
        item['writer'] = u"".join(response.xpath('//div[@id="containerInner"]//div[contains(@class, "writerInfoContents")]/div[2]//font//text()').extract()).strip()
        item['writed_at'] = u"{}-{}-{} {}:{}:{}".format(*response.xpath('//div[@id="containerInner"]//div[contains(@class, "writerInfoContents")]/div[7]//text()').re(u'\d+'))
        item['url'] = unicode(response.url)
        item['category'] = u'humor'
        item['image_urls'] = response.xpath('//div[@id="containerInner"]//div[contains(@class, "viewContent")]//img/@src').extract()

        log_msg = "Parsed: url=%(url)s content_size=%(cont_size)d image_count=%(img_cnt)d crawled_at=%(crawled_at)s"
        log_args = {
            "url": item['url'],
            'cont_size': len(item['content']),
            'img_cnt': len(item['image_urls']),
            'crawled_at': strftime("%Y-%m-%d %H:%M:%S", localtime()),
        }
        self.logger.info(log_msg, log_args)

        return item
