from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Project, Profile, Rating
from .forms import ProjectForm,ProfileForm, RatingsForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer,ProfileSerializer

# Create your views here.
def index(request):
    projects = Project.objects.all()[::-1]

    return render(request,'projects/index.html', {'projects':projects})

@login_required(login_url='login')
def project(request, id):
    project = Project.objects.get(id=id)
    ratings = Rating.objects.filter(user=request.user, project=project).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_ratings = Rating.objects.filter(project=project)

            design_ratings = [d.design for d in project_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in project_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in project_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'project': project,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'projects/project.html', params)    

@login_required
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

@login_required
def update_profile(request):
    current_user_id = request.user.id
    user_profile = Profile.objects.get(user_id=current_user_id)
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid(): 

            user_profile.photo = form.cleaned_data.get('photo')
            user_profile.contact = form.cleaned_data.get('contact')
            user_profile.bio = form.cleaned_data.get('bio')

            user_profile.save()
        return redirect(profile)

    else:
        form = ProfileForm()
    return render(request, 'projects/update_profile.html', {"form": form})    

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user_id = request.user.id
    user_profile = Profile.objects.get(user_id=current_user_id)
    
    try:
        profile = Profile.objects.get(user_id=current_user_id)
    except Profile.DoesNotExist:
        return redirect(update_profile)
    projects = Project.objects.filter(id=current_user_id)
    

    return render(request, 'projects/profile.html', { "projects": projects, "user_profile": user_profile},)


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