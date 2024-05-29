# Scrapy settings for realty_s project

BOT_NAME = 'realty_s'

SPIDER_MODULES = ['realty_s.spiders']
NEWSPIDER_MODULE = 'realty_s.spiders'

# User-Agent string
USER_AGENT = 'realty_s (+http://xn--80az8a.xn--d1aqf.xn--p1ai)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Splash settings
SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Output settings
FEED_FORMAT = 'json'
FEED_URI = 'output.json'
FEED_EXPORT_ENCODING = 'utf-8'
