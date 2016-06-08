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

CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_ITEMS = 400

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 5.0
AUTOTHROTTLE_DEBUG = False

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60
HTTPCACHE_DIR = ''
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.LeveldbCacheStorage'
HTTPCACHE_IGNORE_MISSING = False
HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.RFC2616Policy'
HTTPCACHE_DBM_MODULE = 'leveldb'

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'gotcha'
MYSQL_PASSWORD = 'gotchapw'
MYSQL_SCHEMA = 'gotcha'

LOG_FILE = 'logs/gotcha.log'
LOG_ENABLED = True
LOG_ENCODING = 'UTF-8'
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_STDOUT = False

MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 1024
MEMUSAGE_WARNING_MB = 0
MEMUSAGE_NOTIFY_MAIL = None
MEMUSAGE_REPORT = False
MEMUSAGE_CHECK_INTERVAL_SECONDS = 60

DEPTH_LIMIT = 0
DEPTH_PRIORITY = 1
DEPTH_STATS = True

URLLENGTH_LIMIT = 240

ROBOTSTXT_OBEY = True

REDIRECT_ENABLED = False
REDIRECT_MAX_TIMES = 0

RETRY_ENABLED = True
RETRY_TIMES = 3

