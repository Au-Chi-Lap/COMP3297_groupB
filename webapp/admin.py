from django.contrib import admin

# Register your models here.
from . models import venue, hkumember

admin.site.register(venue)
admin.site.register(hkumember)