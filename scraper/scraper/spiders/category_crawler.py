import scrapy

from ..items import CategoryScraperItem


class CategorySpider(scrapy.Spider):
    name = 'category'

    start_urls = ['http://www.sephora.com']

    def parse(self, response):
        for category in response.css('a.css-hzvn5z'):
            name = category.css('a::text').extract()[0]
            url = category.css('a::attr(href)').extract()[0]
        
            categories = CategoryScraperItem()

            categories['name'] = name
            categories['url'] = url

            yield categories

            next_page = 'http://www.sephora.com' + url
            yield response.follow(next_page, callback=self.parse)

            
