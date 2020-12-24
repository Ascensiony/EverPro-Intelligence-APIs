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


def popover(soup: BeautifulSoup, compressed=False) -> "Boolean":

    if compressed:
        try:
            print(soup.find("div", "_2I5qvP").text)
            return True
        except Exception as e:
            return False

    return False


def product_name(soup: BeautifulSoup):

    try:
        return str(soup.find("img", "_396cs4")["alt"])
    except Exception as e:
        print(str(e) + " Product Name could not be retrieved")
        return None


def image_link(soup: BeautifulSoup):

    try:
        return str(soup.find("img", "_396cs4")["src"])
    except Exception as e:
        print(str(e) + " Image could not be retrieved")
        return None


def stars(soup: BeautifulSoup):

    try:
        _stars = soup.find("div", "gUuXy-").find("div", "_3LWZlK")
    except Exception as e:
        print(str(e) + " Stars could not be retrieved")
        return ""

    if _stars is not None:
        return _stars.text.strip()

    return ""


def count_reviews_ratings(soup: BeautifulSoup) -> "tuple(str, str)":

    rev, rat = "", ""

    try:
        area = soup.find("div", "gUuXy-").find("span", "_2_R_DZ").find("span")

        try:
            for i, sp in enumerate(area.findChildren("span", recursive=False)):
                if i == 1:
                    continue
                if i == 0:
                    rat = sp.text.strip()
                if i == 2:
                    rev = sp.text.strip()

        except Exception as e:
            print(str(e) + " Reviews & Ratings div could not be retrieved 2")
            return "", ""

    except Exception as e:
        print(str(e) + " Reviews & Ratings div could not be retrieved 1")
        return "", ""

    return rev, rat


def get_details_curr_price(soup: BeautifulSoup) -> "tuple(str, str, str)":

    details, curr, price = "", "₹", ""

    try:
        area = soup.find("div", "col col-5-12 nlI3QM")

        try:
            price_area = area.find("div", "_3tbKJL")
            price = price_area.text.strip()[1:] if price_area is not None else ""
        except Exception as e:
            print(str(e) + " Price div could not be retrieved 2")
            price = ""

        try:
            details_area = area.find("div", "_2ZdXDB")
            details = details_area.text.strip() if details_area is not None else ""
        except Exception as e:
            print(str(e) + "Details div could not be retrieved 2")
            details = ""

    except Exception as e:
        print(str(e) + " Details, Price div could not be retrieved 1")
        return "", "₹", ""

    return details, curr, price


def compressed_image_link(soup: BeautifulSoup):

    try:
        return str(soup.find("img", "_2r_T1I")["src"])
    except Exception as e:
        print(str(e) + " Compressed Image could not be retrieved")
        return None


def compressed_product_name(soup: BeautifulSoup):

    try:
        name = soup.find("div", {"class": "_2B099V"}).find("a", "IRpwTa")
    except Exception as e:
        print(str(e) + " Compressed Name could not be retrieved")
        return None

    if name is not None:
        return name.text.strip()

    return ""


def compressed_product_brand(soup: BeautifulSoup):

    try:
        brand = soup.find("div", {"class": "_2B099V"}).find("div", "_2WkVRV")
    except Exception as e:
        print(str(e) + " Compressed Brand could not be retrieved")
        return None

    if brand is not None:
        return brand.text.strip()

    return ""


def compressed_get_details_curr_price(
    soup: BeautifulSoup,
) -> "tuple(str, str, str, str)":

    disc_price, curr, cut_pirce, disc = "", "", "", ""

    try:
        area = (
            soup.find("div", {"class": "_2B099V"})
            .find("a", "_3bPFwb")
            .find("div", "_25b18c")
        )

        try:
            disc_price_area = area.find("div", "_30jeq3")
            if disc_price_area is not None:
                disc_price = disc_price_area.text.strip()[1:]
                curr = disc_price_area.text.strip()[0]
        except Exception as e:
            print(str(e) + " Compressed discounted price could not be retrieved")

        try:
            cut_area = area.find("div", "_3I9_wc")
            if cut_area is not None:
                cut_pirce = cut_area.text.strip()[1:]
        except Exception as e:
            print(str(e) + " Compressed cut price could not be retrieved")

        try:
            area3 = area.find("div", "_3Ay6Sb")
            if area3 is not None:
                disc = area3.text.strip()
        except Exception as e:
            print(str(e) + " Compressed discount could not be retrieved")

    except Exception as e:
        print(
            str(e)
            + " Compressed discounted price, cut price, discount could not be retrieved"
        )

    return curr, disc_price, cut_pirce, disc


def test_img_format(link: str) -> "Boolean":
    if link.endswith(".svg") or not link.startswith("https://"):
        return False

    return True


def more_compressed_reviews(soup: BeautifulSoup) -> "str":

    try:
        area = soup.find("div", "gUuXy-").find("span", "_2_R_DZ")
        if area is not None:
            return area.text.strip()[1:-1]
        return ""
    except Exception as e:
        print(e)
        print(str(e) + " More Compressed review count could not be retrieved")

    return ""


def more_compressed_prices(soup: BeautifulSoup) -> "tulpe(str, str, str)":

    disc_price, curr, cut_pirce, disc = "", "", "", ""

    try:
        area = soup.find("a", "_8VNy32").find("div", "_25b18c")

        try:
            disc_price_area = area.find("div", "_30jeq3")
            if disc_price_area is not None:
                disc_price = disc_price_area.text.strip()[1:]
                curr = disc_price_area.text.strip()[0]
        except Exception as e:
            print(str(e) + " Compressed discounted price could not be retrieved")

        try:
            cut_area = area.find("div", "_3I9_wc")
            if cut_area is not None:
                cut_pirce = cut_area.text.strip()[1:]
        except Exception as e:
            print(str(e) + " Compressed cut price could not be retrieved")

        try:
            area3 = area.find("div", "_3Ay6Sb")
            if area3 is not None:
                disc = area3.text.strip()
        except Exception as e:
            print(str(e) + " Compressed discount could not be retrieved")

    except Exception as e:
        print(
            str(e)
            + " Compressed discounted price, cut price, discount could not be retrieved"
        )

    return curr, disc_price, cut_pirce, disc


def omg_flipkart_is_disaster(soup: BeautifulSoup):

    global index
    global search_results

    skipped = 0
    for data in soup:
        try:
            img_link_response = image_link(data)
            product_name_response = product_name(data)

            if img_link_response is None or product_name_response is None:
                skipped += 1
                continue

            if not test_img_format(img_link_response):
                skipped += 1
                continue

            # print("Image Link: " + img_link_response)
            # print("Product Name: " + product_name_response)
            # print("Stars: " + stars(data))
            # print("Reviews: " + more_compressed_reviews(data))
            curr, disc_price, cutprice, disc = more_compressed_prices(data)
            # print("Price: " + curr + disc_price)
            # print("Cut Price: " + curr + cutprice)
            # print("Discount: " + disc)
            # print()

            search_results.append(dict())
            # search_results[index]["product_link"] = str(product_link(data)).strip()
            search_results[index]["image_link"] = str(img_link_response).strip()
            search_results[index]["product_name"] = str(product_name_response).strip()
            # search_results[index]["brand"] = str(compressed_product_brand(data)).strip()
            search_results[index]["stars"] = str(stars(data)).strip()
            search_results[index]["reviews"] = str(
                more_compressed_reviews(data)
            ).strip()
            # search_results[index]["ratings"] = str(rat).strip()
            # search_results[index]["other_details"] = str(details).strip()
            search_results[index]["price"] = str(disc_price).strip()
            search_results[index]["original_price"] = str(cutprice).strip()
            search_results[index]["discount_percentage"] = str(disc).strip()
            search_results[index]["currency"] = str(curr).strip()

            index += 1

        except Exception as e:
            skipped += 1
            print(e)
            continue

    print(f"\nCOMPRESSED FLIPCART RESULTS SKIPPED - {skipped}")


def compressed_lookup(soup: BeautifulSoup):

    global index
    global search_results

    skipped = 0
    please_be_false = False
    for data in soup:
        try:
            if data.find("div", {"class": "_4ddWXP"}) is not None:
                please_be_false = True
                break
            if popover(data, compressed=True):
                continue

            img_link_response = compressed_image_link(data)
            product_name_response = compressed_product_name(data)

            if img_link_response is None or product_name_response is None:
                skipped += 1
                continue

            # print("Image Link: " + img_link_response)
            # print("Product Name: " + product_name_response)
            # print("Brand: " + compressed_product_brand(data))

            curr, disc_price, cutprice, disc = compressed_get_details_curr_price(data)

            # print("Price: " + curr + disc_price)
            # print("Cut Price: " + curr + cutprice)
            # print("Discount: " + disc)
            # print()

            search_results.append(dict())
            # search_results[index]["product_link"] = str(product_link(data)).strip()
            search_results[index]["image_link"] = str(img_link_response).strip()
            search_results[index]["product_name"] = str(product_name_response).strip()
            search_results[index]["brand"] = str(compressed_product_brand(data)).strip()
            # search_results[index]["stars"] = str(stars(data)).strip()
            # search_results[index]["reviews"] = str(rev).strip()
            # search_results[index]["ratings"] = str(rat).strip()
            # search_results[index]["other_details"] = str(details).strip()
            search_results[index]["price"] = str(disc_price).strip()
            search_results[index]["original_price"] = str(cutprice).strip()
            search_results[index]["discount_percentage"] = str(disc).strip()
            search_results[index]["currency"] = str(curr).strip()

            index += 1

        except Exception as e:
            skipped += 1
            print(e)
            continue

    if please_be_false:
        omg_flipkart_is_disaster(soup)
        return
    print(f"\nCOMPRESSED FLIPCART RESULTS SKIPPED - {skipped}")


def lookup(soup: BeautifulSoup):

    global index
    global search_results

    skipped = 0
    for data in soup:
        try:
            data = data.find("div", "_13oc-S")

            children = data.findChildren("div", recursive=False)

            if len(children) > 1:
                print("\nCOMPRESSED VIEW\n")
                compressed_lookup(children)
                continue

            if popover(data):
                continue

            img_link_response = image_link(data)
            product_name_response = product_name(data)

            if img_link_response is None or product_name_response is None:
                skipped += 1
                continue

            # print("Image Link: " + img_link_response)
            # print("Product Name: " + product_name_response)
            # print("Stars: " + stars(data))
            rev, rat = count_reviews_ratings(data)
            # print("Reviews: " + rev)
            # print("Ratings: " + rat)
            details, curr, price = get_details_curr_price(data)
            # print("Details: " + details)
            # print("Price: " + curr + price)
            # print()

            search_results.append(dict())
            # search_results[index]["product_link"] = str(product_link(data)).strip()
            search_results[index]["image_link"] = str(img_link_response).strip()
            search_results[index]["product_name"] = str(product_name_response).strip()
            search_results[index]["stars"] = str(stars(data)).strip()
            search_results[index]["reviews"] = str(rev).strip()
            search_results[index]["ratings"] = str(rat).strip()
            search_results[index]["other_details"] = str(details).strip()
            search_results[index]["price"] = str(price)
            # search_results[index]["original_price"] = str(cut_price)
            search_results[index]["currency"] = str(curr).strip()

            index += 1

        except Exception as e:
            skipped += 1
            print(e)
            continue

    print(f"\nFLIPCART RESULTS SKIPPED - {skipped}")


def flipkart_search_by_query(query: str, *args, **kwargs):

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")

    browserdriver = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
    browserdriver.get("https://www.flipkart.com/search?q=" + quote(query))

    print("https://www.flipkart.com/search?q=" + quote(query))
    print()

    timeout = 10

    try:
        wait = WebDriverWait(browserdriver, timeout)

    except TimeoutException:
        browserdriver.quit()
        return "Timed out waiting page to load"

    try:
        content = browserdriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        try:
            soup = soup.find("div", "E2-pcE _3zjXRo")
            if soup is None:
                return []
        except Exception as e:
            return []

        try:
            soup = soup.findChildren("div", recursive=False)[-1]
        except Exception as e:
            print(str(e) + " Results list is empty!! (Flipcart)")

        soup = soup.findAll("div", {"class": "_2pi5LC col-12-12"})

        if soup is None:
            return []

        lookup(soup)

        with open("./search/engines/flipkart.json", "w", encoding="utf-8") as f:
            json.dump(search_results, f, ensure_ascii=False, indent=4)

        return search_results

    except Exception as e:
        print(e)
        return []


# flipkart_search_by_query("iPhone 11")