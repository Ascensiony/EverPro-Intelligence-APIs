from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from six.moves.urllib.parse import urlencode, quote
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup

import re
import json
import time


tokenizer = RegexpTokenizer(r"[a-zA-Z\s\d]")

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("start-maximized")

zone_to_url = {
    "US": "https://www.amazon.com/",
    "UK": "https://www.amazon.co.uk/",
    "IN": "https://www.amazon.co.in/",
}


def _identity_seller1(soup: BeautifulSoup):

    search_area = soup.find("div", {"id": "mbc-sold-by-1"})

    if search_area is None:
        raise Exception("ID1 not found")

    try:
        search_area = search_area.find("span", {"class": "mbcMerchantName"})
        if search_area is not None:
            return search_area.text.strip()

    except Exception as e:
        print(e)
        print("Could not retrieve the seller name open the website and debug1")
        return ""

    raise Exception("Wow1")


def _identity_seller2(soup: BeautifulSoup):

    search_area = soup.find("a", {"id": "bylineInfo"})

    if search_area is None:
        raise Exception("ID2 not found")

    try:
        if search_area is not None:
            return search_area.text.strip()  # [10:-6].strip()
    except Exception as e:
        print(e)
        print("Could not retrieve the seller name open the website and debug2")
        return ""

    raise Exception("Wow2")


def _identity_seller3(soup: BeautifulSoup):

    search_area = soup.find("div", {"id": "merchant-info"})

    if search_area is None:
        raise Exception("ID3 not found")

    try:
        search_area = soup.find("a", {"id": "sellerProfileTriggerId"})
        if search_area is not None:
            return search_area.text.strip()
    except Exception as e:
        print(e)
        print("Could not retrieve the seller name open the website and debug3")
        return ""

    return ""


def identity_seller(soup: BeautifulSoup):

    try:
        return _identity_seller1(soup)

    except Exception as e:
        print(e)
        try:
            return _identity_seller2(soup)

        except Exception as e:
            print(e)
            try:
                return _identity_seller3(soup)

            except Exception as e:
                print(e)
                return ""

    return ""


def get_stock_info(soup: BeautifulSoup):

    try:
        stock_info = soup.find("div", {"id": "availability_feature_div"})

        if stock_info is None:
            raise Exception("availability_feature_div ID not found")

        stock_info = "".join(tokenizer.tokenize(stock_info.text.strip().lower()))
        stock_info = " ".join(stock_info.split())

    except Exception as e:
        stock_info = soup.find("div", {"id": "availability"})
        return stock_info.text.strip()
    try:
        if stock_info is not None:
            return stock_info
    except Exception as e:
        pass
    return ""


def get_stars_reviews(soup: BeautifulSoup):

    try:
        search_area = soup.find("div", "a-row")

        try:
            st = search_area.find("i")["class"][-1]
        except Exception as e:
            print(str(e) + " Stars could not be retrieved")
            st = ""

        try:
            rev = search_area.find("span", "a-color-link").text.strip()
        except Exception as e:
            print(str(e) + " Reviews could not be retrieved")
            rev = ""

        return st, rev

    except Exception as e:
        print(str(e) + " Stars and reviews could not be retrieved")
        return "", ""

    return "", ""


def get_price_from_carousel(soup: BeautifulSoup):

    try:
        return soup.find("div", "a-row a-color-price").text.strip()
    except Exception as e:
        print(str(e) + " Price from Carousel could not be retrieved")
        return ""
    return ""


def extract_details(link: str, tracker):

    browserdriver = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
    browserdriver.get(link)

    timeout = 15

    try:
        wait = WebDriverWait(browserdriver, timeout)

    except TimeoutException as e:
        print(e)
        print("Timeout")
        browserdriver.quit()
        return {}

    try:

        content = browserdriver.page_source
        soup = BeautifulSoup(content, "html.parser")

        browserdriver.quit()
        product_title = soup.find("span", {"id": "productTitle"}).text.strip()
        seller = str(identity_seller(soup)).strip()
        if seller is None:
            return dict()
        if seller == tracker:
            return dict()
        stock_info = get_stock_info(soup)

        return dict(
            product_title=product_title,
            seller=seller,
            stock_info=stock_info,
        )

    except Exception as e:
        browserdriver.quit()
        print(e)
        return {}


def parse_carousel(soup: BeautifulSoup, tracker):

    skipped = 0
    r = []
    for data in soup.findChildren("li", recursive=False):
        try:
            asin = data.find(
                "div", "a-section sp_offerVertical p13n-asin sp_ltr_offer"
            )["data-asin"]
            link = data.find("a", "a-link-normal")["href"]

            details = extract_details(link, tracker)

            if details is None or details == dict():
                print("SKIPPING DUE TO SAME SELLER")
                skipped += 1
                time.sleep(7)
                continue

            stars, rev = get_stars_reviews(data)
            price = get_price_from_carousel(data)
            details["stars"] = stars
            details["reviews"] = rev
            details["price"] = price

            print(asin)
            print(link)
            print(details)
            print()

            r.append(dict(asin=asin, linkToProduct=link, details=details))
            time.sleep(7)

        except Exception as e:
            skipped += 1
            print(e)
            continue

    print(f"SKIPPED COMPETITORS - {skipped}")
    return r


def lookup_similar_products(soup: BeautifulSoup, tracker):

    try:
        search_area = soup.find("div", {"id": "sp_detail"})

        try:
            search_area = search_area.find("ol", "a-carousel")
        except Exception as e:
            print(str(e) + "Carousel1 not found")

    except Exception as e:
        print(str(e) + "sp_details not found")
        try:
            search_area = soup.find("div", {"id": "sp_detail2"})

            try:
                search_area = search_area.find("ol", "a-carousel")
            except Exception as e:
                print(str(e) + "Carousel2 not found")
        except Exception as e:
            print(str(e) + "sp_details2 not found")
            return []

    try:
        if search_area is not None:
            return parse_carousel(search_area, tracker)
    except Exception as e:
        print("sp_details AND sp_details2 found")
        return []
    return []


def track_for_product(soup: BeautifulSoup, asin, zone, search):

    try:
        seller_name = identity_seller(soup)
        if seller_name is None:
            return "NA"
        print(seller_name)
        tracker = seller_name

        tracking = lookup_similar_products(soup, tracker)

        return dict(
            tracker_firm=tracker,
            tracking=tracking,
            asin=asin,
            zone=zone,
            search=search,
        )

    except Exception as e:
        print(e)
        print("IN track_for_product")
        return {}

    return {}


def amazon_track_competition(asin: str, zone: str, *args, **kwargs):

    browserdriver = webdriver.Chrome(options=options, executable_path=r"./chromedriver")

    search = zone_to_url[zone] + "dp/" + asin
    browserdriver.get(search)

    print(search)
    print()

    timeout = 15

    try:
        wait = WebDriverWait(browserdriver, timeout)

    except TimeoutException as e:
        print(e)
        print("Timeout")
        browserdriver.quit()
        return {}

    try:

        content = browserdriver.page_source
        soup = BeautifulSoup(content, "html.parser")

        browserdriver.quit()

        return track_for_product(soup, asin, zone, search)

    except Exception as e:
        browserdriver.quit()
        print(e)
        print("IN amazon_track_competition")
        return {}


# print(amazon_track_competition("B07Y", "US"))
# amazon_track_competition("B07YWS4QTH", "US")
# amazon_track_competition("B07WSHWNH8", "IN")
# amazon_track_competition("B01MTQ5M7B", "IN")
# amazon_track_competition("B081KBXT5N", "US")
# amazon_track_competition("B07N39NDDB", "UK")
