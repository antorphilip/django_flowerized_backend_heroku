from django.contrib import admin
from items.models import Item
from items.models import Categories
from items.models import Package


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Category',)


class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Package',)



admin.site.register(Item, ItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Package, PackageAdmin)
