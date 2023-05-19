from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from .serializers import BusTimeSerializer
from .models import BusTime
from rest_framework.views import APIView
from rest_framework.response import Response


class BusTimesViewSet(viewsets.ModelViewSet):
    serializer_class = BusTimeSerializer
    queryset = BusTime.objects.all()
    basename = 'bustime'

class BusTimesView(APIView):
    def post(self, request):
        serializer = BusTimeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
def home(request):#test view
    return render(request, "home.html")