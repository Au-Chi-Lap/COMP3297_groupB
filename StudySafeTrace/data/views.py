from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta, datetime, date
import requests
import json


# Create your views here.
diagdate =  datetime(2022,5,6)
hkuid= 3023776542

def venues(request):
    
    payload = {
        'hkuid':hkuid
    }
    context={
        'subject':hkuid,
        'date':diagdate.date(),
        "venues":[]
    }     
    hkumember_response = requests.get(
        "https://young-lowlands-48457.herokuapp.com/hkumember", params=payload)

    print("Hkumember response status: ", hkumember_response.status_code)
    if (hkumember_response.status_code != 200):
        return

    hkumember_data = hkumember_response.json()

    if (len(hkumember_data) == 0):
        print("No matching hkumember found!")
        return

    infectedID=hkumember_data[0]['id'] 
  
    entryPayload={
    'hkuid':infectedID,
    'time_after':str(diagdate-timedelta(days=2)),
    'time_before':str(diagdate+timedelta(days=1)),
    'ordering':'time'
    }
    entry_response = requests.get("https://young-lowlands-48457.herokuapp.com/entry", params=entryPayload)
    print("entry response status: ", entry_response.status_code)
    if (entry_response.status_code != 200):
        return

    entry_data = entry_response.json()

    if (len(entry_data) == 0):
        print("No matching entry/exit record found!")
        return

    venuelist=[]
    for x in range(len(entry_data)):
        if (entry_data[x]['status']=="Exit"):
            continue
        entry = datetime.strptime(entry_data[x]['time'], "%Y-%m-%dT%H:%M:%S%z")

        exit = datetime.strptime(entry_data[x+1]['time'], "%Y-%m-%dT%H:%M:%S%z")

        if (exit-entry) >= timedelta(minutes=30):

            venuelist.append(entry_data[x]['venuecode'])

    
    venue_response=requests.get("https://young-lowlands-48457.herokuapp.com/venue")
    print("venue response status: ", venue_response.status_code)
    if (venue_response.status_code != 200):
        return

    venue_data = venue_response.json()

    if (len(venue_data) == 0):
        print("No matching venue found!")
        return

    for x in venuelist:
        context['venues'].append(venue_data[x-1]['venuecode'])
    context['venues']=list(set(context['venues']))
    context['venues'].sort()
  
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
