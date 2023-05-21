from django.urls import include, path
from . import views

urlpatterns = [
    path('bustimes/', views.getBustimes),
    path('', views.apiHomescreen, name='apiHomescreen'),
]