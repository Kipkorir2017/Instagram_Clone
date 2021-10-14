from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=80,blank=True)
    image_caption = models.CharField(max_length=600)
    profile = models.ForeignKey(on_delete = models.CASCADE)
    likes = models.ManyToManyField(related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)
    

 
