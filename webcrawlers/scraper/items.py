# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CategoryScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(serialize=str)
    url = scrapy.Field()
    

class ProductScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field(serialize=int)
