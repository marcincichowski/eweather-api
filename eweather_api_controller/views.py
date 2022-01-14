from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from eweather_api_controller.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, PlaceSerializer


@api_view(['GET'])
def list_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("success")


@api_view(['GET'])
def list_places(request):
    place = Place.objects.all()
    serializer = PlaceSerializer(place, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_user_places(request, pk):
    place = Place.objects.filter(owner=pk)
    serializer = PlaceSerializer(place, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_place(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_place(request, pk):
    place = Place.objects.get(id=pk)
    serializer = PlaceSerializer(instance=place, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_place(request, pk):
    place = Place.objects.get(id=pk)
    place.delete()
    return Response("success")


@api_view(['GET'])
def get_active_user(request):
    user = User.objects.get(active=True)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def set_active_user(request, pk):
    user = User.objects.get(id=pk)
    last_user = User.objects.get(active=True)
    last_user.active = False
    user.active = True
    serializer = UserSerializer(instance=user)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)