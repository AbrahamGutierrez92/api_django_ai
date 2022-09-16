from dataclasses import field
from rest_framework import serializers
from .models import Project

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'tecnologia', 'created_at')
        read_only_field = ('created_at',)