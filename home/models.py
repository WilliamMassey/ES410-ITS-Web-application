from django.db import models

# Create your models here.

class Carpark(models.Model):
    name = models.CharField(max_length = 20)
    total_places = models.SmallIntegerField()
    occupied_places = models.SmallIntegerField()
    booked_places = models.SmallIntegerField()

class Live_Feed(models.Model):
    time_stamp = models.DateTimeField()
    car_number_plate = models.ForeignKey('accounts.Car', on_delete = models.CASCADE)
    carpark = models.ForeignKey(Carpark, on_delete = models.CASCADE)