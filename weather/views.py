from django.shortcuts import render
import urllib
import json


def index(request):
    city = request.POST.get("city")
    if request.method == "POST":
        city = city
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=3a833324b9650fb5ef8a769aa4f92093').read()
        api_url2 = json.loads(api_url)
        data = {
            "city": city,
            "weather_description":api_url2['weather'][0]['description'],
            "weather_temperature":api_url2['main']['temp'],
            "weather_pressure":api_url2['main']['pressure'],
            "weather_humidity":api_url2['main']['humidity'],
            "weather_icon":api_url2['weather'][0]['icon'],
        }
    else:
        data = {
            "city": None,
            "weather_description":None,
            "weather_temperature":None,
            "weather_pressure":None,
            "weather_humidity":None,
            "weather_icon":None,
        }
    context = {
        'data': data,
        'city': city,
    }
    return render(request, 'index.html',context)
    