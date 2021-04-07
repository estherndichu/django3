from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.

class Projects(models.Model):
    projects = models.URLField()

    def __str__(self):
        return self.projects

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('picture')
    bio = models.CharField()
    projects = models.ForeignKey(Projects,on_delete=models.CASCADE)
    contact = models.EmailField()

    def __str__(self):
        return self.user

def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)        