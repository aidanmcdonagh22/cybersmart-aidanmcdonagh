from requests import request
from .models import Todo
from django.conf import settings

class Weather():
        
    def getWeather(pk):
        todoObj = Todo.objects.filter(pk=pk)
        resp = request(f"api.openweathermap.org/data/2.5/weather?q={object}&appid={settings.WEATHER_API_KEY}")