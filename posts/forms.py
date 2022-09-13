from django.forms import ModelForm
from django import forms
from .models import *


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'text']


class TagModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']

