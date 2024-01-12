import requests
from bs4 import BeautifulSoup as bs


class basemethods:
    def __init__(self):
        pass

    def find_by_div(self, soup, **attribute):
        try:
            return soup.find(
                "div",
                {"class": attribute["classname"]}
                if attribute.get("classname")
                else attribute,
            ).text
        except:
            return ""

    def find_by_anchor(self, soup, **attribute):
        try:
            return soup.find(
                "a",
                {"class": attribute["classname"]}
                if attribute.get("classname")
                else attribute,
            ).text
        except:
            return ""

    def find_by_img(self, soup, **attrribute):
        try:
            return soup.find(
                "img",
                {"class": attrribute["classname"]}
                if attrribute.get("classname")
                else attrribute,
            ).get("src")
        except:
            return ""

    def find_href(self, soup, **attribute):
        try:
            return soup.find(
                "a",
                {"class": attribute["classname"]}
                if attribute.get("classname")
                else attribute,
            ).get("href")
        except:
            return ""


class scraping(basemethods):
    def __init__(self):
        self.cookies = {
            "T": "TI166870722814800043339830051550501649583116542290926189747923014829",
            "SN": "VI181DC8A6E5044627BCC08932C63DBECA.TOK4B0C4B4154FC4C9DBBF0F2B475AD4A1D.1698319129.LO",
            "AMCV_17EB401053DAF4840A490D4C%40AdobeOrg": "-227196251%7CMCIDTS%7C19656%7CMCMID%7C05642723439259928296922416347835669158%7CMCAID%7CNONE%7CMCOPTOUT-1698236389s%7CNONE%7CMCAAMLH-1698833989%7C12%7CMCAAMB-1698833989%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI",
            "_pxvid": "dc1e2a88-669f-11ed-a7d1-31779629e268",
            "S": "d1t18DBQ6TH5eOW0uKT9wUz8/HkHbEkToOPawqdFZrFjS6qozgt/lFB4gTImZA65MU1HMp5AuxDrwRWlgqLXJPj9z3w==",
            "K-ACTION": "null",
            "__pxvid": "f68ff696-9d2c-11ed-9998-0242ac120003",
            "at": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE2OTk1OTc5NzcsImlhdCI6MTY5Nzg2OTk3NywiaXNzIjoia2V2bGFyIiwianRpIjoiOWMyOGRjYmUtMzJjMy00MzZkLTk2YjUtZjUyMmY1ZGQ1Yjc1IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjY4NzA3MjI4MTQ4MDAwNDMzMzk4MzAwNTE1NTA1MDE2NDk1ODMxMTY1NDIyOTA5MjYxODk3NDc5MjMwMTQ4MjkiLCJrZXZJZCI6IlZJMTgxREM4QTZFNTA0NDYyN0JDQzA4OTMyQzYzREJFQ0EiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.v9LyjImspfJteSIJ0sH8PTMeZApRVm8E38S0HOqAJ1s",
            "vh": "707",
            "vw": "2560",
            "dpr": "0.75",
            "fonts-loaded": "en_loaded",
            "AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg": "1",
            "pxcts": "539e32d0-6a60-11ee-a959-5fdcd60d43bf",
            "s_sq": "flipkart-prd%3D%2526pid%253DHomePage%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fbig-dussehra-sale-2023-store%25253Ffm%25253Dneo%2525252Fmerchandising%252526iid%25253DM_274c3510-ac19-4eb%2526ot%253DA",
            "_px3": "3ef21a26e8f8ac0112e421659e3809596a2ad57d3ab908b8f4193fc5ffffe4bb:PRu/ED0g7YPTteD3WranFCRAAjYMt5Bg41+djMd4bvdu1zdgEvRaiiVjCWEAbJWAqjEkQ3COQyiwTYVb+odFuw==:1000:lb6kI03rwk2uAZPv1bRg041/KOtRXQrYlgjQznBdwHhmwoR72tRJBeJ6lFNk3VEdMYzII7p43+ppuXpq0OqHy0lCWA7MloPMdcWdc95oitSlRKNeHh0qwGcxDIGV8uulXKtmf/oyni5tz5Eb2ajMZJ+jjsc3vZmAcotP+NwSAQ6DHyBor+a4AmrE50YJLt3yRJDhaS7jf3dIqjslV3LEh4JwkB0M5zj/mDYq9rUyfVI=",
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "keep-alive",
        }

    def get_product(self):
        response = requests.get(
            "https://www.flipkart.com/beauty-and-grooming/fragrances/pr?sid=g9b,0yh&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&otracker=clp_creative_card_1_6.creativeCard.CREATIVE_CARD_big-dussehra-sale-2023-store_OM0OG7W5MV72&fm=neo%2Fmerchandising&iid=M_d812a489-ad4f-444e-895d-b46d74211736_6.OM0OG7W5MV72&ppt=hp&ppn=homepage&ssid=ar0fyvgf0mlnypds1698229257411",
            cookies=self.cookies,
            headers=self.headers,
        )

        soup = bs(response.text, "html.parser")
        return soup.find_all("div", "_4ddWXP")

    def get_pro_details(self, soup_product):
        name = self.find_by_anchor(soup_product, classname="s1Q9rs")
        price = self.find_by_div(soup_product, classname="_30jeq3")
        img = self.find_by_img(soup_product, classname="_396cs4")
        rating = self.find_by_div(soup_product, classname="_3LWZlK")
        quantity = self.find_by_div(soup_product, classname="_3Djpdu")
        href = "https://www.flipkart.com{}".format(
            self.find_href(soup_product, classname="s1Q9rs")
        )
        print(name, "\n", price, "\n", img, "\n", rating, "\n", quantity, "\n", href)


a = scraping()
data = a.get_product()
a.get_pro_details(data[0])

# for i in range(len(data)):
# a.get_pro_details(data[i])
