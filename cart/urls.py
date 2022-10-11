from django.urls import path
from cart import views


urlpatterns = [
    path('carts/', views.getCart),
    path('addcarts/', views.addCart),

]
