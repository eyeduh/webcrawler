import scrapy

class ProductsSpider(scrapy.Spider):
    name = 'products'

    start_urls = ['http://www.sephora.com/brands-list']

    def parse(self, response):
        for brand in response.xpath('//a[@data-at="brand_link"]'):
            yield {
                'brand' : brand.css('a::text').get(),
                'brand url' : 'http://www.sephora.com' + brand.xpath('//a/@href').get(),
                'new' : brand.xpath('//span[@data-comp="Flag"]/text()').get(default='No'),
            }


            brand_urls = response.xpath('//a[@data-at="brand_link"]/@href')
            yield from response.follow_all(brand_urls, callback=self.parse_products)


    
    def parse_products(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).get(default='').strip()
            
        yield {
            'name' : extract_with_xpath('//span[@data-at="sku_item_name"]/text()'),
            'brand' : extract_with_xpath('//span[@data-at="sku_item_brand"]/text()'),
            'url' : extract_with_xpath('//a[@data-comp="ProductItem "]/@href'),
            'img' : extract_with_xpath(('//img/@src')),
            'price' : extract_with_xpath('//span[@data-at="sku_item_price_list"]/text()'),
            # 'Product Rating' : extract_with_xpath('//div[@data-comp="StarRating"]/@aria-label'),
                }
