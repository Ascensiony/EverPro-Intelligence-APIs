from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("productdata/", views.productdata_list_view, name="productdata_list_view"),
    path(
        "productdata/<slug:slug>",
        views.productdata_detail_view,
        name="productdata_detail_view",
    ),
]