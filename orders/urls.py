from django.urls import path
from orders import views


urlpatterns = [
    path('orders/', views.getOrder),
    path('addorder/', views.addOrder),

]
