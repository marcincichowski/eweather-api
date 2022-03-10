from django.db import models


class User(models.Model):
    login = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    username = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.username}[{self.id}] {"A" if self.active else "Ina"}ctive displaying'


class Place(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=30)

    class Meta:
        unique_together = ('lat', 'lon', 'owner')

    def __str__(self):
        return f'Lat: {self.lat} Lon: {self.lon} [Owner: {self.owner.id}\n]'


class PlaceWeatherInfo(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()

    class Meta:
        unique_together = ('lat', 'lon', 'timestamp')

    def __str__(self):
        return f'Lat: {self.lat} Lon: {self.lon} at {self.timestamp.now().strftime("%d/%m/%Y %H:%M:%S")}'
