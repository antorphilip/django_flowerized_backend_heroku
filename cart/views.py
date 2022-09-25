from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.serializers import CartSerializer
from cart.models import Cart

# Create your views here.



class CartList(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(Cart, context={'request': request}, many=True)
        return Response(serializer.data)