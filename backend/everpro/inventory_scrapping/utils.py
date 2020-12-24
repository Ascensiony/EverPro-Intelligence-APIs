from selenium import webdriver
from bs4 import BeautifulSoup

import time
from django.utils import timezone

from .models import ProductData
from .scrapper import search_product_by_asin


def update_productdata_table():
    pdata = ProductData.objects.all()
    for data in pdata:
        stock_info, product_name, all_other_details = search_product_by_asin(
            data.asin, data.zone
        )
        last_updated = timezone.now()

        data.stock_info = stock_info
        data.all_other_details = all_other_details
        data.product_name = product_name
        data.last_updated = last_updated
        data.save()
        time.sleep(5)
    print("Kudos! I did the task\n")
