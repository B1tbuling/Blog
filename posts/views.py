from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse


def post_like(request, pk):
    PostLike(post_id=pk, user_id=request.user.id).save()
    return HttpResponse(200)


def comment_like(request, pk, id_comm):
    CommentLike(comment_id=id_comm, user_id=request.user.id).save()
    return HttpResponse(200)


def add_comment(request, pk):
    # Как-то понять, что пользователь аутефицирован
    Comments.objects.create(text=request.POST['text'], user_id=request.user.id, post_id=pk).save()
    return redirect(reverse('get_post_page_url', kwargs={'pk': pk}))


def update_comment(request, id_comm):
    comment = Comments.objects.get(id=id_comm)
    comment_form = CommentForm(request.POST, instance=comment)
    if comment_form.is_valid():
        comment_form.save()
        return redirect(reverse('get_post_page_url', kwargs={'pk': comment.post.id}))
    return HttpResponse(422)


def delete_comment(request, id_comm):
    comment = Comments.objects.get(id=id_comm)
    pk = comment.post.id
    comment.delete()
    return redirect(reverse('get_post_page_url', kwargs={'pk': pk}))


def get_post_page(request, pk):
    comments_dict = []
    form = CommentForm
    post = Posts.objects.get(id=pk)
    tags = post.tags.all()
    comments = post.comments_set.all()
    amount_like_post = len(PostLike.objects.filter(post_id=pk))
    for comment in comments:
        amount_like_comment = len(CommentLike.objects.filter(comment_id=comment))
        comments_dict.append({'form_update': CommentForm(instance=comment), 'comment': comment, 'amount_like_comment': amount_like_comment})
    return render(
                request,
                'posts/post_page.html',
                context={'post': post,
                         'tags': tags,
                         'comments': comments_dict,
                         'form_comment': form,
                         'amount_like_post': amount_like_post
                         }
                )


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
            post.user_id = request.user.id
            post.save()
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


def delete_post(request, pk):
    post = Posts.objects.get(id=pk)
    post.delete()
    return redirect(reverse('get_posts_list_url'))


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


def delete_tag(request, slug):
    tag = Tag.objects.get(tag=slug)
    tag.delete()
    return redirect(reverse('get_tags_list_url'))

