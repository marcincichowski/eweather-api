from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from eweather_api_controller.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, PlaceSerializer, PlaceWeatherInfoSerializer


def check_hardware_address(request):
    if 'Host' in request.headers:
        host = request.headers.get('Host')
        if host in settings.ALLOWED_HOSTS:
            return True
        else:
            if 'Hardware-Address' in request.headers:
                mac = request.headers.get('Hardware-Address')
                if mac is None:
                    return False

                print(f"Trying to Auth device with MAC:{mac}")
                device = Device.objects.get(mac=mac)
                if device:
                    return True
                else:
                    return False
            else:
                return False
    return False


@api_view(['GET'])
def list_users(request):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def update_user(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def delete_user(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        user = User.objects.get(id=pk)
        user.delete()
        return Response("success")


@api_view(['POST'])
def delete_device(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        device = Device.objects.get(id=pk)
        device.delete()
        return Response("success")


@api_view(['GET'])
def list_places(request):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        place = Place.objects.all()
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def list_user_places(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        place = Place.objects.filter(owner=pk)
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_place(request):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def update_place(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        place = Place.objects.get(id=pk)
        serializer = PlaceSerializer(instance=place, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def delete_place(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        place = Place.objects.get(id=pk)
        place.delete()
        return Response("success")


@api_view(['GET'])
def get_active_user(request):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        user = User.objects.get(active=True)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def set_active_user(request, pk):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        user = User.objects.get(id=pk)
        try:
            last_user = User.objects.get(active=True)
        except User.DoesNotExist:
            user.active = True
            user.save()
            serializer = UserSerializer(instance=user)
            return Response(serializer.data)
        else:
            if user != last_user:
                last_user.active = False
                user.active = True
                user.save()
                last_user.save()
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


@api_view(['POST'])
def post_place_weather(request):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        serializer = PlaceWeatherInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def get_place_weather(request, lat, lon, amount=300):
    if not check_hardware_address(request):
        return HttpResponse('Unauthorized', status=401)
    else:
        try:
            place_weather = PlaceWeatherInfo.objects.filter(lat=lat, lon=lon)[:amount:-1]
        except PlaceWeatherInfo.DoesNotExist:
            place_weather = PlaceWeatherInfo.objects.none()
        serializer = PlaceWeatherInfoSerializer(place_weather, many=True)
        return Response(serializer.data)
