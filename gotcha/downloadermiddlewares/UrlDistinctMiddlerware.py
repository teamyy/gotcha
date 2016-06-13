import time
from scrapy.exceptions import IgnoreRequest
from urlparse import urlparse,parse_qs

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
            oldest_key = min(self.cache.keys(), key=lambda key:self.cache[key])
            self.cache.pop(oldest_key)

class UrlDistinctMiddlerware(object):
    def __init__(self, settings):
        self.url_cache_capacity = settings.getint('URL_CACHE_CAPACITY', 400)
        self.url_cache_retention = settings.getint('URL_CACHE_RETENTION', 3600) # sec

    url_cache = UrlCache()
    def process_request(self, request, spider):
        params = parse_qs(urlparse(request.url).query)
        if hasattr(spider, 'identity_params') and isinstance(spider.identity_params, list):
            query_string = u'&'.join(
                [u'%s=%s' % (key, value) for key, value in self.filter_params(params, spider.identity_params).items()])
            request.identity_url = request.url.split('?')[0] + '?' + query_string

        if self.url_cache.has_key(request.identity_url):
            raise IgnoreRequest()
        self.url_cache.set(request.identity_url)

        return None

    def process_response(self, request, response, spider):
        if hasattr(request, 'identity_url'):
            response.url = request.identity_url

        return response

    def filter_params(self, params, identity_params):
        filtered_params = {}
        for param_key in identity_params:
            if not params.has_key(param_key):
                raise IgnoreRequest("The article was dropped becuase identity parameter is not exist")
            filtered_params[param_key] = params[param_key][-1]
        return filtered_params