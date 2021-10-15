from django import forms
from django.contrib.auth.models import User
from insta.models import Comment, Image, Profile
from django.contrib.auth.forms import UserCreationForm


class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes','comments']

