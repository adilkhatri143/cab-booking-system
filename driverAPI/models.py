from django.db import models
from . import constants
from passengerAPI.models import Passenger


class Driver(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=256, blank=False, unique=True)
    number = models.CharField(max_length=10, blank=False, unique=True)
    password = models.CharField(max_length=15, blank=False)


class CarOwnedByDriver(models.Model):
    driver = models.ForeignKey(Driver, blank=False, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=15, blank=False, unique=True)
    license_number = models.CharField(max_length=15, blank=False, unique=True)
    status = models.CharField(
        max_length=10, blank=False, default=constants.FREE)


class DriverHistory(models.Model):
    driver = models.ForeignKey(Driver, blank=False, on_delete=models.CASCADE)
    passenger = models.ForeignKey(
        Passenger, blank=False, on_delete=models.CASCADE)
    source_address = models.CharField(max_length=20, blank=False)
    destination_address = models.CharField(max_length=20, blank=False)
