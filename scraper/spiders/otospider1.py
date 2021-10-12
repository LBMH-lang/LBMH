import scrapy


class Otospider1Spider(scrapy.Spider):
    name = 'otospider1'
    allowed_domains = ['oto.com.vn']
    start_urls = ['http://oto.com.vn/']

    def parse(self, response):
        pass
