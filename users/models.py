from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
