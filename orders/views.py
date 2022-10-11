from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from orders.serializers import OrderSerializer
from orders.models import Order

# Create your views here.



@api_view(['GET'])
def getOrder(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['POST'])  
def addOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
