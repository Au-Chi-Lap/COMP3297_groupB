from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import date,timedelta
import requests
import json

# Create your views here.
def venues(request):

    context={

    }

    return render(request, 'venues.html', context=context)

def contacts(request):

    context = {

    }

    return render(request, 'contacts.html', context=context)


# for testing
# def venues(request):
#     return HttpResponse('oh wow a venue')

# def contacts(request):
#     return HttpResponse('oh wow a contact')
