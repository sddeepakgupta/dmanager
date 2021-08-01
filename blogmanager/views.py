from django.shortcuts import render
from blogmanager.models import Tutorial
from blogmanager.serializers import TutorialSerializer
from rest_framework import generics

# Create your views here.

class tutorialList(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
 
 
class tutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

