from rest_framework.test import APITestCase
from inventory_scrapping.models import ProductData
from django.urls import reverse
import json


class TestProductDataAPI(APITestCase):
    def test_get(self):
        response = self.client.get(reverse("productdata_list_view"))
        self.assertEquals(response.status_code, 200)

    def test_post_request_can_create_new_entity(self):
        data = {
            "asin": "B01DN08VAY",
            "platform": "Amazon",
            "zone": "US",
            "stock_info": None,
            "all_other_details": None,
            "product_name": None,
        }
        self.client.post(reverse("productdata_list_view"), data=data)
        # self.assertEqual(ComepetetionTrack.objects.count(), 1)
