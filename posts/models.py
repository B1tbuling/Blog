from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from users.models import CustomerUser


class Posts(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=70)
    text = models.TextField(blank=True)
    header_color = models.CharField(default='dark', max_length=30)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, default=15)
    amount_likes = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    class Meta:
        db_table = "posts_list"

    def get_absolute_url(self):
        return reverse('get_post_page_url', kwargs={'pk': self.id})


class Tag(models.Model):
    tag = models.SlugField(max_length=40, unique=True)
    # posts = models.ManyToManyField('Posts', blank=True, related_name='tags')

    class Meta:
        db_table = "tag_list"

    def get_absolute_url(self):
        return reverse('get_post_page_url', kwargs={'slug': self.tag})

    def __str__(self):
        return f'#{self.tag}'


class Comments(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    amount_likes = models.IntegerField(default=0)
    date_create = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"


class CommentLike(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments_likes"


class PostLike(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts_likes"


class ImagesPost(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "images_post"

