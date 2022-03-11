from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from eweather_api.forms import addProfileForm, addPlaceForm, addDeviceForm
from eweather_api_controller.models import User, Place, Device


def index(request):

    return render(request, 'eweather/index.html')

def auth(request):

    return render(request, 'auth.html')

def profiles(request):
    profiles = User.objects.all()
    return render(request, 'eweather/profiles.html', context={'profiles': profiles})

def add_profile(request):
    if request.method == 'POST':
        form = addProfileForm(request.POST)
        if form.is_valid():
            user = User(login=form.cleaned_data['login'], username=form.cleaned_data['username'])
            user.save()
            return redirect('profiles')
        else:
            return render(request, 'eweather/add_profile.html', context={'form': form})
    else:
        form = addProfileForm()
        return render(request, 'eweather/add_profile.html', context={'form': form})

def settings(request):

    return render(request, 'eweather/settings.html')


def places(request):
    places = Place.objects.all()
    return render(request, 'eweather/places.html', context={'places': places})

def add_place(request):
    if request.method == 'POST':
        form = addPlaceForm(request.POST)
        if form.is_valid():
            place = Place(name=form.cleaned_data['name'], owner=form.cleaned_data['owner'], lat=form.cleaned_data['lat'], lon=form.cleaned_data['lon'])
            place.save()
            return redirect('places')
        else:
            return render(request, 'eweather/add_place.html', context={'form': form})
    else:
        form = addPlaceForm()
        return render(request, 'eweather/add_place.html', context={'form': form})


def devices(request):
    devices = Device.objects.all()
    return render(request, 'eweather/devices.html', context={'devices': devices})

def add_device(request):
    if request.method == 'POST':
        form = addDeviceForm(request.POST)
        if form.is_valid():
            place = Device(name=form.cleaned_data['name'], mac=form.cleaned_data['mac'])
            place.save()
            return redirect('devices')
        else:
            return render(request, 'eweather/add_device.html', context={'form': form})
    else:
        form = addDeviceForm()
        return render(request, 'eweather/add_device.html', context={'form': form})