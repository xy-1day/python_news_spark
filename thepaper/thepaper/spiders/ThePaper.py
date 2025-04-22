import scrapy


class ThepaperSpider(scrapy.Spider):
    name = "ThePaper"
    allowed_domains = ["www.thepaper.cn"]
    start_urls = ["https://www.thepaper.cn/"]

    def parse(self, response):
        pass
