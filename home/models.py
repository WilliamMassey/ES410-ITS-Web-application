from django.db import models

# Create your models here.

# creates dictionary with a string key for every 15 min slot in the day, in the iso format (HH:MM:SS) and sets all of the values to 0 
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

# carpark_data stores the booking or occupancy data for a specific day at a carpark
class Carpark_Data(models.Model):
    date = models.DateField() 
    is_booking = models.BooleanField() # if True is booking data, if False is occupancy 
    carpark = models.ForeignKey('home.Carpark', on_delete = models.CASCADE)
    data =  models.JSONField(default = time_slot_default()) # sets default data to be a dictionary using time_slot_default as explained in func.py

class Live_Feed(models.Model):
    timestamp = models.DateTimeField()
    car_number_plate = models.CharField(max_length = 7, default = None)
    carpark = models.IntegerField(default = None)

