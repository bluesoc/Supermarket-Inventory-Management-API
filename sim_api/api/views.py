from django.shortcuts import render
from django.urls import reverse

from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response

from api.models import Item
from .serializer import ItemSerializer
import json

# Create your views here.


# Starting Page View
def index(request):
    valid_endpoints = [
        ["[GET]", "view/", "[optional] id=int"],
        ["[POST", "create/", "name='str' category='str' quantity='int'"],
        ["[DELETE]", "delete/<int:id>", "id=int"],
        ["[PUT]", "update/<int:id>", "id=int <updated attributes>"],
        ["[GET]", "search?q=<str>", "str=Name of the item"],
    ]

    return render(
        request,
        "api/index.html",
        {
            "valid_endpoints": valid_endpoints,
        }
    )


# Fetch a item
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


# Create Item on DB
@api_view(['POST'])
def create(request):
    serialized_item = ItemSerializer(data=request.data)

    if serialized_item.is_valid():
        serialized_item.save()
        return Response(serialized_item.data, status=201, content_type='application/json')

    return Response(serialized_item.errors, status=404, content_type='application/json')


# Update Item on DB
@api_view(['PUT'])
def update(request, id):
    try:
        update_item = Item.objects.get(pk=id)
        serialized_item = ItemSerializer(instance=update_item, data=request.data)

        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)

    except ObjectDoesNotExist: #update_item.DoesNotExist:
        return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as ERR:
        print("\nERR:", ERR, "\n\n")
        return Response({"message": "Internal Exception"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(request, id=None):
    try:
        delete_item = Item.objects.get(id=id)
        delete_item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_202_ACCEPTED)

    except: # delete_item.DoesNotExist:
        return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Send me a DELETE request with a item id"}, status=status.HTTP_404_NOT_FOUND)



# Query item. Endpoint: /search?q=
@api_view(['GET'])
def search(request):
    try:
        q = request.GET.get('q')

        if not q:
                return JsonResponse(
                    {"message": "Send me a GET request with a string"},
                    status=status.HTTP_404_NOT_FOUND)

        fetch_item = Item.objects.filter(
            name__icontains=q,
            manufacturer__icontains=q
        )

        print(type(fetch_item), " >> ", fetch_item)

        serialized_data = serialize("json", fetch_item)

        return JsonResponse(
                    json.loads(serialized_data),
                    safe=False,
                    status=status.HTTP_200_OK)

    except Exception as ERR_SEARCH:
        print("EXCEPTION: ", ERR_SEARCH)
        return JsonResponse({"message": "Can't search item"}, status=status.HTTP_404_NOT_FOUND)

