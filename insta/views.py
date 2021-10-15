from django.shortcuts import render,redirect
from insta.models import Comment, Image, Profile
from insta.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
# Create your views here.
def display_home(request):
    return render(request, "index.html",)




def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            caption=form.cleaned_data.get('caption')
            post = Image(image = image,image_caption= caption, image_profile=profile)
            post.save()  
        else:
            print(form.errors)
        return redirect('index')
    else:
        form = NewPostForm()

    return render(request, 'newpost.html', {"form": form})