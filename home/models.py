from django.db import models
from datetime import timedelta, datetime



def time_slot_default():
    no_slots = 24*4
    slot_length = timedelta(minutes=15)
    time_slot = dict()  

    for slot in range(0,no_slots):
        time_slot[((datetime(year=2020, month=1, day=1) + slot*slot_length).time()).isoformat()] = 0 
    return time_slot

class Carpark(models.Model):
    name = models.CharField(max_length = 20)
    total_places = models.SmallIntegerField()


class Carpark_Data(models.Model):
    date = models.DateField() 
    is_booking = models.BooleanField()
    carpark = models.ForeignKey('home.Carpark', on_delete = models.CASCADE)
    data =  models.JSONField(default = time_slot_default())

class Live_Feed(models.Model):
    timestamp = models.DateTimeField()
    car_number_plate = models.CharField(max_length = 7, default = None)
    carpark = models.IntegerField(default = None)

