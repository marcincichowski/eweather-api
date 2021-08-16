from django.db import models

class User(models.Model):
    login = models.CharField(max_length=30)
    last_request = models.DateField('last request')

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    class Meta:
        unique_together = ('lat', 'lon', 'user')
    def __str__(self):
        result = f"user: {self.user.id} \n " \
                 f"name: {self.name} \n" \
                 f"lat: {self.lat} " \
                 f"lon: {self.lon}"
        return result