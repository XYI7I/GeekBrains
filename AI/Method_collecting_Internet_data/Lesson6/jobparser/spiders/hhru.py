import scrapy
import pymongo
from scrapy.http import HtmlResponse
from scraping.jobparser.items import JobparserItem
from scraping.jobparser.selectors import ITEM_SELECTORS, NAVIGATION_SELECTORS


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = [
        "https://omsk.hh.ru/search/vacancy"
        "?area=&fromSearchLine=true&st=searchVacancy&text=python"
    ]

    def parse(self, response: HtmlResponse):
        item_urls = response.xpath(NAVIGATION_SELECTORS["parse_item"]).getall()
        for link in item_urls:
            yield response.follow(link, callback=self.parse_item)

        next_page = response.xpath(NAVIGATION_SELECTORS['parse']).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response: HtmlResponse):
        item = JobparserItem()
        for key, xpath in ITEM_SELECTORS.items():
            item[key] = response.xpath(xpath)

        item["title"] = item["title"].get()
        item["salary"] = item["salary"].getall()
        item["url"] = response.url

        yield item