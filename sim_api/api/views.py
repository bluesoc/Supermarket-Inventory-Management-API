from django.http import HttpResponse
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
    view_api = reverse('view')

    # Note that these variables are used for cosmetics only.
    # The entire "index()" method code can be deleted at will.
    # It does not affect the API.

    valid_endpoints = {
        "[GET]": "view/",
        "[POST]": "create/",
        "[DELETE]": "delete/<int:id>",
        "[PUT]": "update/<int:id>",
    }

    all_endpoints = ''

    for method in valid_endpoints:
        all_endpoints += f"""<tr><th>{ method }</th><th>{ valid_endpoints[method] }</th></tr>"""

    index_page = f"""
    <!-- Styling provided by W3Schools - www.w3schools.com -->
    <style>
        td, th {{
          border: 1px solid #dddddf;
          text-align: left;
          padding: 8px;
          font-weight: normal;
        }}
        tr:nth-child(even) {{
          background-color: #dddddf;
        }}
    </style>
    <h2>Django Backend API</h2>
    <h3>Supermarket Inventory Management System</h3>

    <p>View the full JSON output <a href="{view_api}">Here.</a> Or access the <a href='/admin'>Admin page</a></p>
  
    <p><b>Api Endpoints:</b></p>
    <table>
    <tr>
        <th>Method</th>
        <th>Route</th>
    </tr>
    { all_endpoints }
    </table>

    <br>
    <p><b>Interactive API Request Interface</b></p>

    <form method="POST" action="">
        <button type="submit" name="action" value="POST">POST</button>
        <input type="text" id="name" name="name" placeholder="Name" required size="15">
        <input type="text" id="category" name="category" placeholder="Category" required size="10">
        <input type="text" id="amount" name="amount" placeholder="Amount (Integer)" required size="15" oninput="this.value = this.value.replace(/[^0-9]/g, '');">
    </form>
    <form method="DELETE" action="">
        <button type="submit" name="action" value="IDK">DELETE</button>
        <input type="text" id="id" name="id" placeholder="Id Key (Integer)" required size="15" oninput="this.value = this.value.replace(/[^0-9]/g, '');">
    </form>
    <form method="PUT" action="">
        <button type="submit" name="action" value="POST">UPDATE</button>
    </form>
    """

    return HttpResponse(index_page)


@api_view(["GET"])
def view(request):
    itens = Item.objects.all()
    serialized_data = serialize("json", itens)
    return JsonResponse(json.loads(serialized_data), safe=False)


@api_view(["POST"])
def create(request):
    serialized_item = ItemSerializer(data=request.data)

    if serialized_item.is_valid():
        serialized_item.save()
        return Response(serialized_item.data, status=201)

    return Response(serialized_item.errors, status=404)


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
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    except delete_item.DoesNotExist:
        return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

