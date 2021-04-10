from .models import Project,Profile, Rating
from django import forms

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'photo', 'project')

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("picture", "bio", "contact",)        

class RatingsForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']      