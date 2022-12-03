from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from .models import *
from users.models import CustomerUser


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email')

    class Meta:
        model = CustomerUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'profile_image']


class ProfilePhotoUserForm(forms.ModelForm):

    class Meta:
        model = CustomerUser
        fields = ['profile_image']

        widgets = {
            'profile_image': forms.FileInput(attrs={'id': 'input_photo_profile'})
        }


class ProfileDataUserForm(forms.ModelForm):

    class Meta:
        model = CustomerUser
        fields = ['first_name', 'last_name', 'birth_date', 'profile_status']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'data'}),
            'profile_status': forms.TextInput(attrs={'class': 'form-control'})
        }



