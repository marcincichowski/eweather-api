from django.db import models


class User(models.Model):
    login = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    username = models.CharField(max_length=30, null=True)


class Place(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        unique_together = ('lat', 'lon', 'owner')

    def __str__(self):
        result = f"user: {self.owner.id} \n " \
                 f"name: {self.address} \n" \
                 f"lat: {self.lat} " \
                 f"lon: {self.lon}"
        return result
