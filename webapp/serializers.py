from dataclasses import field
from rest_framework import serializers
from . models import venue, hkumember

class venueSerializer(serializers.ModelSerializer):
    class Meta:
        model = venue
        fields= '__all__'

class hkumemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = hkumember
        fields= '__all__'