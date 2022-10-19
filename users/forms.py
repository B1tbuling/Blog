from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Enter password')
    password2 = forms.CharField(label='Enter again password')
