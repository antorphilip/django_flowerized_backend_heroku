from django.contrib import admin
from .models import Account
from .models import Item

# Register your models here.
admin.site.register(Account)
admin.site.register(Item)