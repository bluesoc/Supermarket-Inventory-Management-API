from django.shortcuts import render
from django.shortcuts import get_object_or_404

from api.models import Item

import json
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.


def index(request):
    data = {
        'key': 'value',
        'api endpoint 1': '/',
        'api endpoint 2': 'create',
        'api endpoint 3': 'delete', 
    }
    return JsonResponse(data)

def view(request):
    itens = Item.objects.all()

    serialized_data = serialize("json", itens)
    return JsonResponse(json.loads(serialized_data), safe=False)


def create(request):
    return ''

def delete(request):
    return ''
