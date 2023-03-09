from django.shortcuts import render
from .serializers import NoteSerializer 
from rest_framework import viewsets      
from .models import Note  

# Create your views here.

class NoteView(viewsets.ModelViewSet):  
    serializer_class = NoteSerializer   
    queryset = Note.objects.all() 