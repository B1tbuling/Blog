from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse


def get_post_page(request, pk):
    post = Posts.objects.get(id=pk)
    tags = post.tags.all()
    return render(request, 'posts/post_page.html', context={'post': post, 'tags': tags})


def get_posts_list(request):
    posts = Posts.objects.all()
    return render(request, 'posts/posts_list.html', context={'posts': posts})


def create_post(request):
    if request.method == 'GET':
        form = PostModelForm()
        tags = Tag.objects.all()
        return render(request, 'posts/post_create.html', context={'form': form, 'tags': tags})

    if request.method == 'POST':
        form_post = PostModelForm(request.POST)
        print(request.POST)
        if form_post.is_valid():
            post = form_post.save()
            return redirect(reverse('get_post_page_url', kwargs={'pk': post.id}))
        else:
            return redirect('create_post_url')

    return HttpResponse(status=405)


def update_post(request, pk):
    if request.method == 'GET':
        post = Posts.objects.get(id=pk)
        form = PostModelForm(instance=post)
        return render(request, 'posts/post_update.html', context={'form': form, 'post_id': pk})

    if request.method == 'POST':
        post = Posts.objects.get(id=pk)
        form_data = PostModelForm(request.POST, instance=post)
        if form_data.is_valid():
            form_data.save()
            return redirect(reverse('get_post_page_url', kwargs={'pk': post.id}))
        return redirect(reverse('update_post_url', kwargs={'pk': pk}))

    return HttpResponse(status=405)


def delete_post(request, pk): ...


def get_tag_page(request, slug):
    tag = Tag.objects.get(tag__iexact=slug)
    posts = tag.posts.all()
    print(posts)
    return render(request, 'tags/tag_page.html', context={'tag': tag, 'posts': posts})


def get_tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tags_list.html', context={'tags': tags})


def create_tag(request):
    if request.method == 'GET':
        tag_form = TagModelForm()
        return render(request, 'tags/tag_create.html', context={'tag_form': tag_form})

    if request.method == 'POST':
        form_data = TagModelForm(request.POST)
        if form_data.is_valid():
            new_tag = form_data.save()
            return redirect(reverse('get_tag_page_url', kwargs={'slug': new_tag.tag}))

    return HttpResponse(status=405)


def update_tag(request, slug):
    if request.method == 'GET':
        tag = Tag.objects.get(tag__iexact=slug)
        tag_form = TagModelForm(instance=tag)
        return render(request, 'tags/tag_update.html', context={'tag_form': tag_form, 'slug': slug})

    if request.method == 'POST':
        tag = Tag.objects.get(tag=slug)
        form_data = TagModelForm(request.POST, instance=tag)
        if form_data.is_valid():
            new_tag = form_data.save()
            return redirect(reverse('get_tag_page_url', kwargs={'slug': new_tag.tag}))


def delete_tag(request, slug): ...
