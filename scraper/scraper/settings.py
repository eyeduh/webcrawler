from __future__ import unicode_literals
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".settings")
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../.."))

MEDIA_ALLOW_REDIRECTS = True

BOT_NAME = 'scraper'

LOG_LEVEL = 'DEBUG'

SPIDER_MODULES = [
    'scrapy_django_dashboard.spiders',
    'scraper.scraper',
]

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

ITEM_PIPELINES = {
    'scrapy_django_dashboard.pipelines.DjangoImagesPipeline': 200,
    'scrapy_django_dashboard.pipelines.ValidationPipeline': 400,
    'scraper.scraper.pipelines.DjangoWriterPipeline': 800,
}

IMAGES_THUMBS = {
    'medium': (50, 50),
    'small': (25, 25),
}

DSCRAPER_IMAGES_STORE_FORMAT = 'ALL'
DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'ERROR'
DSCRAPER_LOG_LIMIT = 5
