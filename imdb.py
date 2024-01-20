import requests
from bs4 import BeautifulSoup as bs
from requests import session
from prac import Basemethods
import pandas as pd

data = list()

s = session()
s.headers[
    "user-agent"
] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"


class Scraper(Basemethods):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.imdb.com/event/ev0000003/2023/1/?ref_=fea_eds_top-1_2",
            "Alt-Used": "www.imdb.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        self.params = {
            "ref_": "nv_mv_mpm",
        }

    def get_details(self):
        response = requests.get(
            "https://www.imdb.com/chart/moviemeter/",
            params=self.params,
            headers=self.headers,
        )
        soup = bs(response.text, "html.parser")
        product = soup.find_all("a", "ipc-title-link-wrapper")
        for i in range(len(product)):
            href = "https://www.imdb.com{}".format(product[i].get("href"))
            r = s.get(href)
            soup1 = bs(r.text, "html.parser")
            name = self.find_by_span(soup1, classname="hero__primary-text")
            rating = self.find_by_div(soup1, classname="sc-bde20123-2 cdQqzc")
            desc = self.find_by_span(soup1, classname="sc-466bb6c-2 chnFO")
            dire = self.find_by_li(soup1, classname="ipc-metadata-list__item")
            d = dict()
            d["Name"] = name
            d["Rating"] = rating
            d["Description"] = desc
            d["Directors"] = dire
            data.append(d)
        print(data)


a = Scraper()
a.get_details()

df = pd.DataFrame(data)
df.to_excel("IMBD.xlsx", index=False)
