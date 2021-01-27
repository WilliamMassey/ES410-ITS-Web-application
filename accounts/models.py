from django.db import models
from django.contrib.auth.models import auth
from datetime import datetime, timezone, timedelta, time, date
from home.models import Carpark
# Create your models here.

# extending user 
class Details(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default = None)
    free_parking = models.BooleanField(default = False)

class Car(models.Model):
    CAR_COLOURS = (
        ('b', 'BLUE'),
        ('r', 'RED'),
        ('g', 'GREEN'),
        ('y', 'YELLOW'),
        ('o', 'ORANGE'),
        ('s', 'BLACK'),
        ('n', 'BROWN'),
        ('w', 'WHITE')
    )
    car_number_plate = models.CharField(max_length = 8, primary_key = True, default = None)
    colour = models.CharField(max_length = 1, default = 's', choices = CAR_COLOURS)
    manufacturer = models.CharField(max_length = 20, default = None)

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default = None)
    car = models.ForeignKey(Car, on_delete = models.CASCADE, default = None)
    start_datetime = models.DateTimeField(default = datetime(2020,12,31,12,0))
    end_datetime = models.DateTimeField(default = datetime(2020,12,31,13,0))
    carpark = models.ForeignKey('home.Carpark', on_delete = models.CASCADE, default = None)
  
class User_Car_Mapping(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default = None)
    car =  models.ForeignKey(Car, on_delete=models.CASCADE, default = None)

def time_slot_default():
    no_slots = 24*4
    slot_length = timedelta(minutes=15)
    time_slot = dict()

    for slot in range(0,no_slots):
        time_slot[((datetime(year=2020, month=1, day=1) + slot*slot_length).time()).isoformat()] = 0
    return time_slot

class Booking_data(models.Model):
    #Desired result would be to use date and carpark as a composite pimary key i.e. booking data could be found by day and by carpark without copies.
    date = models.DateField()
    carpark = models.ForeignKey('home.Carpark', on_delete = models.CASCADE)
    time_slots =  models.JSONField(default = time_slot_default())
