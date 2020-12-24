from django.db import models
import uuid

# from djongo import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from django.conf import settings


class ProductData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asin = models.CharField(max_length=20, unique=True)
    platform = models.CharField(max_length=20)
    zone = models.CharField(max_length=20)

    stock_info = models.CharField(max_length=20, blank=True)
    all_other_details = models.TextField(null=True, blank=True)
    product_name = models.CharField(max_length=20, blank=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "ASIN" + " " + str(self.asin)