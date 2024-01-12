import json
import requests
import pandas as pd


data = list()


class Scrap:
    def __init__(self):
        self.cookies = {
            "bcookie": "0416a8de-ccf4-4958-bb62-86c31e9028a4",
            "tm_stmp": "1699076709770",
            "AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg": "1075005958%7CMCIDTS%7C19678%7CMCMID%7C04986412422990650492113556232323564166%7CMCAAMLH-1700719931%7C12%7CMCAAMB-1700719931%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1700122331s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1",
            "PHPSESSID": "bb454047f4a82d0801db30ce739f7cb8",
            "cf_clearance": "OIpsTUKx0gqV7f96Y4eErqUFGTRToHLZfVSKzs51qnc-1700115131-0-1-b7b5312a.ebd3332c.e0b46eca-0.2.1700115131",
            "NYK_PCOUNTER": "2",
            "NYK_ECOUNTER": "71",
            "_gcl_au": "1.1.411319575.1699076711",
            "s_nr": "1700115132174-Repeat",
            "_ga_DZ4MXZBLKH": "GS1.1.1700115130.6.1.1700115133.57.0.0",
            "_ga": "GA1.1.584028591.1699076711",
            "WZRK_G": "38e58550053e42a8bc54a9b6fbc759c1",
            "__stp": "eyJ2aXNpdCI6InJldHVybmluZyIsInV1aWQiOiIzOTFmYzdlMy01MzliLTQ0MDItYjkxZC1iYzIxNDMyNjBiYjgiLCJjayI6Ik5BIn0=",
            "unbxd.netcoreId": "IjIwZWYwZjBjOGQwZWVhOTg3NzI0MTJjZWE5YjNiOTI2MTJlM2U1M2NiNWU1OTE1MmI1NzAzMTY1ZjU2ZThhNTMi",
            "__stat": "IkJMT0NLIg==",
            "_clck": "7cjerd|2|fgr|0|1403",
            "EXP_price-sticky-actioncontainer": "price-sticky-actioncontainer",
            "EXP_SSR_CACHE": "024035784acfcec9ebd769d69bc3046e",
            "_cfuvid": "ZuC7gIFkBYOkuFznu1LGemnq0TspfMI1V2DNaNLnSw0-1700113861502-0-604800000",
            "AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg": "1",
            "s_cc": "true",
            "__stdf": "MA==",
            "s_sq": "%5B%5BB%5D%5D",
            "NYK_VISIT": "0416a8de-ccf4-4958-bb62-86c31e9028a4~1700113963556",
            "__cf_bm": "CKeRJbWWqoQhGjkrEkCnHViSEiwAQ5AvRDle7_PnH1s-1700115130-0-AZ0gNcF6kl6UtW6HDXK+MZqhtvsym1MunbMBaID/h3kV71w5tR0ms7D+t87BzEDyT+yXu1uKp9xWp93dwA/YKLk=",
            "PCI": "0",
            "F_C_R_D": "1",
            "WZRK_S_WRK-4W9-R55Z": "%7B%22s%22%3A1700115131%2C%22t%22%3A1700115131%7D",
            "__sts": "eyJzaWQiOjE3MDAxMTUxMzIzMTYsInR4IjoxNzAwMTE1MTMyMzE2LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5ueWthYWZhc2hpb24uY29tJTJGbWVuJTJGd2F0Y2hlcyUyRmMlMkY2ODc1JTNGdHJhbnNhY3Rpb25faWQlM0QwZGYwMjMyOTk5ZjA3OWEzZmY3YTM4YWIzYzVkMDFhYSUyNmludGNtcCUzRG55a2FhJTNBb3RoZXIlM0FuZi1tZW4tZHdlYiUzQWRlZmF1bHQlM0Fvbi10aGUtY2xvY2stdGlsZSUzQVNMSURJTkdfV0lER0VUX1YyJTNBMTIlM0FzaG9wLWFsbC1jbG9jayUzQS0xJTNBMGRmMDIzMjk5OWYwNzlhM2ZmN2EzOGFiM2M1ZDAxYWElMjZwJTNEMyIsInBldCI6MTcwMDExNTEzMjMxNiwic2V0IjoxNzAwMTE1MTMyMzE2fQ==",
            "__stgeo": "IjAi",
            "__stbpnenable": "MQ==",
            "s_plt": "3.09",
            "s_pltp": "nds%3Amen%3Awatches",
            "_clsk": "s8j0pr|1700115134393|1|1|z.clarity.ms/collect",
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.nykaafashion.com/men/watches/c/6875?transaction_id=0df0232999f079a3ff7a38ab3c5d01aa&intcmp=nykaa%3Aother%3Anf-men-dweb%3Adefault%3Aon-the-clock-tile%3ASLIDING_WIDGET_V2%3A12%3Ashop-all-clock%3A-1%3A0df0232999f079a3ff7a38ab3c5d01aa&p=4",
            "x-csrf-token": "kwkdT302zzLypQEV",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "keep-alive",
        }

        self.params = {
            "PageSize": "48",
            "filter_format": "v2",
            "apiVersion": "5",
            "currency": "INR",
            "country_code": "IN",
            "deviceType": "WEBSITE",
            "sort": "popularity",
            "categoryId": "6875",
            "currentPage": 0,
        }

    def get_details(self):
        currentPage = 0
        while currentPage < 6:
            self.params["currentPage"] = currentPage
            response = requests.get(
                "https://www.nykaafashion.com/rest/appapi/V2/categories/products",
                params=self.params,
                cookies=self.cookies,
                headers=self.headers,
            )

            for i in range(len(response.json()["response"]["products"])):
                name = response.json()["response"]["products"][i].get("subTitle")
                img = response.json()["response"]["products"][i].get("imageUrl")
                # keys = response.json()["response"]["products"][i].keys()
                brand = response.json()["response"]["products"][i].get("title")
                price = response.json()["response"]["products"][i].get(
                    "discountedPrice"
                )
                p_data = {
                    "Name": name,
                    "Image": img,
                    "Brand": brand,
                    "Price": price,
                }
                data.append(p_data)

            currentPage += 1
        print(data)


d = Scrap()

d.get_details()

df = pd.DataFrame(data)
df.to_excel("nykaa.xlsx", index=False)
