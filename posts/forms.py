from django.forms import ModelForm
from django import forms
from .models import *


class PostModelForm(forms.ModelForm):
    class Meta:
        image = forms.ImageField()
        model = Posts
        fields = ['title', 'text', 'tags']

        widgets = {
            'tags': forms.SelectMultiple(attrs={'class': 'form-select form-select-lg mb-3', 'style': 'width: 600px'})
        }


class ImagesForPostModelForm(forms.ModelForm):
    class Meta:
        model = ImagesPost
        fields = ['image']


class TagModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

        widgets = {
            'text': forms.TextInput()
        }
