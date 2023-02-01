from django.shortcuts import render
from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.filter(active=True)
    serializer_class = StorySerializer
    http_method_names = ["get"]
