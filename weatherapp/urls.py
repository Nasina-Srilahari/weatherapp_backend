from django.urls import path
from . import views

urlpatterns = [
    path('api/weather', views.get_weather, name='get_weather'),
]