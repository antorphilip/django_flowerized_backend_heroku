from django.db import models


class Item(models.Model):
    name=models.CharField(max_length=1000)
    price=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='items/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(max_length = 200, default="https://firebasestorage.googleapis.com/v0/b/flowerized-site.appspot.com/o/momo.jpg?alt=media&token=d902bfc4-e239-44cc-bb89-cf9e2e20b1c5")
