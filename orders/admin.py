from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item')



admin.site.register(Order, OrderAdmin)