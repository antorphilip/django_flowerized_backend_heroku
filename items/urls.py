from django.urls import path
from items import views


urlpatterns = [
    path('items/', views.ItemsList.as_view(), name='items_list'),
]
