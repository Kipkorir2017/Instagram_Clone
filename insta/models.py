from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    

class Image(models.Model):
    image_name = models.CharField(max_length=80,blank=True)
    image_caption = models.CharField(max_length=600)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)


class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
 
