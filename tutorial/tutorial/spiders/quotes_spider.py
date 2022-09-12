import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://tuoitre.vn/vu-chay-quan-karaoke-o-dong-nai-chay-tang-tren-khach-dang-hat-ben-duoi-kip-thoi-thao-chay-20220911235958686.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div[@class='w980']/h1[@class='article-title']/text()").get()
        date = response.xpath("//div[@class='w980']/div[@class='date-time']/text()").get()
        content = response.xpath("//div[@class='column-first-second']/div[@class='main-content-body']/h2[@class='sapo']/text()").get()
        print("Title"+title)
        print("Date"+date)
        print("Content"+content)