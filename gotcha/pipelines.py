# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

logger = logging.getLogger('gotchaLogger')

class GotchaPipeline(object):
    def process_item(self, item, spider):
        return item

class PrintPipeline(object):
    def process_item(self, item, spider):
        print item
        return item


import MySQLdb


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
        self.gotcha_item_list.append((item['title'], item['content'], item['writer'], item['created_at'], item['url'], item['category']))

        if len(self.gotcha_item_list) < self.MAX_LIST_SIZE :
            return item
        self.insert_mysql()
        return item

    def insert_mysql(self):
        try:
            self.cursor.executemany("""INSERT INTO articles (title, content, writer, created_at, url, category)
                        VALUES (%s, %s, %s, %s, %s, %s)""", self.gotcha_item_list)
            self.connection.commit()

            logger.info('Success to store %d rows')
            del self.gotcha_item_list[:]

        except MySQLdb.Error as e:
            logger.error('Mysql Insert Fail : %d, %s', e.args[0], e.args[1])