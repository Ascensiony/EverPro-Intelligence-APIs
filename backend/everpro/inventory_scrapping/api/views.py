from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from inventory_scrapping.models import ProductData


@api_view(
    http_method_names=[
        "GET",
        "POST",
    ]
)
def productdata_list_view(request):
    if request.method == "GET":
        return productdata_list_view_get(request)
    elif request.method == "POST":
        return productdata_list_view_post(request)


def productdata_list_view_get(request):
    try:
        data = ProductData.objects.all()
        serializer = ProductDataSerializer(data, many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def productdata_list_view_post(request):
    try:
        pdata = ProductData()
        serializer = ProductDataSerializer(pdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except DatabaseError:
        return Response(status=status.HTTP_409_CONFLICT)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def productdata_detail_view(request, slug):
    try:
        pdata = ProductData.objects.get(asin=slug)
        if request.method == "GET":
            return productdata_detail_view_get(request, pdata)
        elif request.method == "PUT":
            return productdata_detail_view_put(request, pdata)
        elif request.method == "DELETE":
            return productdata_detail_view_delete(request, pdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def productdata_detail_view_get(request, pdata):
    serializer = ProductDataSerializer(pdata)
    return Response(serializer.data)


def productdata_detail_view_put(request, pdata):
    serializer = ProductDataSerializer(pdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def productdata_detail_view_delete(request, pdata):
    delresult = pdata.delete()
    data = {"message": "error during deletion"}
    if delresult[0] == 1:
        data = {"message": "succesfully deleted"}
    return Response(data)


"""
Example for PUT/POST
{
    "asin": "B08L5NP6NG",
    "platform": "Amazon",
    "zone": "US",
    "stock_info": null,
    "all_other_details": null,
    "product_name": null
}
"""