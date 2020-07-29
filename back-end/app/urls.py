from django.contrib import admin
from django.urls import path
from app.controllers.controller_auth import *
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', FetchUserView.as_view()),  # Used to fetch login user
    path('user/login', views.obtain_auth_token, name='token'),
    path('user/is-valid-key', token_is_valid),
    path('user/register', CreateUserView.as_view()),
    path('user/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', FetchUsersView.as_view()),
]
