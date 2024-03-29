from django.shortcuts import render
from django.urls import reverse

import json
from django.http import JsonResponse
from django.core.serializers import serialize

from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response

from api.models import Item
from .serializer import ItemSerializer

# Create your views here.


def index(request):
    # Note that these variables are used for cosmetics only.
    # The entire "index()" method code can be deleted at will.
    # It does not affect the API.

    valid_endpoints = {
        "[GET]": "view/",
        "[POST]": "create/",
        "[DELETE]": "delete/<int:id>",
        "[PUT]": "update/<int:id>",
    }

    return render(
        request,
        "api/index.html",
        {
            "valid_endpoints": valid_endpoints,
        }
    )


@api_view(["GET"])
def view(request, id=None):
    if id is not None:
        try:
            item = Item.objects.filter(pk=id)

            if not item:
                raise Exception

            serialized_data = serialize("json", item)
            return JsonResponse(
                json.loads(serialized_data),
                safe=False,
                status=status.HTTP_200_OK
                )
        except:
            msg = {"message": "Item not found"}
            return JsonResponse(msg, safe=False, status=status.HTTP_404_NOT_FOUND)

    itens = Item.objects.all()
    serialized_data = serialize("json", itens)
    return JsonResponse(json.loads(serialized_data), safe=False)


@api_view(["POST"])
def create(request):
    serialized_item = ItemSerializer(data=request.data)

    if serialized_item.is_valid():
        serialized_item.save()
        return Response(serialized_item.data, status=201, content_type='application/json')

    return Response(serialized_item.errors, status=404, content_type='application/json')


@api_view(['PUT'])
def update(request, id):
    try:
        update_item = Item.objects.get(id=id)
        serialized_item = ItemSerializer(update_item, data=request.data)

        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)

    except update_item.DoesNotExist:
        return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(request, id):
    try:
        delete_item = Item.objects.get(id=id)
        delete_item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_202_ACCEPTED)

    except: # delete_item.DoesNotExist:
        return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
