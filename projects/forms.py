from .models import Project
from django import forms

class ProjectForm(forms.Form):
    title= forms.CharField(max_length=30, label='Title')
    description = forms.CharField(max_length=200)
    photo = forms.ImageField(label='Image')
    project = forms.URLField(label='Project Url')
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'photo', 'project')