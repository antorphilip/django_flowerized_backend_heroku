from django.urls import path
from cart import views


urlpatterns = [
    path('carts/', views.CartList.as_view(), name='cart_list'),
]
