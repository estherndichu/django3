from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Project, Profile
from .forms import ProjectForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer,ProfileSerializer

# Create your views here.
@login_required
def index(request):
    projects = Project.objects.all()[::-1]

    return render(request,'projects/index.html', {'projects':projects})

def post(request):  
    current_user = request.user

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            post.user = request.user
            projects.save()
            return HttpResponseRedirect('/')
    else:
        form = ProjectForm()  

    form = ProjectForm()
    return render(request,'projects/post.html', {'form':form})   

class ProjectList(APIView):
    def get(self, request, form=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)     
    
class ProfileList(APIView):
    def get(self,request, format=None):
        all_profiles= Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)