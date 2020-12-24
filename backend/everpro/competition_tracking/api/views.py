from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .utils import GET_CT, POST_CT, DELETE_CT, PUT_CT


@api_view(
    http_method_names=[
        "GET",
        "POST",
    ]
)
def competition_tracking_list_view(request):
    if request.method == "GET":
        return competition_tracking_list_view_get(request)
    elif request.method == "POST":
        return competition_tracking_list_view_post(request)


def competition_tracking_list_view_get(request):
    try:
        return Response(GET_CT(asin="all"))
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)


def competition_tracking_list_view_post(request):
    try:
        return Response(
            POST_CT(
                dict(asin=str(request.data["asin"]), zone=str(request.data["zone"]))
            )
        )
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def competition_tracking_detail_view(request, slug):
    try:
        if request.method == "GET":
            return competition_tracking_detail_view_get(request, slug)
        elif request.method == "PUT":
            return competition_tracking_detail_view_put(request, slug)
        elif request.method == "DELETE":
            return competition_tracking_detail_view_delete(request, slug)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)


def competition_tracking_detail_view_get(request, slug):
    return Response(GET_CT(asin=str(slug)))


def competition_tracking_detail_view_put(request, slug):
    try:
        return Response(PUT_CT(dict(asin=str(slug), zone="IN")))
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def competition_tracking_detail_view_delete(request, slug):
    return Response(DELETE_CT(dict(asin=str(slug), zone="IN")))


"""
test case
{
    "asin": "B085J1D8BH",
    "zone": "IN"
}
"""