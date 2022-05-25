from django.db import models
from django.forms import CharField

# Create your models here.
class Entry(models.Model):
    datetime = models.DateTimeField()
    concept = models.CharField(max_length=30)
    amount = models.FloatField()
    
    