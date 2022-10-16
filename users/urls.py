from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', ...., name='....'),
    path('register/', register_user, name='register_user_url'),
    path('login/', login_user, name='login_user_url'),
    path('logout/', logout_user, name='logout_user_url'),
    path('profile/', get_profile_user, name='get_profile_user_url')
]