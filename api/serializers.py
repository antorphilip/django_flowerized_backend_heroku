from rest_framework import serializers
from flowerized_app.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'      
    

    def getImgurl(self, obj):
        return obj.itemPicture.url