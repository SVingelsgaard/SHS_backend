from django.shortcuts import render
from .serializers import BusTimeSerializer
from .models import BusTime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper import run_scrape
from django.http import HttpResponse
from django.http import JsonResponse

def apiHomescreen(request):
    return render(request, "api/templates/api_homescreen.html")
 
@api_view(['GET'])
def getBustimes(request):
    bustime = run_scrape()
    serializer = BusTimeSerializer(data=bustime, many=False)
    
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    
def one_or_zero(request):
    # You can define your logic to determine the value (1 or 0) here.
    value = 1  # Replace with your logic

    return JsonResponse({'result': value})
