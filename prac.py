class Basemethods:
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

    def find_by_h(self, soup, **attribute):
        try:
            return soup.find(
                "h1",
                {"class": attribute["classname"]}
                if attribute.get("classname")
                else attribute,
            ).text
        except:
            return ""

    def find_by_span(self, soup, **atttribute):
        try:
            return soup.find(
                "span",
                {"class": atttribute["classname"]}
                if atttribute.get("classname")
                else atttribute,
            ).text
        except:
            return ""

    def find_by_ul(self, soup, **attribute):
        try:
            return soup.find_all(
                "ul",
                {"class": attribute["classname"]}
                if attribute.get("classname")
                else attribute,
            )
        except:
            return ""

    def find_by_li(self, soup, **attribute):
        try:
            return soup.find_all(
                "li",
                {"class": attribute["classname"]}
                if attribute.get("classname")
                else attribute,
            )[0].text
        except:
            return ""
