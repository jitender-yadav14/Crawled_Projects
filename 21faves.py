import json
import requests
from requests import session
import pandas as pd


data = list()


class scrapper:
    def __init__(self):
        self.cookies = {
            "client_id": "1701148628799119",
            "_c_id": "1701148628799208753",
            "page_render_time": "0",
            "page_time": "1",
            "store_locale": "en-US",
            "gate_time": "27",
            "__cf_bm": "9rhCoArhTRrd1P7rvjJ5jUa34QeNiF0ToAO_N4dPpNc-1701148628-0-AfJYItUAofxNtO6WiPhPqh/b37omK1n3mbdn9rtxQpYqBihzj+UFtvOQSV1QiVwqlFgAyqA4IaGmSFb2NpyDPP0=",
            "session_id": "1701148607262440",
            "shoplazza_source": "%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2F%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22expire%22%3A1701753407264%7D",
            "last_land_url": "https%3A%2F%2Fwww.21faves.com%2F",
            "last_template_name": "index",
            "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2218c145bc36b864-09fab26f0f6b568-e555620-921600-18c145bc36c7ef%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218c145bc36b864-09fab26f0f6b568-e555620-921600-18c145bc36c7ef%22%7D",
            "sajssdk_2015_cross_new_user": "1",
            "_ga_3795KT0V6X": "GS1.1.1701148607.1.1.1701148936.49.0.0",
            "_ga": "GA1.2.81039884.1701148608",
            "_pin_unauth": "dWlkPVlUTXhORGN5WW1JdE1UTmhZaTAwTXpWaExUbGpZV0l0TVRsall6Y3laREF4TkdSaQ",
            "_identity_cart": "5b62844b-b55e-4851-b118-16946cc31dc8",
            "_gid": "GA1.2.1500779272.1701148610",
            "_fbp": "fb.1.1701148610754.2045724277",
            "_identity_popups_bundle": "f4f9e3c8-39bb-45b1-aba5-dc3e7284fe891701148635",
            "_identity_popups": "1ca6d601-aeed-479b-877d-ddccd9634d101701148635",
            "sw_session": "656577f4574a7",
            "_gat_gtag_UA_83020630_37": "1",
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Requested-With": "XMLHttpRequest",
            "Alt-Used": "www.21faves.com",
            "Connection": "keep-alive",
            "Referer": "https://www.21faves.com/collections/one-pieces?spm=..index.products_1.1&spm_prev=..collection_5b444d75-0aac-4449-a1b0-426528c82997.header_1.1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        self.params = {
            "page": 0,
            "sort_by": "manual",
            "limit": "48",
            "tags": "",
            "price": "",
        }

    # def detail_page(self, p_url):
    #     s = session()
    #     s.headers[
    #         "user-agent"
    #     ] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
    #     response = s.get(p_url)
    #     print(response)

    def get_details(self):
        page = 0
        while page < 20:
            self.params["page"] = page
            response = requests.get(
                "https://www.21faves.com/api/collections/047142f8-11fe-4923-a58d-17551eb1a1fe/products",
                params=self.params,
                cookies=self.cookies,
                headers=self.headers,
            )

            Products = response.json()["data"].get("products")
            if not Products:
                break

            for i in Products:
                name = i.get("title")
                price = i.get("price")
                p_url = "https://www.21faves.com{}".format(i.get("url"))

                if i.get("images"):
                    img = "https:{}".format(i.get("images")[0].get("src"))
                else:
                    img = ""
                p_data = {"Name": name, "Price": price, "href": p_url, "Image": img}
                data.append(p_data)

            page += 1
        # print(data)


a = scrapper()
d = a.get_details()


df = pd.DataFrame(data)
df.to_excel("21faves.xlsx", index=False)
