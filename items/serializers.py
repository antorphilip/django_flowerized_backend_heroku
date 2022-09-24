from rest_framework import serializers
from items.models import Item
from items.models import Categories

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category')
    package_name = serializers.CharField(source='package')
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'category_name','package_name', 'is_active', 'created', 'img_url')


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'