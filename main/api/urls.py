from django.urls import include, path
from . import views

urlpatterns = [ 
    path('bustimes/', views.getBustimes),
    path('openDoorButton/', views.openDoorButton, name='openDoorButton'),
    path('openDoor/', views.openDoorEP, name='openDoorEP'),
    path('', views.apiHomescreen, name='apiHomescreen'),
]