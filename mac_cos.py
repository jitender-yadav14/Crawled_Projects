import requests
from requests import session
from bs4 import BeautifulSoup as bs
import pandas as pd

s = session()

data = list()


class Scraper:
    def __init__(self):
        # def response(self):
        url = "https://www.maccosmetics.in/bestsellers"
        s.headers[
            "user-agent"
        ] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
        self.response = s.get(url)
        self.soup = bs(self.response.text, "html.parser")

    def getdetails(self):
        products = self.soup.find_all("div", "skeleton-details")
        for product in products:
            name = product.find("h2").text
            href = "https://www.maccosmetics.in{}".format(product.find("a").get("href"))
            response1 = s.get(href)
            soup1 = bs(response1.text, "html.parser")
            price = soup1.find("div", "product-full__price").text
            img = soup1.find_all("img", "js-product-image")[0].get("src")
            mfg_date = soup1.find_all("div", "product-overview--expiration-date")[
                0
            ].text
            item = {
                "Name": name,
                "Price": price,
                "MFG": mfg_date,
                "IMG": img,
                "href": href,
            }
            data.append(item)
        print(data)


a = Scraper()
a.getdetails()


df = pd.DataFrame(data)
df.to_excel("mac_cos.xlsx", index=False)
