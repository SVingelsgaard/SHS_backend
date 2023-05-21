from rest_framework import serializers
from .models import BusTime


class BusTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTime
        fields = ['location', 'destination', 'bus_number', 'times']