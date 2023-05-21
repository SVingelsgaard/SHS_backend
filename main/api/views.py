from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from .serializers import BusTimeSerializer
from .models import BusTime
from rest_framework.decorators import api_view
from rest_framework.response import Response

def apiHomescreen(request):
    return render(request, "index.html")

@api_view(['GET'])
def getData(request):
    serializer = BusTimeSerializer(data=request.data, many=True)
    print('get triggerd')
    return Response({'name':'sigurd','age':20})
'''    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)'''
