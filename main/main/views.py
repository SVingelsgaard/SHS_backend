from django.shortcuts import render, redirect

def Homescreen(request):
    return render(request, "main/templates/homescreen.html")