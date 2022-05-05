from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

class venue(models.Model):
    venuecode = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2)
    capacity = models.IntegerField()
    def __str__(self):
        return self.venuecode

class hkumember(models.Model):
    hkuid=models.BigIntegerField()
    name=models.CharField(max_length=150)
    def _str_(self):
        return f'{self.hkuid}'

class entryrecord(models.Model):
    hkuid = models.ManyToManyField(hkumember)    
    venuecode = models.ManyToManyField(venue)
    time = models.DateTimeField()
    status =  models.CharField(max_length=10)
    def _str_(self):
        return f'{self.hkuid}({self.time})'


class CustomUser(AbstractUser):
    is_device = models.BooleanField(default=False)
    is_taskforce = models.BooleanField(default=False)
    email = models.EmailField(unique=False, blank=True,null = True)
    first_name = models.CharField(max_length = 20, blank = True, null = True)
    last_name = models.CharField(max_length = 20, blank = True, null = True)
    # REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    def __str__(self):
        return "{}".format(self.username)