from django.test import TestCase
from django.urls import reverse
import unittest


class TestSearchResultRobustness(TestCase):
    def test_search(self):
        response = self.client.post(
            reverse("search_product"), data=dict(query="iphone 8")
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
