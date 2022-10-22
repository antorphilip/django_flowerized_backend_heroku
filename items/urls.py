from django.urls import path
from items import views


urlpatterns = [
    path('items/', views.ItemsList.as_view(), name='items_list'),
    path('items/<int:pk>/', views.itemtest, name='items_list'),
    #used to call the items by id
    path('itemcategory/<str:category>/', views.itemcategory, name='items_list'),
    #used category id to call categories not category name
    path('itempackage/<str:package>/', views.itempackage, name='items_list'),
    #used package id to call package not package name
]

