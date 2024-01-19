import requests 
import json


class Scraper():

    def __init__(self):
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://www.jiomart.com/',
            'x-algolia-api-key': 'aace3f18430a49e185d2c1111602e4b1',
            'x-algolia-application-id': '3YP0HP3WSH',
            'Origin': 'https://www.jiomart.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        self.data = '{"requests":[{"indexName":"prod_mart_fashion_products_popularity","params":"attributesToHighlight=%5B%5D&attributesToRetrieve=%5B%22*%22%2C%22-algolia_facet%22%2C%22-alt_class_keywords%22%2C%22-available_stores%22%2C%22-avg_discount%22%2C%22-avg_discount_pct%22%2C%22-avg_discount_rate%22%2C%22-avg_mrp%22%2C%22-avg_selling_price%22%2C%22-search_keywords%22%5D&clickAnalytics=true&enableRules=true&facets=%5B%22avg_discount_pct%22%2C%22avg_selling_price%22%2C%22brand%22%2C%22category_level.level2%22%2C%22category_level.level4%22%2C%22colour%22%2C%22distress%22%2C%22dresslength%22%2C%22fabrictype%22%2C%22fit%22%2C%22mood%22%2C%22neckline%22%2C%22pattern%22%2C%22productgroups%22%2C%22size%22%2C%22sizegroup%22%2C%22skirtlength%22%2C%22sleeve%22%2C%22sport%22%2C%22style%22%2C%22waistrise%22%2C%22washcare%22%5D&filters=category_ids%3A534%20AND%20availability_status%3AA%20%20AND%20(mart_availability%3AJIO%20OR%20mart_availability%3AJIO_INSTA%20OR%20mart_availability%3AJIO_WA%20OR%20mart_availability%3AJIO_INSTA_WA)%20AND%20(buybox_mrp.PANINDIAFASHION.available%3Atrue)%20AND%20(available_stores%3APANINDIAFASHION)%20AND%20((inventory_stores%3AALL%20OR%20inventory_stores%3Afashion_zone%20OR%20inventory_stores%3AS535%20OR%20inventory_stores%3ASLG2%20OR%20inventory_stores%3ASXJJ%20OR%20inventory_stores%3AR741%20OR%20inventory_stores%3ASURR%20OR%20inventory_stores%3AR300%20OR%20inventory_stores%3ASAFY%20OR%20inventory_stores%3ASLI1%20OR%20inventory_stores%3AV050%20OR%20inventory_stores%3ASH50%20OR%20inventory_stores%3AY524%20OR%20inventory_stores%3AR351%20OR%20inventory_stores%3ASJ14%20OR%20inventory_stores%3AV012%20OR%20inventory_stores%3ASL9F%20OR%20inventory_stores%3AR975%20OR%20inventory_stores%3AS402%20OR%20inventory_stores%3AS223%20OR%20inventory_stores%3Ageneral_zone%20OR%20inventory_stores%3AV017%20OR%20inventory_stores%3ASL7L%20OR%20inventory_stores%3ASB41%20OR%20inventory_stores%3ASQ9C%20OR%20inventory_stores%3ASLTP%20OR%20inventory_stores%3ASANS%20OR%20inventory_stores%3ASL7Q%20OR%20inventory_stores%3ASG84%20OR%20inventory_stores%3ASANQ%20OR%20inventory_stores%3ASE87%20OR%20inventory_stores%3ASH62%20OR%20inventory_stores%3ASL7O%20OR%20inventory_stores%3ASH09%20OR%20inventory_stores%3ASK3Y%20OR%20inventory_stores%3AV027%20OR%20inventory_stores%3AS352%20OR%20inventory_stores_3p%3AALL%20OR%20inventory_stores_3p%3Afashion_zone%20OR%20inventory_stores_3p%3AS535%20OR%20inventory_stores_3p%3ASLG2%20OR%20inventory_stores_3p%3ASXJJ%20OR%20inventory_stores_3p%3AR741%20OR%20inventory_stores_3p%3ASURR%20OR%20inventory_stores_3p%3AR300%20OR%20inventory_stores_3p%3ASAFY%20OR%20inventory_stores_3p%3ASLI1%20OR%20inventory_stores_3p%3AV050%20OR%20inventory_stores_3p%3ASH50%20OR%20inventory_stores_3p%3AY524%20OR%20inventory_stores_3p%3AR351%20OR%20inventory_stores_3p%3ASJ14%20OR%20inventory_stores_3p%3AV012%20OR%20inventory_stores_3p%3ASL9F%20OR%20inventory_stores_3p%3AR975%20OR%20inventory_stores_3p%3AS402%20OR%20inventory_stores_3p%3AS223%20OR%20inventory_stores_3p%3Ageneral_zone%20OR%20inventory_stores_3p%3AV017%20OR%20inventory_stores_3p%3ASL7L%20OR%20inventory_stores_3p%3ASB41%20OR%20inventory_stores_3p%3ASQ9C%20OR%20inventory_stores_3p%3ASLTP%20OR%20inventory_stores_3p%3ASANS%20OR%20inventory_stores_3p%3ASL7Q%20OR%20inventory_stores_3p%3ASG84%20OR%20inventory_stores_3p%3ASANQ%20OR%20inventory_stores_3p%3ASE87%20OR%20inventory_stores_3p%3ASH62%20OR%20inventory_stores_3p%3ASL7O%20OR%20inventory_stores_3p%3ASH09%20OR%20inventory_stores_3p%3ASK3Y%20OR%20inventory_stores_3p%3AV027%20OR%20inventory_stores_3p%3AS352))&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=12&maxValuesPerFacet=50&page=__PAGE__&query=&ruleContexts=%5B%22PLP%22%5D&tagFilters="}]}'
        
    def get_details(self):
        start = 0
        while start < 84:
            response = requests.post(
                    'https://3yp0hp3wsh-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%3B%20instantsearch.js%20(4.59.0)%3B%20JS%20Helper%20(3.15.0)',
                headers=self.headers,
                data=self.data.replace('__PAGE__',str(start)),
            )
            start += 1
            prods = response.json()["results"][0]["hits"][0]
            prod_code = prods["product_code"]
            name = prods["display_name"]
            brand = prods["brand"]
            href = "https://www.jiomart.com{}".format(prods["url_path"])
            manf_name = prods["manufacturer_name"]
            price = prods["store_wise_mrp"]["PANINDIAFASHION"]["price"]
            print(price)
            


a = Scraper()
a.get_details()