import requests
import json
import pandas as pd


class PropertyCrawler:
    def __init__(self):
        self.skip = 0
        self.limit = 10
        self.url = "https://superadmin.homes247.in/backend/search/mumbai"
        self.base_url = "https://superadmin.homes247.in/backendoptimized"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-GB,en;q=0.5",
            "Origin": "https://www.homes247.in",
            "Connection": "keep-alive",
            "Referer": "https://www.homes247.in/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }
        self.params = {
            "limit": "",
            "limitrows": "",
            "proptypeid": "",
            "bedroom": "",
            "minprice": "",
            "maxprice": "",
            "possission": "",
            "locality": "",
            "statusid": "",
        }

    def make_page_link(self, details):
        try:
            return "https://www.homes247.in/property/{}/{}/{}-{}".format(
                details.get("city_name").lower().replace(" ", "-"),
                details.get("locality_name").lower().replace(" ", "-"),
                details.get("propertyName").lower().replace(" ", "-"),
                details.get("property_info_IDPK").lower().replace(" ", "-"),
            )
        except:
            return None

    def get_properties(self):
        properties = []
        a = 0
        while a < 301:
            # while True:
            self.params["limit"] = self.skip
            self.params["limitrows"] = self.limit

            response = requests.get(
                self.url, params=self.params, headers=self.headers
            ).json()

            if not response.get("deatils") or len(response.get("deatils")) <= 0:
                break

            for property in response.get("deatils"):
                property_id = property["property_info_IDPK"]

                details = (
                    requests.get(
                        "{}/get_propertyByIdnew?propId={}".format(
                            self.base_url, property_id
                        ),
                        headers=self.headers,
                    )
                    .json()
                    .get("details")[0]
                )
                amenties = (
                    requests.get(
                        "{}/get_amen_appr_ban_byid?propId={}".format(
                            self.base_url, property_id
                        ),
                        headers=self.headers,
                    )
                    .json()
                    .get("details")[0]
                )
                builder = (
                    requests.get(
                        "{}/get_propertyid_descriptions?propId={}".format(
                            self.base_url, property_id
                        ),
                        headers=self.headers,
                    )
                    .json()
                    .get("descriptions")[0]
                )

                extracted_properties = {
                    "Page Link": self.make_page_link(details),
                    "Last updated": details.get("lastupdated"),
                    "Project Name": details.get("propertyName"),
                    "By": builder["BuilderName"],
                    "Status": details.get("Status"),
                    "Locality": details.get("locality_name"),
                    "Property Type": details.get("propertyType"),
                    "Configuration": details.get("bhk"),
                    "Space Type": details.get("dimension"),
                    "Space": "{} - {} sq.ft".format(
                        details.get("area_min"), details.get("area_max")
                    ),
                    "Min Price": details.get("price_min"),
                    "Max Price": details.get("price_max"),
                    "Total Area": details.get("area_max"),
                    "Total Units": details.get("total_apartments"),
                    "Possession Date": details.get("PossessionDate"),
                    "PROJECT RERA ID": details.get("RERA_ID"),
                    "About Project": details.get("short_description"),
                    "Amenities": ", ".join(
                        map(lambda x: x["Name"], amenties.get("Amenities_Details"))
                    ),
                    "Builder Id": builder.get("BuilderId"),
                    "Builder Name": details.get("BuilderName"),
                    "Established In": details.get("publisheddate"),
                    "Total Projects": builder.get("Builder_details")[0]["totalprojects"]
                    if len(builder.get("Builder_details"))
                    else None,
                    "About Builder": builder.get("Builder_details")[0]["builderdesc"][
                        :100
                    ]
                    if len(builder.get("Builder_details"))
                    else None,
                    "Project Location": None
                    or "https://www.google.com/maps?ll=19.272362,73.086136&z=12&t=m&hl=en&gl=US&mapclient=embed&q=19%C2%B016%2720.5%22N+73%C2%B005%2710.1%22E+19.272362,+73.086136@19.272362,73.0861358",
                    "Project Address": property["address"],
                }

                properties.append(extracted_properties)
                print("Crawled Property : ", property_id)

                a += 1
            self.skip += self.limit

        return properties

    def save_to_excel(self, properties, filename="properties.xlsx"):
        df = pd.DataFrame(properties)
        df.to_excel(filename, index=False)
        print(f"Properties saved to {filename}")


crawler = PropertyCrawler()
properties = crawler.get_properties()
crawler.save_to_excel(properties)
