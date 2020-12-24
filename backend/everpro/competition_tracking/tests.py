from rest_framework.test import APITestCase
from competition_tracking.models import *
from django.urls import reverse
import json


class TestContactAPI(APITestCase):
    def test_get(self):
        response = self.client.get(reverse("competition_tracking_list_view"))
        self.assertEquals(response.status_code, 200)

    def test_post_request_can_create_new_entity(self):
        data = {"asin": "BXOSXSX", "zone": " IN"}
        self.client.post(reverse("competition_tracking_list_view"), data=data)
        self.assertEqual(ComepetetionTrack.objects.count(), 1)