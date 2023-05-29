from django.shortcuts import render
from .serializers import BusTimeSerializer
from .models import BusTime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper import run_scrape
from django.http import HttpResponse

def apiHomescreen(request):
    return render(request, "api/templates/api_homescreen.html")
 
@api_view(['GET'])
def getBustimes(request):
    bustime = run_scrape()
    return (HttpResponse("test"))
    serializer = BusTimeSerializer(data=bustime, many=False)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
