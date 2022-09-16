from django.contrib import admin
from django.urls import path, include
from flowerized_app import views
from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('users/', views.create_and_show_acount),
    re_path('userdetail/(?P<id>\w+)$',views.userData),
    re_path('^updateUser/(?P<id>\w+)$',views.updateData),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)