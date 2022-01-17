from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    login = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=False)
    username = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.username} {"[X]" if self.active else "[ ]"}'


class Place(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    lon = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('lat', 'lon', 'owner')

    def __str__(self):
        return f'{self.address} (Lat: {self.lat} Lon: {self.lon}) [{self.owner.username}]'


class PlaceWeatherInfo(models.Model):
    lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    lon = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    timestamp = models.DateTimeField(unique=True)
    temperature = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()

    class Meta:
        unique_together = ('lat', 'lon', 'timestamp')

    def __str__(self):
        return f'Lat: {self.lat} Lon: {self.lon} [{self.timestamp.strftime("%d.%m.%Y %H:%M")}]'
