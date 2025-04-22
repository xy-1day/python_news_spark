import scrapy


class SohuSpider(scrapy.Spider):
    name = "SoHu"
    allowed_domains = ["news.sohu.com"]
    start_urls = ["https://news.sohu.com/"]

    def parse(self, response):
        pass
