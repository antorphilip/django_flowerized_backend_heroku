from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user')
    item_name = serializers.CharField(source='item')
    class Meta:
        model = Order
        fields = ('id', 'total', 'item_name', 'user_email')