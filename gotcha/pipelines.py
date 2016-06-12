# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from urlparse import urlparse,parse_qs

from scrapy.exceptions import DropItem
import MySQLdb

logger = logging.getLogger('gotchaLogger')


class NecessaryFieldEmptyDropPipeline(object):
    def process_item(self, item, spider):
        if not item['title']:
            raise DropItem("An article was dropped because 'title' field is empty (url: %s)" % item['url'])
        if not item['writer']:
            raise DropItem("An article was dropped because 'writer' field is empty (url: %s)" % item['url'])
        if not item['writed_at']:
            raise DropItem("An article was dropped because 'writed_at' field is empty (url: %s)" % item['url'])

        return item


class PotsuNetAdminArticleDropPipeline(object):
    def process_item(self, item, spider):
        writer = item['writer']
        domain = urlparse(item['url']).netloc

        if domain in [u"potsu.net", "potsu.net"] and writer in [u"potsu", "potsu"]:
            raise DropItem("Admin's article in potsu.net was dropped (url: %s)" % item['url'])

        return item

class UrlDistinctPipeline(object):
    def process_item(self, item, spider):
        params = parse_qs(urlparse(item['url']).query)
        if hasattr(spider,'identity_params') and isinstance(spider.identity_params, list):
            query_string = u'&'.join([ u'%s=%s' % (key, value) for key, value in self.filter_params(params, spider.identity_params).items()])
            item['url'] = item['url'].split('?')[0] + '?' + query_string
        return item

    def filter_params(self, params, identity_params):
        filtered_params = {}
        for param_key in identity_params:
            if not params.has_key(param_key):
                raise DropItem("The article was dropped becuase identity parameter is not exist")
            filtered_params[param_key] = params[param_key][0]
        return filtered_params

class MySqlPipeline(object):
    MAX_LIST_SIZE = 10
    gotcha_item_list = []

    def __init__(self, mysql_host='localhost', mysql_port=3306, username='gotcha', password='gotchapw', db_name='gotcha'):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.username = username
        self.password = password
        self.db_name = db_name

    @classmethod

    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            db_name=crawler.settings.get('MYSQL_SCHEMA')
        )

    def open_spider(self, spider):
        self.connection = MySQLdb.connect(self.mysql_host, self.username, self.password, self.db_name, self.mysql_port, charset="utf8")
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        if len(self.gotcha_item_list) > 0 :
            self.insert_mysql()
        self.connection.close()

    #  수집된 item과 각 item을 수집할 때 사용한 spider를 파라미터로 받음.
    def process_item(self, item, spider):
        self.gotcha_item_list.append((item['title'], item['content'], item['writer'], item['writed_at'], item['url'], item['category']))

        if len(self.gotcha_item_list) < self.MAX_LIST_SIZE :
            return item
        self.insert_mysql()
        return item

    def insert_mysql(self):
        query_template = u"""INSERT INTO articles (title, content, writer, writed_at, url, category)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title), content=VALUES(content), writed_at=VALUES(writed_at), url=VALUES(url), category=VALUES(category)"""
        try:
            self.cursor.executemany(query_template, self.gotcha_item_list)
            self.connection.commit()

            logger.info('Success to store %d rows', len(self.gotcha_item_list))
            del self.gotcha_item_list[:]

        except MySQLdb.Error as e:
            logger.error('Mysql Insert Fail : %d, %s', e.args[0], e.args[1])
