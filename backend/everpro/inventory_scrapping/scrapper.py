from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

from nltk.tokenize import RegexpTokenizer

zone_to_url = {
    "US": "https://www.amazon.com/",
    "UK": "https://www.amazon.co.uk/",
    "IN": "https://www.amazon.co.in/",
}

tokenizer = RegexpTokenizer(r"[a-zA-Z\s\d]")


def search_product_by_asin(asin: str, zone: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")

    print(zone_to_url[zone] + "dp/" + asin)

    browserdriver = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
    browserdriver.get(zone_to_url[zone] + "dp/" + asin)

    timeout = 10

    try:
        wait = WebDriverWait(browserdriver, timeout)
        wait.until(EC.visibility_of_element_located((By.ID, "availability")))
        wait.until(EC.visibility_of_element_located((By.ID, "productTitle")))

    except TimeoutException:
        print("Timed out waiting page to load")
        browserdriver.quit()
        return "N/A", "N/A", "N/A"

    try:
        content = browserdriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        search_area = soup.find("div", {"id": "availability_feature_div"})
        stock_info = "".join(tokenizer.tokenize(search_area.text.strip().lower()))
        stock_info = " ".join(stock_info.split())

        if stock_info == "":
            search_area = soup.find("div", {"id": "availability"})
            stock_info = "".join(tokenizer.tokenize(search_area.text.strip().lower()))
            stock_info = " ".join(stock_info.split())

        search_area = soup.find("span", {"id": "productTitle"})
        product_name = search_area.text.strip()

        search_area = soup.find(
            "table", {"id": "productDetails_detailBullets_sections1"}
        )

        if search_area != None:
            table = " ".join(search_area.text.strip().split())

        else:
            table = "Other details not available"

        return stock_info, product_name, table

    except Exception as e:
        return "N/A", "N/A", "N/A"


# print(search_product_by_asin("B08695YMYC", "IN"))
