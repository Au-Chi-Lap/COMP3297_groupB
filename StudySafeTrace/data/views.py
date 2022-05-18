from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import timedelta, datetime, date
import requests
import json
from .forms import InputForm


# Create your views here.
# diagdate =  datetime(2022,5,5)
# hkuid= 3025704501
def vInput(request):
    if request.method == 'POST':
        form=InputForm(request.POST)
        if form.is_valid():
            request.session['hkuid'] = request.POST['hkuid']
            request.session['date'] = request.POST['date']
            return redirect('https://enigmatic-coast-62798.herokuapp.com/data/venues')
    else:
        form=InputForm()
    return render(request,'input.html',{'form':form})

def cInput(request):
    if request.method == 'POST':
        form=InputForm(request.POST)
        if form.is_valid():
            request.session['hkuid'] = request.POST['hkuid']
            request.session['date'] = request.POST['date']
            return redirect('https://enigmatic-coast-62798.herokuapp.com/data/contacts')
    else:
        form=InputForm()
    return render(request,'input.html',{'form':form})

# diagdate = input['diagdate']
# hkuid= 3025704501

def venues(request):
    hkuid = int(request.session.get('hkuid'))
    diagdate= datetime.strptime(request.session.get('date'),"%Y-%m-%d")
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
    hkuid = int(request.session.get('hkuid'))
    diagdate= datetime.strptime(request.session.get('date'),"%Y-%m-%d")
    context = {
        'subject':hkuid,
        'date': diagdate.date(),
        'contacts':[]
    }

    payload = {
            'hkuid':hkuid
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

    contactlist=[]
    for x in range(len(entry_data)):
        if (entry_data[x]['status']=="Exit"):
            continue
        entry = datetime.strptime(entry_data[x]['time'], "%Y-%m-%dT%H:%M:%S%z")
        exit = datetime.strptime(entry_data[x+1]['time'], "%Y-%m-%dT%H:%M:%S%z")
        if (exit-entry) >= timedelta(minutes=30):
            entryPayload2={
            'time_after':str(entry),
            'time_before':str(exit),
            'ordering':'time'
            }
            entry2_response = requests.get("https://young-lowlands-48457.herokuapp.com/entry", params=entryPayload2)
            entry2_data = entry2_response.json()

            if (len(entry2_data) == 0):
                print("No close contact found betwenn: ",str(entry)," ",str(exit))
            else:
                for y in range(len(entry2_data)):
                    if(entry2_data[y]['hkuid']==infectedID):
                        continue
                    elif (entry2_data[y]['status']=="Exit"):
                        continue
                    elif(entry2_data[y]['venuecode']!=entry_data[x]['venuecode']):
                        continue
                    else:
                        entrytime = datetime.strptime(entry2_data[y]['time'], "%Y-%m-%dT%H:%M:%S%z")
                        tmpID=entry2_data[y]['hkuid']
                        for i in range(y+1,len(entry2_data)):
                            if (entry2_data[i]['hkuid']==tmpID) and (entry2_data[i]["status"]=="Exit"):
                                exittime = datetime.strptime(entry2_data[i]['time'], "%Y-%m-%dT%H:%M:%S%z")
                                print("entry: ",entrytime)
                                print("exit: ", exittime)
                                
                                if (exittime-entrytime) >= timedelta(minutes=30):
                                    contactlist.append(entry2_data[i]['hkuid'])
                                    break


    contactlist=list(set(contactlist))
    contact_response=requests.get("https://young-lowlands-48457.herokuapp.com/hkumember")
    print("venue response status: ", contact_response.status_code)
    if (contact_response.status_code != 200):
        return

    contact_data = contact_response.json()

    if (len(contact_data) == 0):
        print("No matching venue found!")
        return

    for x in contactlist:
        context['contacts'].append(str(contact_data[x-1]['hkuid']))
        context['contacts'].sort()


    return render(request, 'contacts.html', context=context)


# for testing
# def venues(request):
#     return HttpResponse('oh wow a venue')

# def contacts(request):
#     return HttpResponse('oh wow a contact')
