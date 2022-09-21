from rest_framework import serializers
from items.models import Item
from items.models import Categories

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image.url


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'