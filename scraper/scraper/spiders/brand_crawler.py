from os import name
from webcrawlers.models import Brand
import scrapy

from ..items import BrandScraperItem

class BrandsSpider(scrapy.Spider):
    name = 'brands'

    start_urls = ['http://www.sephora.com/brands-list']

    def parse(self, response):
        for brand in response.xpath('//a[@data-at="brand_link"]'):
            name = brand.css('a::text').get()
            url = 'http://www.sephora.com' + brand.css('a::attr(href)').extract()[0]
            new = brand.css('span.css-1yfnlr::text').get(default='Not New')

            brands = BrandScraperItem()
        
            brands['name'] = name
            brands['url'] = url
            brands['new'] = new
            
            brand_objects = Brand.objects.create(**brands)

            yield brands
            
