from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_posts_list, name='get_posts_list_url'),
    path('<int:pk>/', get_post_page, name='get_post_page_url'),
    path('create/', get_form_create_post, name='get_form_create_post'),
    path('add/', create_post, name='add_form_create_post'),
    path('update/<int:pk>', get_form_update_post, name='get_form_update_post'),
    path('change/<int:pk>', update_post, name='add_form_update_post')
]
