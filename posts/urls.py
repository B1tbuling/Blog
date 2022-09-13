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
    path('change/<int:pk>', update_post, name='add_form_update_post'),
    path('tags/', get_tags_list, name='get_tags_list_url'),
    path('tags/create', get_form_create_tag, name='get_form_create_tag_url'),
    path('tags/add', add_form_create_tag, name='add_form_create_tag_url'),
    path('tags/update/<str:slug>', get_form_update_tag, name='get_form_update_tag_url'),
    path('tags/change/<str:slug>', change_form_update_tag, name='change_form_update_tag_url'),
    path('tags/<str:slug>', get_tag_page, name='get_tag_page_url')

]
