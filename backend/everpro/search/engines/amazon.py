from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from six.moves.urllib.parse import urlencode, quote

from bs4 import BeautifulSoup

import re
import json

search_results = []
index = 0


def to_return(string: str) -> "str":
    return string if string is not None else ""


def popover(soup: BeautifulSoup) -> "Boolean":

    try:
        return (
            (soup.find("span", {"class": "s-label-popover-default"}) != None)
            or (soup.find("span", {"class": "s-label-popover"}) != None)
            or (soup.find("a", {"class": "s-label-popover"}) != None)
        )
    except Exception as e:
        return True


def image_link(soup: BeautifulSoup) -> "str":

    # print(data.find("div", "a-section aok-relative s-image-fixed-height")) # Image tag with differnt sizes of image
    try:
        # print(soup)
        link = soup.find("img")["src"]
    except KeyError as e:
        try:
            link = soup.find("img")["href"]
        except KeyError as e:
            return None

    return link


def product_name(soup: BeautifulSoup) -> "str":

    try:
        return to_return(soup.find("img")["alt"])
    except KeyError as e:
        return None


def other_details(soup: BeautifulSoup) -> "str":

    try:
        details_area = soup.find("div", "a-row a-size-base a-color-secondary").find(
            "span", {"class": "a-offscreen"}
        )
    except Exception as e:
        print(e)
        print("Other details not found (Amazon)")
        return ""

    if details_area is not None:
        return "" if details_area is None else details_area.text.strip()

    try:
        details_area = soup.find("div", "a-row a-size-base a-color-secondary").find(
            "span", {"class": "a-truncate-full"}
        )

        if details_area is not None:
            details_area.text.strip()
        else:
            details_area = soup.find("div", "a-row a-size-base a-color-secondary")
            return (
                ""
                if details_area is None
                else " ".join(details_area.text.strip().split())
            )
    except Exception as e:
        return ""


def get_price(soup: BeautifulSoup) -> "tuple(str, str, str)":

    curr, disc_price, cut_price = "₹", "", ""
    price = ""
    try:
        price = (
            soup.find("span", {"class": "a-price"})
            .find("span", {"class": "a-offscreen"})
            .text
        )
    except Exception as e:
        print(e)
        print("Price not Found (Amazon)")

    try:
        int(price[1:])
        curr, disc_price = "₹", price.strip()[1:]
    except Exception as e:
        curr, disc_price = price[0], price.strip()[1:]

    try:
        cut_price = (
            soup.find("span", {"class": "a-price", "data-a-strike": "true"})
            .find("span", {"class": "a-offscreen"})
            .text
        ).strip()[1:]

    except Exception as e:
        print(str(e) + " Cut price not found")

    return curr, disc_price, cut_price


def stars(soup: BeautifulSoup) -> "str":

    try:
        stars = soup.find(
            "div", {"class", "a-section a-spacing-none a-spacing-top-micro"}
        ).find("span", {"class": "a-icon-alt"})
        if stars is not None:
            return to_return(stars.text.strip())
        return to_return("0 out of 5 stars")
    except Exception as e:
        print(e)
        print("Starts not found (Amazon)")
        return to_return("0 out of 5 stars")


def count_reviews(soup: BeautifulSoup) -> "str":

    try:
        reviews = soup.find(
            "div", {"class", "a-section a-spacing-none a-spacing-top-micro"}
        ).find("span", {"class": "a-size-base", "dir": "auto"})
    except Exception as e:
        print(e)
        print("Review Count Not Found (Amazon)")
        return "0"
    if reviews is not None:
        return reviews.text.strip()
    return "0"


def product_link(soup: BeautifulSoup) -> "str":

    try:
        prod_area = soup.find("a", "a-link-normal a-text-normal")

        if prod_area is not None:
            return "https://www.amazon.in" + str(prod_area["href"]).strip()
        return ""
    except Exception as e:
        print(e)
        print("Priduct link Not Found (Amazon)")
        return ""


def lookup(search_area):

    global index
    global search_results

    count = 0
    for data in search_area:
        try:
            if popover(data):
                continue

            img_link_rsp = image_link(data)
            product_name_rsp = product_name(data)

            if image_link(data) is None or product_name_rsp is None:
                count += 1
                continue

            # print("Product Link: " + product_link(data))
            # print("Image Link: " + img_link_rsp)
            # print("Product Name: " + product_name_rsp)
            # print(stars(data))
            # print("Number of Reviews: " + str(count_reviews(data)))
            # print("Details: " + str(other_details(data)))
            currency, price_, cut_price = get_price(data)
            # print("Price: " + currency + price_)
            # print("Cut Price: " + currency + cut_price)
            # print()

            search_results.append(dict())
            search_results[index]["product_link"] = str(product_link(data)).strip()
            search_results[index]["image_link"] = str(img_link_rsp).strip()
            search_results[index]["product_name"] = str(product_name_rsp).strip()
            search_results[index]["stars"] = str(stars(data)).strip()
            search_results[index]["reviews"] = str(count_reviews(data)).strip()
            search_results[index]["other_details"] = str(other_details(data)).strip()
            search_results[index]["price"] = str(price_)
            search_results[index]["original_price"] = str(cut_price)
            search_results[index]["currency"] = str(currency).strip()

            index += 1

        except Exception as e:
            print(e)
            count += 1
            continue

    print(f"\nRESULTS SKIPPED - {count}\n")


def amazon_search_by_query(query: str, *args, **kwargs):

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")

    browserdriver = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
    # executable_path=r'path_to_driver'

    browserdriver.get("https://www.amazon.co.in/s?k=" + quote(query))

    print("https://www.amazon.co.in/s?k=" + quote(query))
    print()

    timeout = 10

    try:
        wait = WebDriverWait(browserdriver, timeout)

    except TimeoutException as e:
        print(str(e))
        browserdriver.quit()
        return []

    try:
        content = browserdriver.page_source
        soup = BeautifulSoup(content, "html.parser")

        search_area = soup.findAll("div", "a-section a-spacing-medium")
        if not search_area:
            search_area = soup.findAll(
                "div", "a-section a-spacing-medium a-text-center"
            )
            if not search_area:
                return []
        lookup(search_area)
        with open("./search/engines/amazon.json", "w", encoding="utf-8") as f:
            json.dump(search_results, f, ensure_ascii=False, indent=4)
        return search_results

    except Exception as e:
        print(e)
        return []


# amazon_search_by_query("belt")