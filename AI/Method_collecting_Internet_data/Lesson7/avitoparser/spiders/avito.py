import scrapy
from scrapy.http import HtmlResponse
from avitoparser.items import AvitoparserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']

    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://www.avito.ru/rossiya?q={query}']

    def parse(self, response: HtmlResponse):
       ads_links = response.xpath("//a[@data-marker='item-title']")
       for link in ads_links:
           yield response.follow(link, callback=self.parse_ads)


    def parse_ads(self, response:HtmlResponse):
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('name', '//h1/span/text()')
        loader.add_xpath('price', "//span[@itemprop='price']/text()")
        loader.add_xpath('photos', "//div[contains(@class,'gallery-img-frame')]/@data-url")
        # loader.add_css()
        loader.add_value('url', response.url)
        yield loader.load_item()

        # name = response.xpath("//h1/span/text()").get()
        # price = response.xpath("//span[@itemprop='price']/text()").get()
        # photos = response.xpath("//div[contains(@class,'gallery-img-frame')]/@data-url").getall()
        # yield AvitoparserItem(name=name, price=price, photos=photos)



