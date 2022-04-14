from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import venue
from . models import hkumember
from . serializers import venueSerializer
from . serializers import hkumemberSerializer

class venueList(APIView):

    def get(self,request):
        venue1 = venue.objects.all()
        serializer = venueSerializer(venue1, many=True)
        return Response(serializer.data)
    def post(self):
        pass 

class hkumemberList(APIView):

    def get(self,request):
        hkumember1 = hkumember.objects.all()
        serializer = hkumemberSerializer(hkumember1, many=True)
        return Response(serializer.data)
    def post(self):
        pass 