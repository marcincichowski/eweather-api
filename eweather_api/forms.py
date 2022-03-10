from django import forms

from eweather_api_controller.models import User


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class addProfileForm(forms.Form):
    login = forms.CharField(label='login', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    username = forms.CharField(label='Nazwa profilu', max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))


class addPlaceForm(forms.Form):
    owner = CustomModelChoiceField(required=True, queryset=User.objects.all(), empty_label="Wybierz", widget=forms.Select(attrs={'class': 'select'}))
    lat = forms.FloatField(required=True, widget=forms.HiddenInput())
    lon = forms.FloatField(required=True, widget=forms.HiddenInput())
