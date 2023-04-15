from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower


class User(AbstractUser):
    pass

class Car(models.Model):
    producer = models.CharField(max_length=128, unique=True)
    country_of_origin = models.CharField(max_length=128, blank=True, null=True)
    year_of_production = models.PositiveIntegerField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='cars', through='UserCars')
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)

    class Meta:
        ordering = [Lower('producer')]

class UserCars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']

