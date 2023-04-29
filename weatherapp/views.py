import json
from django.shortcuts import render
import requests
from django.http import JsonResponse
import time

def get_weather(request):
    #city = 'Hyderabad'
    city = request.GET.get('city')
    api_key = 'ac1788d9018df65b83fbc8a4e0db0fe5'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    weather_data = {
        'city': city,
        'description': response['weather'][0]['description'],
        'temperature': response['main']['temp'],
        'humidity': response['main']['humidity'],
        'windspeed': response['wind']['speed'],
        'winddirection': response['wind']['deg'],
        'pressure': response['main']['pressure'],
    
    }
    

    
    return JsonResponse(weather_data)
