from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import date, timedelta
import requests
import json
import urllib

# Create your views here.


def venues(request):

    payload = urllib.parse.urlencode(
        {"q": json.dumps({"resource": "https://young-lowlands-48457.herokuapp.com/venue"})})
    venues_response = requests.get(
        "https://young-lowlands-48457.herokuapp.com/venue", params=payload)

    print("Venues response status: ", venues_response.status_code)
    if (venues_response.status_code != 200):
        return

    venues_data = venues_response.json()

    if (len(venues_data) == 0):
        print("No venues data found!")
        return

    context = {"venues": venues_data}

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
