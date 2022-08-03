from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from items.serializers import ItemSerializer
from items.models import Item


class ItemsList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, context={'request': request}, many=True)
        return Response(serializer.data)
