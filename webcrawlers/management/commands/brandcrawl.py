from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sys
sys.path.append('/Users/ida/Desktop/myproject/scraper/scraper/spiders')
from scraper.scraper.spiders import brand_crawler

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(brand_crawler.BrandsSpider)
        process.start()