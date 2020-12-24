from rest_framework import serializers
from inventory_scrapping.models import ProductData

from django.utils import timezone


class ProductDataSerializer(serializers.Serializer):
    asin = serializers.CharField(max_length=20)
    platform = serializers.CharField(max_length=10)
    zone = serializers.CharField(max_length=10)

    stock_info = serializers.CharField(max_length=100, allow_null=True)
    all_other_details = serializers.CharField(max_length=500, allow_null=True)
    product_name = serializers.CharField(max_length=100, allow_null=True)
    last_updated = serializers.DateTimeField(default=timezone.now())

    def create(self, validated_data):
        return ProductData(**validated_data)

    def update(self, instance, validated_data):
        instance.asin = validated_data.get("asin", instance.asin)
        instance.platform = validated_data.get("platform", instance.platform)
        instance.zone = validated_data.get("zone", instance.zone)

        # instance.stock_info = validated_data.get("stock_info", instance.stock_info)
        # instance.all_other_details = validated_data.get("all_other_details", instance.all_other_details)
        # instance.product_name = validated_data.get("product_name", instance.product_name)
        instance.save()
        return instance