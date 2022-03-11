from django import forms
from django.core.exceptions import ValidationError

from eweather_api_controller.models import User


def check_char(char):
    if char=='A' or char=='a' or char=='B' or char=='b' or char=='C' or char=='c' or char=='D' or char=='d' or char=='E' or char=='e' or char=='F' or char=='f' or char=='1' or char=='2' or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char=='9' or char=='0':
        return True
    else:
        return False


def validate_mac(mac):
    first = True
    if len(mac) != 17:
        err = 'Błędna długość adresu! ' + str(len(mac))
        raise ValidationError(err)
    else:
        for counter, it in enumerate(mac):
            if first:
                if not check_char(it):
                    raise ValidationError('Wpisany adres posiada zabroniony symbol (' + it + ' znak numer ' + str(
                        counter + 1) + ')! Poprawny format: AA:BB:CC:DD:EE:FF ')
                first = False
            elif counter == 2 or counter == 5 or counter == 8 or counter == 11 or counter == 14:
                if it != ':':
                    raise ValidationError('Wpisany adres posiada zabroniony symbol (' + it + ' znak numer ' + str(
                        counter + 1) + ')! Poprawny format: AA:BB:CC:DD:EE:FF ')
            elif not check_char(it):
                raise ValidationError('Wpisany adres posiada zabroniony symbol (' + it + ' znak numer ' + str(counter+1) + ')! Poprawny format: AA:BB:CC:DD:EE:FF ')


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username

class addProfileForm(forms.Form):
    login = forms.CharField(label='login', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    username = forms.CharField(label='Nazwa profilu', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))


class addPlaceForm(forms.Form):
    name = forms.CharField(label='Nazwa', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    owner = CustomModelChoiceField(required=True, queryset=User.objects.all(), empty_label="Wybierz", widget=forms.Select(attrs={'class': 'select'}))
    lat = forms.FloatField(required=True, widget=forms.HiddenInput())
    lon = forms.FloatField(required=True, widget=forms.HiddenInput())


class addDeviceForm(forms.Form):
    name = forms.CharField(label='Nazwa', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    mac = forms.CharField(label='Adres MAC', max_length=17, validators=[validate_mac], widget=forms.TextInput(attrs={'class': 'input'}))
