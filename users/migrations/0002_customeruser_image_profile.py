# Generated by Django 4.1.1 on 2022-10-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
