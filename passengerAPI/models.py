from django.db import models


class Passenger(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=256, blank=False, unique=True)
    number = models.CharField(max_length=10, blank=False, unique=True)
    password = models.CharField(max_length=15, blank=False)


class PassengerHistory(models.Model):
    passenger = models.ForeignKey(
        Passenger, blank=False, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        'driverAPI.Driver', blank=False, on_delete=models.CASCADE)
    source_address = models.CharField(max_length=20, blank=False)
    destination_address = models.CharField(max_length=20, blank=False)
