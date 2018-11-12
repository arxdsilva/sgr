from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
