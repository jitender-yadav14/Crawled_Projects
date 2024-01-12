import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd

data = list()


class Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.rarrtech.com/",
            "Content-Type": "application/json",
            "Origin": "https://www.rarrtech.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        self.json_data = {
            "apiId": 214,
            "params": [
                "164",
                "0",
                "All time",
                "",
                "",
                0,
                0,
                "",
                "",
                0,
                "rarrtech",
            ],
        }

    def get_pro_det(self, job_id):
        json_data = {
            "apiId": 216,
            "params": [
                "164",
                "0",
                job_id,
                "rarrtech",
            ],
        }

        r = requests.post(
            "https://portal.atsmantra.com//userInterface/getApiConfigListParamWithoutLogin",
            headers=self.headers,
            json=json_data,
        )

        d = r.json()
        return d

    def get_details(self):
        response = requests.post(
            "https://portal.atsmantra.com//userInterface/getApiConfigListParamWithoutLogin",
            headers=self.headers,
            json=self.json_data,
        )
        product = response.json()

        for i in range(len(product)):
            job_id = product[i]["job_unique_id"]
            d1 = self.get_pro_det(job_id)
            comp_name = product[i]["company_name"]
            exp = product[i]["job_exp"]
            job_name = d1[0]["job_title"]
            CTC = d1[0]["ctc"]
            job_descrip = d1[0]["job_desc"]
            emp_type = d1[0]["employment_type"]
            skills = d1[0]["job_skills"]
            location = d1[0]["job_loc"]
            item = {
                "Post": job_name,
                "Company Name": comp_name,
                "Experience": exp,
                "CTC": CTC,
                "Employment Type": emp_type,
                "Skills": skills,
                "Location": location,
                "Job Description": job_descrip,
            }

            data.append(item)
        print(data)


a = Scraper()
d = a.get_details()


df = pd.DataFrame(data)
df.to_excel("rarr.xlsx", index=False)
