# -*- coding: utf8 -*-

import time
import logging
from urlparse import urlparse, parse_qs

from scrapy.exceptions import IgnoreRequest

logger = logging.getLogger('UrlDistinctMiddlerwareLogger')


class UrlCache:
    def __init__(self, capacity, retention):
        self.capacity = capacity
        self.retention = retention
        self.cache = {}

    def has_key(self, key):
        now = int(time.time())
        return self.cache.has_key(key) and now - self.cache[key] > self.retention

    def set(self, key):
        if len(self.cache) >= self.capacity:
            self.swipe()
        self.cache[key] = int(time.time())

    def swipe(self):
        now = int(time.time())
        del_count = 0
        for key, timestamp in self.cache:
            if now - timestamp > self.retention:
                del self.cache[key]
                del_count += 1

        if del_count == 0:
            oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k])
            self.cache.pop(oldest_key)


class UrlDistinctMiddlerware(object):
    def __init__(self, settings):
        self.url_cache_capacity = settings.getint('URL_CACHE_CAPACITY', 400)
        self.url_cache_retention = settings.getint('URL_CACHE_RETENTION', 3600)
        self.url_cache = UrlCache(self.url_cache_capacity, self.url_cache_retention)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        params = parse_qs(urlparse(request.url).query)
        identity_params = spider.identity_params
        refined_params = self.refine_params(params, identity_params)
        refined_url = request.url.split('?')[0] + '?' + refined_params

        if self.url_cache.has_key(refined_url):
                logger.debug("Cached hit! : %s" % refined_url)
                raise IgnoreRequest()
        self.url_cache.set(refined_url)

        return None

    def process_response(self, request, response, spider):
        params = parse_qs(urlparse(request.url).query)
        identity_params = spider.identity_params
        refined_params = self.refine_params(params, identity_params)
        refined_url = request.url.split('?')[0] + '?' + refined_params

        response = response.replace(url=str(refined_url))

        logger.debug("Replaced response url : %s" % response.url)

        return response

    def refine_params(self, params, identity_params):
        filtered_params = {key: values[-1] for key, values in params.items() if key in identity_params}
        return u'&'.join([u'%s=%s' % (key, value) for key, value in filtered_params.items()])

