from django.http import HttpResponse
from django.urls import reverse

import json
from django.http import JsonResponse
from django.core.serializers import serialize

from api.models import Item

from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response

# Create your views here.


def index(request):
    view_api = reverse('view')

    index_page = f"""
    <h2>Django Backend API</h2>
    <h3>Supermarket Inventory Management System</h3>

    <p><a href='/admin'>Admin page</a></p>

    View the full JSON output <a href="{view_api}">Here.</a> 
    <br>
    <p>Api Endpoints:</p>
    <p>[GET]       view/</p>
    <p>[POST]      create/</p>
    <p>[PUT]       update/</p>
    <p>[DELETE]    delete/</p>
    """

    return HttpResponse(index_page)


def view(request):
    itens = Item.objects.all()

    serialized_data = serialize("json", itens)
    return JsonResponse(json.loads(serialized_data), safe=False)


@api_view(["POST"])
def create(request):
    post_item = request.data

    data = { "key": 'value' }

    return JsonResponse(data)


def delete(request):
    return ''
