from .models import Project,Profile
from django import forms

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'photo', 'project')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("picture", "bio", "contact",)        