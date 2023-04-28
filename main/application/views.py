from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import BusTimeSerializer
from .models import BusTime


class BusTimesViewSet(viewsets.ModelViewSet):
    serializer_class = BusTimeSerializer
    queryset = BusTime.objects.all()

    