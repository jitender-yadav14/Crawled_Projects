from bs4 import BeautifulSoup as bs
import requests
from prac import Basemethods


class Scraper(Basemethods):
    def __init__(self):
        self.cookies = {
            "eps_sid": "60d42d6dcbff25198502e9636fbba26f56d7f723",
            "reese84": "3:x1jWlp0CI0SYtgGLneZp1Q==:AUOer6sVxcVr1qMb6YnZ5XsHvxtQ6TBCgiOc+tpFVfOJFhBu1V5q9ruNIEh8lkuhILJVehW7m0rHeryDWvoGUiNbTxfPy6630qjupy9mLGslntUEbjuN0ByYcE3uSEGkgYHoGid2Spaelv6hpVixCEQ4bZxrMTGujejt/zMgSbR42wy36m4EDZiXR8/e3hDkWFRa6HrFVEorJ6Vwiu8XsRzgDnjoPGPUSeOLzysfxtwST/bPc8AgIaEobYFBwCTlNvqmyQFJvGytPVj9XArsdrG53TfXK3p9Bc2/8CwqFDMHbRwPlwIuH7JK5IZ06/nagScZFjNpEhFJ7uvnee2YctcowPQCRk1hclyLZhtbgjGGMUK72Vgx1p599rgnlDZdxQD+NHJYhO4zYoIh+PLkWZ3apHabeYWiJ87loAGkqKlgFbv0MmyEQwMxaWqv9eAmcZ4WaxzYiQaCjvpsOmhmh+FrMrbxyn48pLoJ3rJT9dWS/h2Jt/dmC12Xy2V4mpn9WCc0KeZr9RpCh0Y/LdFNmg==:11QnoFgLYZ21OcDAG3gtFqif1Hbf3w/ysD2vDy5j7no=",
            "language": "sv-se",
            "BID": "2944f9e401cb412a9a48dffa",
            "OptanonConsent": "isGpcEnabled=0&datestamp=Wed+Nov+22+2023+12%3A02%3A15+GMT%2B0530+(India+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fd9d9c98-e5cc-4341-aa8c-b0566a41fd59&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CV2STACK42%3A0&geolocation=IN%3BDL&AwaitingReconsent=false",
            "OptanonAlertBoxClosed": "2023-11-18T06:15:50.910Z",
            "eupubconsent-v2": "CP1bOuQP1bOuQAcABBENAbEgAAAAAAAAACiQAAAAAAHggBAACQA_gEUALSAaIBGICrwFdhAF4AAQADAAJgAcAB4AGQAWABHACgAFcALYAfwBFgCXAF9ANQA1QBzgDyAHyAQMAg4BFACOAE_gKGAooBdgDOAGiAN4AegA-QCG4EXgRiAj0BIoCSwErAJlgTYBNoClwFXgK7AWFAsQCxQF1ALuAXkAwIJAvAAQAAuACgAKgAcgA8AEAAMIAZABqADwAIgATAAqgBvAD0AISAQwBEgCOAEsAJoAUoAwwBlgDZAHfAPYA-IB9gH6AQCAi4CMAEaAJSAUEAqABVwC5gGKANoAbgA4gCRAE7AKHAUeApEBTYC2AFyALvAXmGAjgABAAMAAkABwAFAARQAnACwAGEAPAA9gCEAIgARwAmABUACvAFsAXAA3wBzAHgAP4AhgBEgCLAEuAKQAVoA1IBsgHAAOMAc4A8gB-AEAAIoARgAkwBOgCigFLgK8Ar4BdgC_AGcANkAbYA3gBxwDmgHUAOyAeoA-QB-wEJAIbgReBGICOoEiASKAkuBLQEvAJsATsAoSBSIFJAKbAVfAsQCxQFogLkAXQAu4BgQDGRAEgAAIABgAEgAOAAoACKAE4AWAAwgB4AHsAQgBEACOAEwAK4AWwA3wBzAHcAP4AhgBEgCLAEuAKQAVoA1IBsgHAAOMAc4A8gB8gD8AIAARQAjABJgCdAFFAKXAV4BXwC7AF-AM4AaIA1ABtgDeAHHAOaAdkA9QB8gD9gISAQ3Ai8CMQEdwJEAkUBJcCWgJeATYAnYBQgCkgFNgKvAV3AsQCxQFogLkAXQAu4BgQDGRQB0ABIAIoAVABYAEIAJgAXAA8ACOAFIANQAcABHACiwFeAV8AuwBfgDOAG8AOaAfsBHoCRQEvAJsAVfAsQCxQFogLYAXcMANgAJABFACoALAAhABMAEcAKQAagA4ACOAFFgK8Ar4BdgC_AGcAN4Ac0A_YCPQEigJeATYAq8BYgC0QFsALuHAR4ADAATAA4ADwALgAZABYADmAHwAfgBHACaAFAAK4AWwAugBfADQAH8AQgAiwBHACXAFIALIAXwAwgBqADnAHcAPIAfMBAAEDgIOAhABEQCKAEcAJxAT4BPwCigFLAKgAVkAuwBegDOAGiAN4AccA6QB6AD5AIbAREAioBHoCRQElgJWgTEBMsCbAJtAUgApMBS8CqgKsAVeArsBYgCygFswLoAuoBdwC-gGBDoGoAC4AKAAqAByAD4AQAAugBgAGoAPAAiABMACqAFwAMQAZgA3gB6gEMARIAlgBNACjAFKAMMAZQA0QBsgDvAHtAPsA_QB_wEWARgAlIBQQCrgFiALmAXkAxQBtADcAHEAOoAi8BIgCVAE7AKHAUfApoCmwFigLYAXIAu0Bd4C8yACKABAAEgAZABYAE0AL4AaAA_gCkAFkAL4AagA5wCKAEcAJwAT6AoYCigFLAKyAWIAtIBdgDeAHNAPQAj0BIsCbAJtAUmAsQBbIC7gF5AMCIQGQAFgAUABcADEAJgAVQAuABiADeAHoARwA7wB_gEpAKCAVcAuYBigDaAHUASoApoBYoC0QFyEgFoABgAEgAOAAuABkAFgAOQAjgBNACoAF8AMgAbQA3gB4AEIAKQAWUA1ADVAHcAQAAigBHACfQFNAVAArIBaQC7AGiAN4AfIBFQCMQEdAI9ASKAlYBLUCbAJtAUmAqkBXYCxAFlALuJQGgAEAALAAoAByAGAAYgA8ACIAEwAKoAXAAxQCGAIkARwAowBsgDvAH4AVcAxQB1AEXgJEAUeAsUBbAC8ygDgABIAFwAMgAsAByAEcAJoAVAAvgBkADaAG8APAAhABFgCOAEyAKQAWQAvgBhQDUANUAc4A7oB8gH2AQAAigBHACRAE-AKGAUuArICtgFigLqAuwBogDXgG8AO2AegA_4COgEegJFASWAmKBNgE2gKQAU-ArsBYgC6AF3ALyAX0AwIpAoAAXABQAFQAOQAfACCAGAAagA8ACIAEwAKQAVQAxABmgEMARIAowBSgDKAGiANkAd8A_AD9AIsARgAlIBQQCrgFzALyAYoA2gBuAEXgJEATsAoeBTQFNgLFAWwAuQBdoC8wAAA.YAAAAAAAAAAA",
            "_gcl_au": "1.1.1777523642.1700291504",
            "LANGUAGE": "sv-se",
            "NDMA": "612",
            "ORIGIN_638441": "#{1}#",
            "SID": "42292518a2d44323bedc7719",
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

    def get_details(self):
        response = requests.get(
            "https://www.ticketmaster.se/event/music-of-the-christmas-night-2023-biljetter/638441",
            cookies=self.cookies,
            headers=self.headers,
        )
        soup = bs(response.text, "html.parser")
        pro = soup.find("div", "sc-1mnfoel-0 cMZuTE")

        for product in pro:
            name = product.find("div", "sc-1mnfoel-0 cMZuTE")
            print(name)


scraper = Scraper()
scraper.get_details()
