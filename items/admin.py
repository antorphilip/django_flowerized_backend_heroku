from django.contrib import admin
from items.models import Item
from items.models import Categories


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Category')


admin.site.register(Item, ItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
