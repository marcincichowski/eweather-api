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

    class Meta:
        unique_together = ('lat', 'lon', 'owner')

    def __str__(self):
        return f'Lat: {self.lat} Lon: {self.lon} [Owner: {self.owner.id}\n]' \
