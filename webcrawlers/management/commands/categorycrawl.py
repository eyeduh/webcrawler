from scraper.scraper.spiders.product_crawler import ProductsSpider
from scraper.scraper.spiders.brand_crawler import BrandsSpider
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sys
sys.path.append('/Users/ida/Desktop/myproject/scraper/scraper/spiders')
from scraper.scraper.spiders import category_crawler

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(category_crawler.CategorySpider)
        process.start()