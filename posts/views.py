from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse


def get_post_page(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'post_page.html', context={'post': post})


def get_posts_list(request):
    posts = Posts.objects.all()
    return render(request, 'posts_list.html', context={'posts': posts})


# def get_post_form(request):
#     form = TestForm
#     return render(request, 'post_create.html', context={'form': form})
#     # return render(request, 'post_create.html', context={'forms': form})


def create_post(request):
    form = PostForm
    return render(request, 'post_create.html', context={'form': form})


def add_post(request):
    date = dict(request.POST)
    title = date['title'][0]
    text = date['text'][0]
    if title == "" or text == "":
        return redirect('create_post_url')
    else:
        post = Posts.objects.create(title=title, text=text)
        post.save()
        return redirect('get_posts_list_url')


def update_post(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'post_update.html', context={'post_update': post})


def change_post(request, pk):
    date = dict(request.POST)
    title = date['title'][0]
    text = date['text'][0]
    if title == "" or text == "":
        return redirect('get_posts_list_url')
    else:
        post = Posts.objects.get(id=pk)
        post.title = title
        post.text = text
        post.save()
        return redirect('get_posts_list_url')
