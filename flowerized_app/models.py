from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField("name",max_length=1000)
    Category=models.CharField("Category",max_length=1000,default='No category')
    Description=models.CharField("Description",max_length=1000,default='No description')
    Price=models.IntegerField("Price",default=0)
    is_active=models.BooleanField(default=True)
    itemPicture=models.ImageField("itemPicture",upload_to='media',blank=True,default='default.jpg',null=True)
    img_url = models.URLField(max_length = 200, default='https://firebasestorage.googleapis.com/v0/b/flowerized-site.appspot.com/o/ITEM%20IMAGES%2Fmomo.jpg?alt=media&token=bb9f6285-af13-4d36-8f41-c7027019f9d1')
    created = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    firstName=models.CharField("First Name",max_length=1000)
    lastName=models.CharField("Last Name",max_length=1000)
    email=models.EmailField("Email",max_length=1000)
    phoneNumber=models.CharField("phoneNumber",max_length=1000)
    password=models.CharField("password",max_length=2000)
    token=models.CharField("token",max_length=2000,null=True)


