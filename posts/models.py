from django.db import models
from django.shortcuts import reverse


class Posts(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=70)
    text = models.TextField(blank=True)
    header_color = models.CharField(default='dark', max_length=30)
    author = models.IntegerField(default=1)
    amount_likes = models.IntegerField(default=0)

    class Meta:
        db_table = "posts_list"

    def get_absolute_url(self):
        return reverse('get_post_page_url', kwargs={'pk': self.id})


class Tag(models.Model):
    tag = models.SlugField(max_length=40, unique=True)

    class Meta:
        db_table = "tag_list"
