from django.shortcuts import render
from .serializers import BusTimeSerializer
from .models import BusTime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper import run_scrape
from django.http import HttpResponse
import json
import urllib.request
from django.http import JsonResponse
import os

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
    

def openDoorEP(request):
    esp_url = os.environ.get('ESP_EP')
    
    if not esp_url:
        return JsonResponse({"status": "error", "message": "ESP endpoint not configured!"})
    
    data_to_send = {
        "opendoor": True
    }
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        json_data = json.dumps(data_to_send).encode('utf-8')
        req = urllib.request.Request(esp_url, data=json_data, headers=headers)
        response = urllib.request.urlopen(req)
        response_data = response.read().decode()
        
        # Here you may want to further process the response_data if needed

        if response.status == 200:
            return JsonResponse({"status": "success", "message": "Request sent successfully!"})
        else:
            return JsonResponse({"status": "error", "message": f"ESP returned {response.status}: {response_data}"})

    except urllib.error.URLError as e:
        return JsonResponse({"status": "error", "message": "Failed to connect to ESP. Error: " + str(e)})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
    
