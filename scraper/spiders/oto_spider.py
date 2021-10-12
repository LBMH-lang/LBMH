import scrapy


class OtoSpiderSpider(scrapy.Spider):
    name = 'oto_spider'
    allowed_domains = ['oto.com.vn']
    start_urls = ['http://oto.com.vn/']

    def parse(self, response):
        pass
