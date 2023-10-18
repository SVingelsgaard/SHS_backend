from django.shortcuts import render
from .serializers import BusTimeSerializer
from .models import BusTime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper import run_scrape
from django.http import HttpResponse
from django.http import JsonResponse
import requests

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
    
def openDoorButton(request):
    if request.method == "POST":
        data = request.POST
        if "value" in data:
            # Perform any other actions you need here
            return JsonResponse({"status": "Success"})
        else:
            return JsonResponse({"status": "Error: Value not provided"}, status=400)

def openDoorEP(request):
    try:
        # Define the ESP URL (replace with your setup's URL)
        esp_url = "http://your_esp_external_address:your_port/openDoor"
        
        # Data to send
        data_to_send = {
            "opendoor": True
        }
        
        # Send POST request
        response = requests.post(esp_url, json=data_to_send)
        
        # Check if request was successful
        if response.status_code == 200:
            return JsonResponse({"status": "success", "message": "Request sent successfully!"})
        else:
            return JsonResponse({"status": "error", "message": f"ESP returned {response.status_code}: {response.text}"})
    except requests.ConnectionError:
        return JsonResponse({"status": "error", "message": "Failed to connect to ESP"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
    
