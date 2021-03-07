from django.db import models

# Create your models here.

class Carpark(models.Model):
    name = models.CharField(max_length = 20)
    total_places = models.SmallIntegerField()

# carpark_data stores the booking or occupancy data for a specific day at a carpark
class carpark_data(models.Model):
    date = models.DateField() 
    is_booking = models.BooleanField() # if True is booking data, if False is occupancy 
    carpark = models.ForeignKey('home.Carpark', on_delete = models.CASCADE)
    data =  models.JSONField(default = time_slot_default()) # sets default data to be a dictionary using time_slot_default as explained in func.py

class Live_Feed(models.Model):
    timestamp = models.DateTimeField()
    car_number_plate = models.CharField(max_length = 7, default = None)
    carpark = models.IntegerField(default = None)

