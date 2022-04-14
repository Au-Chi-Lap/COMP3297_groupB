from unicodedata import name
from django.db import models

class venue(models.Model):
    venuecode = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2)
    capacity = models.IntegerField()

class hkumember(models.Model):
    hkuid = models.CharField(max_length=10)
    name = models.CharField(max_length=150)   

def __str__(self):
    return self.venuecode

def __str__(self):
    return self.hkuid