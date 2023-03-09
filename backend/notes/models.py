from django.db import models

# Create your models here.
class Note(models.Model):
   text = models.CharField(max_length=140)
   published = models.DateTimeField(auto_now_add=True)
   
# default attribute to be displayed
   def _str_(self):
     return self.text