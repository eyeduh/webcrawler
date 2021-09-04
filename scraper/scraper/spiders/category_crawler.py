from webcrawlers.models import Category
import scrapy

from ..items import CategoryScraperItem


class CategorySpider(scrapy.Spider):
    name = 'category'

    start_urls = ['http://www.sephora.com']

    def parse(self, response):
        for category in response.css('a.css-hzvn5z'):
            name = category.css('a::text').extract()[0]
            url = 'http://www.sephora.com' + category.css('a::attr(href)').extract()[0]
        
            categories = CategoryScraperItem()

            categories['name'] = name
            categories['url'] = url

            category_objects = Category.objects.create(**categories)

            yield categories

            next_page = url
            yield response.follow(next_page, callback=self.parse)
        

            
