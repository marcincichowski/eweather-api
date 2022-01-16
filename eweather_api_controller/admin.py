from django.contrib import admin
from eweather_api_controller.models import User, Place, PlaceWeatherInfo

admin.site.register(User)
admin.site.register(Place)
admin.site.register(PlaceWeatherInfo)
