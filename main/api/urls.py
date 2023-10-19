from django.urls import include, path
from . import views

urlpatterns = [ 
    path('bustimes/', views.getBustimes),
    path('openDoor/', views.openDoorEP, name='openDoorEP'),
    path('', views.apiHomescreen, name='apiHomescreen'),
]