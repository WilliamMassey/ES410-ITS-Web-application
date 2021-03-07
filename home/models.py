from django.db import models

# Create your models here.

class Carpark(models.Model):
    name = models.CharField(max_length = 20)
    total_places = models.SmallIntegerField()

class Live_Feed(models.Model):
    timestamp = models.DateTimeField()
    car_number_plate = models.CharField(max_length = 7, default = None)
    carpark = models.IntegerField(default = None)
