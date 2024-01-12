import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from requests import session

s = session()
data = list()


class Scrape:
    def __init__(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Referer": "https://talentedge.com/browse-courses",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        self.response = requests.get(
            "https://talentedge.com/courselistingajax", headers=headers
        )

    def get_details(self):
        r = self.response.json()["template"]
        soup = bs(r, "html.parser")
        products = soup.find_all("div", "course-card")
        for i in range(len(products)):
            href = products[i].find("h3").find("a").get("href")
            spec = (
                products[i]
                .find("div", "course-specification")
                .find("ul")
                .find_all("li")
            )
            price = products[i].find("div", "course-price-div").find("span").text
            r1 = s.get(href)
            # soup1 is html extract of detail page
            soup1 = bs(r1.text, "html.parser")
            name = soup1.find("h1").text
            item = {"Name": name, "Price": price, "Specifications": spec, "href": href}
            data.append(item)
        print(data)


a = Scrape()
a.get_details()

df = pd.DataFrame(data)
df.to_excel("talent_edge.xlsx", index=False)
