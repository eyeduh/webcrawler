# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from webcrawlers.models import Category, Brand, Product

class CategoryScraperItem(DjangoItem):
    django_model = Category
    name = scrapy.Field()
    url = scrapy.Field()


class BrandScraperItem(DjangoItem):
    django_model = Brand
    brand = scrapy.Field()
    url = scrapy.Field()
    new = scrapy.Field()


class ProductScraperItem(DjangoItem):
    django_model = Product
    name = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
