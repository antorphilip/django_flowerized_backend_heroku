from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from users import views

urlpatterns = [
    path('', views.get_routes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserList.as_view(), name='users_list'),
    # re_path('userdetail/(?P<id>\w+)$',views.UserList.as_view()),
    path('register/', views.register),
]
