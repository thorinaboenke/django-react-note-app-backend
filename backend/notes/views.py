from django.shortcuts import render
from .serializers import NoteSerializer 
from rest_framework import viewsets      
from .models import Note  

# Create your views here.

class NoteView(viewsets.ModelViewSet):  
    serializer_class = NoteSerializer   
    queryset = Note.objects.all() 
    # excluding notes from the query if they contain 'bad words'
    # queryset = Note.objects.exclude(text__icontains='jar jar binks')

def note_view(request):
    return render(request, "notes/notes.html")