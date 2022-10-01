from django.db import models
from users.models import User
from items.models import Item
from django.contrib.auth.models import User
from django.conf import settings
from cart.models import Cart


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, null=True)
    total=models.IntegerField(default=0)
