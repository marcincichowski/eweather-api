from rest_framework import serializers

from eweather_api_controller.models import User, Place, PlaceWeatherInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PlaceWeatherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceWeatherInfo
        fields = '__all__'
