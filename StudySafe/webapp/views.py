from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from . models import entryrecord, venue, hkumember
from . serializers import entrySerializer, venueSerializer, hkumemberSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class venueList(generics.ListAPIView):
    queryset = venue.objects.all()
    serializer_class = venueSerializer
    filterset_fields = ('id',)


class hkumemberList(generics.ListAPIView):
    
    queryset = hkumember.objects.all()
    serializer_class = hkumemberSerializer
    filterset_fields = ('hkuid',)

         
class entryFilter(django_filters.FilterSet):
    time=django_filters.DateTimeFromToRangeFilter()
    
    class Meta:
        model=entryrecord
        fields=('time','hkuid',)

class entryList(generics.ListAPIView):
    queryset = entryrecord.objects.all()
    serializer_class = entrySerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = entryFilter
    ordering_fields = ['time']

