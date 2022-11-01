from django.urls import path
from cart import views


urlpatterns = [
    path('carts/', views.getCart),
    path('usercart/<str:user>/<str:item>', views.usercart),

]
