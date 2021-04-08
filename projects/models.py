from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
# Create your models here.

class Project(models.Model):
    project = models.URLField(max_length=120, default='website-url')
    description = models.TextField()
    photo = CloudinaryField('photo')
    title = models.CharField(max_length=200)
        
    def __str__(self):
        return self.project

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('picture')
    bio = models.CharField(max_length=256)
    contact = models.EmailField()

    def __str__(self):
        return self.user

def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)

