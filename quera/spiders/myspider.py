import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["X"]
    start_urls = ["https://www.quera.es/es/anillo-compromiso-pedida"]

    def parse(self, response):
        hrefs=response.xpath('//div[@class="product-item-info"]/a/@href').getall()
        for href in hrefs:
            yield scrapy.Request(href, callback=self.parse_product)
    def parse_product(self, response):
        data={}
        url=response.url
        title = response.xpath('//h1[@itemprop="name"]/text()').get()
        sku = response.xpath('//h2[@itemprop="sku"]/text()').get()
        description = response.xpath('//div[@class="product-description-copy"]/text()').get()
        src = response.xpath('//img[@class="img-fluid"]/@src').get()
        data['Image_url'] = src
        data['title'] = title
        data['ref'] = sku
        data['description'] = description
        data['url']=url
        yield data