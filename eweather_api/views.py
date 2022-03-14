from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from eweather_api.forms import addProfileForm, addPlaceForm, addDeviceForm
from eweather_api_controller.models import User, Place, Device


@login_required(login_url='/auth')
def index(request):
    return render(request, 'eweather/index.html')

def auth(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect(index)
            else:
                return render(request, 'eweather/auth.html', context={'error': 'Podano nieprawidłowy login lub hasło!'})
        else:
            return render(request, 'eweather/auth.html', context={'error': 'Błąd żądania!'})
    else:
        return render(request, 'eweather/auth.html')


def logout_view(request):
    logout(request)
    return redirect('/auth', context={'error': 'Pomyślnie Wylogowano!'})


@login_required(login_url='/auth')
def profiles(request):
    profiles = User.objects.all()
    return render(request, 'eweather/profiles.html', context={'profiles': profiles})


@login_required(login_url='/auth')
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


@login_required(login_url='/auth')
def places(request):
    places = Place.objects.all()
    return render(request, 'eweather/places.html', context={'places': places})

@login_required(login_url='/auth')
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


@login_required(login_url='/auth')
def devices(request):
    devices = Device.objects.all()
    return render(request, 'eweather/devices.html', context={'devices': devices})


@login_required(login_url='/auth')
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