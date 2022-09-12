from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_posts_list, name='get_posts_list_url'),
    path('<int:pk>/', get_post_page, name='get_post_page_url'),
    # path('form/', get_post_form, name='get_post_form_url'),
    path('create/', create_post, name='create_post_url'),
    path('add/', add_post, name='add_post_url'),
    path('update/<int:pk>', update_post, name='update_post_url'),
    path('change/<int:pk>', change_post, name='change_post_url')
]
