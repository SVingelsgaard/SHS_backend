from django.urls import include, path
from . import views


urlpatterns = [
    path('bustimes/', views.getData),
    path('', views.apiHomescreen),
]