# Generated by Django 4.1.1 on 2022-09-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_tag_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='posts.tag'),
        ),
    ]
