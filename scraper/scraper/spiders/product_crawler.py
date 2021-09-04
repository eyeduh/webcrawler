from os import name

from w3lib import url
from webcrawlers.models import Product, Brand
from scraper.scraper.spiders.brand_crawler import BrandsSpider
from urllib import parse
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .brand_crawler import BrandScraperItem


from ..items import ProductScraperItem

class ProductsSpider(CrawlSpider):
    name = 'products'

    brand = Brand

    start_urls = [Brand]

    le1 = LinkExtractor(allow='product')

    
    def parse(self, response):

        links = self.le1.extract_links(response)
      
        for link in links:
            yield scrapy.Request(link.url)
        
            for product in response.css('a.css-ix8km1'):
                
                name = product.xpath('.//span[@data-at="sku_item_name"]/text()').get()
                brand = product.xpath('.//span[@data-at="sku_item_brand"]/text()').get()
                url =  product.xpath('./@href').get()
                img = 'http://www.sephora.com' + product.xpath(('.//img/@src')).get()
                price = product.xpath('.//span[@data-at="sku_item_price_list"]/text()').get()
                # 'Product Rating' : extract_with_xpath('//div[@data-comp="StarRating"]/@aria-label')
                
                products = ProductScraperItem()

                products['name'] = name
                products['url'] = url
                products['brand'] = brand
                products['img'] = img
                products['price'] = price

                products_objects = Product.objects.create(**products)

                yield products
        
