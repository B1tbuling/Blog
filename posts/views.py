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


def get_form_create_post(request):
    form = PostForm
    return render(request, 'post_create.html', context={'form': form})


def create_post(request):
    form_data = PostForm(request.POST)
    if form_data.is_valid():
        data = dict(request.POST)
        title = data['title'][0]
        text = data['text'][0]
        post = Posts.objects.create(title=title, text=text)
        return redirect(reverse('get_post_page_url', kwargs={'pk': post.id}))
    else:
        return redirect('create_post_url')


def get_form_update_post(request, pk):
    post = Posts.objects.get(id=pk)
    form = PostForm({'title': post.title, 'text': post.text})
    return render(request, 'post_update.html', context={'form': form, 'post_id': pk})


def update_post(request, pk):
    form_data = PostForm(request.POST)
    if form_data.is_valid():
        data = dict(request.POST)
        post = Posts.objects.get(id=pk)
        post.title = data['title'][0]
        post.text = data['text'][0]
        post.save()
        return redirect(reverse('get_post_page_url', kwargs={'pk': post.id}))
    return redirect(reverse('get_form_update_post', kwargs={'pk': pk}))


