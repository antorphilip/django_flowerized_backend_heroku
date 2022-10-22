from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from items import serializers
from items.serializers import ItemSerializer
from items.models import Item
from rest_framework.decorators import api_view


class ItemsList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, context={'request': request}, many=True)
        return Response(serializer.data)
    


@api_view(['GET'])
def itemtest(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, context={'request': request})
    return Response(serializer.data)
