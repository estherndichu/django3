from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
@login_required
def index(request):
    
    return render(request,'projects/index.html',)