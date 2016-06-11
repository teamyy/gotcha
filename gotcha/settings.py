# -*- coding: utf-8 -*-

BOT_NAME = 'gotcha'

SPIDER_MODULES = ['gotcha.spiders']

NEWSPIDER_MODULE = 'gotcha.spiders'

USER_AGENT = 'teamyy.gotcha (+https://github.com/teamyy/gotcha)'

SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}

EXTENSIONS = {
    'scrapy.extensions.corestats.CoreStats': 100,
    'scrapy.extensions.memusage.MemoryUsage': 200,
    'scrapy.extensions.closespider.CloseSpider': 300,
    'scrapy.extensions.logstats.LogStats': 400,
    'scrapy.extensions.spiderstate.SpiderState': 500,
    'scrapy.extensions.throttle.AutoThrottle': 600,
    'scrapy.extensions.debug.StackTraceDump': 700,
}

ITEM_PIPELINES = {
    'gotcha.pipelines.NecessaryFieldEmptyDropPipeline': 100,
    'gotcha.pipelines.PotsuNetAdminArticleDropPipeline': 200,
    'gotcha.pipelines.MySqlPipeline': 300,
}

CONCURRENT_ITEMS = 200

CONCURRENT_REQUESTS = 16

CONCURRENT_REQUESTS_PER_DOMAIN = 4

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ko,en;q=0.8',
}

DEPTH_LIMIT = 0

DEPTH_PRIORITY = 1

DEPTH_STATS = False

DEPTH_STATS_VERBOSE = False

DNSCACHE_ENABLED = True

DNSCACHE_SIZE = 1024

DNS_TIMEOUT = 10

DOWNLOADER_STATS = True

DOWNLOAD_TIMEOUT = 30

LOG_ENABLED = True

LOG_ENCODING = 'UTF-8'

LOG_FILE = 'logs/gotcha.log'

LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'

LOG_LEVEL = 'INFO'

LOG_STDOUT = False

MEMDEBUG_ENABLED = False

MEMUSAGE_ENABLED = True

MEMUSAGE_LIMIT_MB = 256

MEMUSAGE_WARNING_MB = 128

MEMUSAGE_NOTIFY_MAIL = None

MEMUSAGE_REPORT = False

MEMUSAGE_CHECK_INTERVAL_SECONDS = 60

REACTOR_THREADPOOL_MAXSIZE = 8

RETRY_PRIORITY_ADJUST = -1

ROBOTSTXT_OBEY = True

STATS_DUMP = True

TELNETCONSOLE_ENABLED = False

URLLENGTH_LIMIT = 240

AJAXCRAWL_ENABLED = False

AUTOTHROTTLE_DEBUG = False

AUTOTHROTTLE_ENABLED = True

AUTOTHROTTLE_START_DELAY = 1

AUTOTHROTTLE_MAX_DELAY = 30

AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

CLOSESPIDER_ERRORCOUNT = 0

CLOSESPIDER_ITEMCOUNT = 0

CLOSESPIDER_PAGECOUNT = 0

CLOSESPIDER_TIMEOUT = 180

COMPRESSION_ENABLED = True

COOKIES_DEBUG = False

COOKIES_ENABLED = True

HTTPCACHE_DBM_MODULE = 'leveldb'

HTTPCACHE_DIR = ''

HTTPCACHE_ENABLED = True

HTTPCACHE_EXPIRATION_SECS = 30

HTTPCACHE_GZIP = False

HTTPCACHE_ALWAYS_STORE = True

HTTPCACHE_IGNORE_HTTP_CODES = [400, 401, 403, 404, 406, 408, 410, 413, 415, 431, 500, 502, 503, 504]

HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS = ['no-store', 'no-cache', 'must-revalidate', 'proxy-revalidate']

HTTPCACHE_IGNORE_SCHEMES = ['file', 'ftp']

HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.RFC2616Policy'

HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.LeveldbCacheStorage'

HTTPCACHE_IGNORE_MISSING = False

METAREFRESH_ENABLED = False

REDIRECT_ENABLED = False

REFERER_ENABLED = True

RETRY_ENABLED = True

RETRY_HTTP_CODES = [408, 500, 502, 503, 504]

RETRY_TIMES = 3

MYSQL_HOST = 'localhost'

MYSQL_PORT = 3306

MYSQL_USERNAME = 'gotcha'

MYSQL_PASSWORD = 'gotchapw'

MYSQL_SCHEMA = 'gotcha'
