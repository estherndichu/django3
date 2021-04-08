from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Project, Profile
from .forms import ProjectForm

# Create your views here.
@login_required
def index(request):
    projects = Project.objects.all()[::-1]

    return render(request,'projects/index.html', {'projects':projects})

def post(request):  
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            projects = form.save(commit=False)
            post.user = request.user
            projects.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ProjectForm()  

    return render(request,'projects/post.html', {'form':form})    