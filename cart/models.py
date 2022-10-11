from django.db import models
from users.models import User
from items.models import Item
from django.contrib.auth.models import User
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE, null=True)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)

    