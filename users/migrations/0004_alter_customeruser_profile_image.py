# Generated by Django 4.1.1 on 2022-10-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customeruser_image_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
