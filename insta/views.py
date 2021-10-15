from django.shortcuts import render,redirect
from insta.models import Comment, Image, Profile
from insta.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
# Create your views here.
def display_home(request):
    return render(request, "index.html",)




