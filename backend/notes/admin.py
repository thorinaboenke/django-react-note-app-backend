from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
  list = ('title', 'published')
  admin.site.register(Note)