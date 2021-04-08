from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
# Create your models here.

class Project(models.Model):
    project = models.URLField()
    description = models.TextField()
    photo = CloudinaryField('photo')
    title = models.CharField(max_length=200)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
        
    def __str__(self):
        return self.projects

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('picture')
    bio = models.CharField(max_length=256)
    projects = models.ForeignKey(Project,on_delete=models.CASCADE)
    contact = models.EmailField()

    def __str__(self):
        return self.user
