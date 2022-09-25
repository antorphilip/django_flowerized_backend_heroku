from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='User')
    item_name = serializers.CharField(source='Item')
    class Meta:
        model = Cart
        fields = ('id', 'price', 'quantity', 'user_email','item_name')