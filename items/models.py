from django.db import models


class Item(models.Model):
    name=models.CharField(max_length=1000)
    price=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='items/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
