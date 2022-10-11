from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user')
    item_name = serializers.CharField(source='item')
    class Meta:
        model = Cart
        fields = ('id', 'price', 'quantity', 'item_name', 'user_email')