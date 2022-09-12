from django.forms import ModelForm
from django import forms
from .models import *


class PostForm(forms.Form):
    # class Meta:
    #     model = Posts
    #     fields = ['title', 'text']

    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100)


        # widgets = {
        #     'title': forms.CharField(max_length=70),
        #     'text': forms.CharField(widget=forms.Textarea)
        # }
#
# class TestForm(forms.Form):
#     one = forms.CharField(disabled=True)
#     two = forms.IntegerField()
