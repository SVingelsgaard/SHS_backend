from django.urls import include, path
from . import views

urlpatterns = [
    path('bustimes/', views.getBustimes),
    path('openDoorButton/', views.openDoorButton, name='openDoorButton'),
    path('openDoorMCEndpoint/', views.openDoorMCEndpoint, name='openDoorMCEndpoint'),
    path('', views.apiHomescreen, name='apiHomescreen'),
]