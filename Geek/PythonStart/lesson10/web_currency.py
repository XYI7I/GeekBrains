import requests
from bs4 import BeautifulSoup as bs


def convert_currency_xe(src, dst='RUB', amount=1):
    def get_digits(text):
        """Returns the digits and dots only from an input `text` as a float
        Args:
            text (str): Target text to parse
        """
        new_text = ""
        for c in text:
            if c.isdigit() or c == ".":
                new_text += c
        return float(new_text)

    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={src}&To={dst}"
    # print(url)
    content = requests.get(url).content
    soup = bs(content, "html.parser")
    exchange_rate_html = soup.find('p', attrs={'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'}).getText().split()
    exchange_rate_val = exchange_rate_html[0].split(',')
    rate_val = ''
    for el in exchange_rate_val:
        rate_val += el

    return rate_val
