from operator import itemgetter
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from cart.serializers import CartSerializer
from cart.models import Cart
from users.serializers import MyTokenObtainPairSerializer, UserSerializer
from users.models import User
from items.models import Item

# Create your views here.



@api_view(['GET', 'POST'])
def getCart(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer._errors)


@api_view(['GET', 'POST']) #used filter to return more than one elements
def usercart(request, user, item):
    if request.method == 'GET':
        carts = Cart.objects.filter(user=user)
        serializer = CartSerializer(carts, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        carts = Cart.objects.get(user=user, item=item)
        serializer = CartSerializer(instance=carts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer._errors)
