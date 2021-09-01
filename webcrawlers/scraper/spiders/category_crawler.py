import scrapy


class CategorySpider(scrapy.Spider):
    name = 'category'

    start_urls = ['http://www.sephora.com']

    def parse(self, response):
        for category in response.css('a.css-hzvn5z'):
            yield {'name' : category.css('a::text').getall(), 
                   'url' : category.css('a::attr(href)').getall(),
                              }
        

            
