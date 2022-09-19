from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_posts_list, name='get_posts_list_url'),
    path('<int:pk>/', get_post_page, name='get_post_page_url'),
    path('create/', create_post, name='create_post_url'),
    path('update/<int:pk>', update_post, name='update_post_url'),
    path('delete/<int:pk>', delete_post, name='delete_post_url'),

    path('tags/', get_tags_list, name='get_tags_list_url'),
    path('tags/create', create_tag, name='create_tag_url'),
    path('tags/update/<str:slug>', update_tag, name='update_tag_url'),
    path('delete/<str:slug>', delete_tag, name='delete_tag_url'),
    path('tags/<str:slug>', get_tag_page, name='get_tag_page_url')

]
