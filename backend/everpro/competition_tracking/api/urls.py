from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(
        "competition_tracking/",
        views.competition_tracking_list_view,
        name="competition_tracking_list_view",
    ),
    path(
        "competition_tracking/<slug:slug>/",
        views.competition_tracking_detail_view,
        name="competition_tracking_detail_view",
    ),
]