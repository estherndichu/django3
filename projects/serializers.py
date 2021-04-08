from rest_framework import serializers
from .models import Project, Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'photo', 'project')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user','picture','bio','projects','contact')        