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
    def post(self,request):
        data = {
            'venuecode': request.data.get('venuecode'),
            'location': request.data.get('location'),
            'type': request.data.get('type'),
            'capacity': request.data.get('capacity'),
        }
        serializer=venueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class hkumemberList(APIView):

    def get(self,request):
        hkumember1 = hkumember.objects.all()
        serializer = hkumemberSerializer(hkumember1, many=True)
        return Response(serializer.data)
    def post(self,request):
        data = {
            'hkuid': request.data.get('hkuid'),
            'name': request.data.get('name'),
        }
        serializer=hkumemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         