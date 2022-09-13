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
    form = PostModelForm()
    return render(request, 'post_create.html', context={'form': form})


def create_post(request):
    # form_data = PostForm(request.POST)
    form_post = PostModelForm(request.POST)
    if form_post.is_valid():
        post = form_post.save()
        # data = dict(request.POST)
        # title = data['title'][0]
        # text = data['text'][0]
        # post = Posts(title=title, text=text)
        # post.save()
        # post = Posts.objects.create(title=title, text=text)
        return redirect(reverse('get_post_page_url', kwargs={'pk': post.id}))
    else:
        return redirect('create_post_url')


def get_form_update_post(request, pk):
    post = Posts.objects.get(id=pk)
    # form = PostModelForm({'title': post.title, 'text': post.text})
    form = PostModelForm(instance=post)
    return render(request, 'post_update.html', context={'form': form, 'post_id': pk})


def update_post(request, pk):
    post = Posts.objects.get(id=pk)
    form_data = PostModelForm(request.POST, instance=post)
    if form_data.is_valid():
        form_data.save()
        # data = dict(request.POST)
        # post = Posts.objects.get(id=pk)
        # post.title = data['title'][0]
        # post.text = data['text'][0]
        # post.save()
        return redirect(reverse('get_post_page_url', kwargs={'pk': post.id}))
    return redirect(reverse('get_form_update_post', kwargs={'pk': pk}))


def get_tag_page(request, slug):
    tag = Tag.objects.get(tag__iexact=slug)
    return render(request, 'tag_page.html', context={'tag': tag})


def get_tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', context={'tags': tags})


def get_form_create_tag(request):
    tag_form = TagModelForm()
    return render(request, 'tag_create.html', context={'tag_form': tag_form})


def add_form_create_tag(request):
    form_data = TagModelForm(request.POST)
    if form_data.is_valid():
        new_tag = form_data.save()
        return redirect(reverse('get_tag_page_url', kwargs={'slug': new_tag.tag}))


def get_form_update_tag(request, slug):
    tag = Tag.objects.get(tag__iexact=slug)
    tag_form = TagModelForm(instance=tag)
    return render(request, 'tag_update.html', context={'tag_form': tag_form, 'slug': slug})


def change_form_update_tag(request, slug):
    tag = Tag.objects.get(tag=slug)
    form_data = TagModelForm(request.POST, instance=tag)
    if form_data.is_valid():
        new_tag = form_data.save()
        return redirect(reverse('get_tag_page_url', kwargs={'slug': new_tag.tag}))
