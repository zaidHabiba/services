from django.contrib import admin
from django.urls import path
from app.controllers.controller_auth import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', FetchUserView.as_view()),  # Used to fetch login user
    path('user/login', AuthToken.as_view()),
    path('user/is-valid-key', token_is_valid),
    path('user/<pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', FetchUsersView.as_view()),
]
