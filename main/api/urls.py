from django.urls import include, path
from . import views

urlpatterns = [
    path('bustimes/', views.getBustimes),
    path('one_or_zero/', views.one_or_zero, name='one_or_zero'),
    path('', views.apiHomescreen, name='apiHomescreen'),
]