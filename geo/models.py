from django.db import models


class Geolocation(models.Model):
    ip = models.CharField(max_length=50, unique=True)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)


    def __str__(self):
        return self.ip
