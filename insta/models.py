from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    

    def __str__(self):
        return f'{self.user.user} Image'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)
    
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



class Image(models.Model):
    image_name = models.CharField(max_length=80,blank=True)
    image_caption = models.CharField(max_length=600)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        return self.save()
    
    def delete_image(self):
        return self.delete()

    @classmethod
    def search_post(cls, name):
        return cls.objects.filter(image_name__image__name__icontains=name)
    
    @classmethod
    def get_picture_by_id(cls, picture_id):
        picture = cls.objects.get(id=picture_id)
        return picture
        
    def add_likes(self):
        return self.likes.count()


class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return f'{self.user.user} Image'

    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()
