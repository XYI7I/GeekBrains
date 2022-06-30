# eBay scraper
import requests
from lxml.html import fromstring

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311&_nkw=sunglasses&_sacat=0"
headers = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

response = requests.get(url, headers=headers)
dom = fromstring(response.text)


items_xpath = '//ul[contains(@class, "-results")]//div[contains(@class, "s-item__wrapper")]'
title_xpath = './/h3[contains(@class, "_title")]/text()'
price_xpath = '//ul[contains(@class,"-results")]//div[contains(@class, "s-item__wrapper")]//span[contains(@class, "_price")]//text()'
items_info = []



for item in dom.xpath(items_xpath):
    info = {}
    info['title'] = item.xpath(title_xpath)
    info['price'] = item.xpath(price_xpath)

print()






