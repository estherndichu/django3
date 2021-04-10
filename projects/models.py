from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
# Create your models here.   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=256)
    contact = models.EmailField()
                                            
    def __str__(self):
        return f'{self.user.username} Profile'

def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)

class Project(models.Model):
    project = models.URLField(max_length=120, default='website-url')
    description = models.TextField()
    photo = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        
    def __str__(self):
        return self.title

    def save_project(self):
        self.save()     

    def delete_project(self):
        self.delete()  


class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project} Rating'