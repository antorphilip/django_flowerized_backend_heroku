from django.db import models
from users.models import User
from items.models import Item
from django.contrib.auth.models import User
from django.conf import settings
from cart.models import Cart
import os
from twilio.rest import Client
from vonage import Client
import vonage


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, null=True)
    isOrdered = models.BooleanField(default=False)
    total=models.IntegerField(default=0)

    def __str__(self):
        return str(self.isOrdered)
    
    def save(self, *args, **kwargs):
        if self.isOrdered == True:
            client = vonage.Client(key="98bd98b4", secret="f0z9PO7RBgDPfRUR")
            sms = vonage.Sms(client)

            responseData = sms.send_message(
                {
                    "from": "Vonage APIs",
                    "to": "639950223470",
                    "text": "Hi, this is a message from flowerized.",
                }
            )

            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        return super().save(*args, **kwargs)
