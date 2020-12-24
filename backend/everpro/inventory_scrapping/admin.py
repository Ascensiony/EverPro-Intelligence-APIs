from django.contrib import admin
from .models import ProductData

# Register your models here.
# admin.site.register(user_info_10004)
admin.site.register(ProductData)

# redis-server
# celery -A inventory_scrapping worker -l info
# celery -A inventory_scrapping beat -l info