from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from weatherApiMain.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, PlaceSerializer

@api_view(['GET'])
def listUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("success")

@api_view(['GET'])
def listPlaces(request):
    place = Place.objects.all()
    serializer = PlaceSerializer(place, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listUserPlaces(request, pk):
    place = Place.objects.filter(user=pk)
    serializer = PlaceSerializer(place, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPlace(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePlace(request, pk):
    place = Place.objects.get(id=pk)
    serializer = PlaceSerializer(instance=place, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePlace(request, pk):
    place = Place.objects.get(id=pk)
    place.delete()
    return Response("success")

@api_view(['GET'])
def getActiveUser(request):
    user = User.objects.get(active=True)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def setActiveUser(request, pk):
    user = User.objects.get(id=pk)
    last_user = User.objects.get(active=True)
    last_user.active = False
    user.active = True
    serializer = UserSerializer(instance=user)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
