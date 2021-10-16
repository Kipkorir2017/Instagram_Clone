from django.shortcuts import render,redirect,get_object_or_404
from insta.models import Comment, Image, Profile
from insta.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def display_home(request):

    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()
    return render(request,'index.html',{"posts":posts,"profile":profile,"comment":comment})




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

    return render(request, 'newpost.html')

@login_required(login_url='/accounts/login/')
def add_comment(request,id):
    post_comment = Comment.objects.filter(post= id)
    images = Image.objects.filter(id=id).all()
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request,'comments.html',{"form":form,"images":images,"comments":post_comment})

def show_profile(request):
    current_user= request.user
    images= Image.objects.filter(profile=current_user.id).all

    return render(request, 'registration/profile.html',{"images":images} )



def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")

        print(user)
        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'search.html',{'profiles': results,'message': message})
    else:
        message = "You haven't searched for anything,try again"
    return render(request, 'search.html', {'message': message})
