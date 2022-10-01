from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from cart.serializers import CartSerializer
from cart.models import Cart

# Create your views here.



@api_view(['GET'])
def getCart(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['POST'])  
def addCart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
