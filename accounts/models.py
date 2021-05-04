from django.db import models
from django.contrib.auth.models import auth
from datetime import datetime, timezone, timedelta, time, date
from home.models import Carpark

# Create your models here.

# Details model stores additional data regarding users not included in the default django user model
class Details(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default = None)
    free_parking = models.BooleanField(default = False) # defines the status whether they need to pay for parking 
    # Additional criteria/ status shall be added

# Car stores infromation regarding the cars
class Car(models.Model):

    CAR_COLOURS = (  # CAR_COLOURS reduces car colour into a single charater
        ('b', 'blue'),
        ('r', 'red'),
        ('g', 'green'),
        ('y', 'yellow'),
        ('o', 'orange'),
        ('s', 'black'),
        ('n', 'brown'),
        ('w', 'white')
    )
    colour = models.CharField(max_length = 1, default = 's', choices = CAR_COLOURS) 
    car_number_plate = models.CharField(max_length = 7, primary_key = True, default = None)# car number plate is unique so is used as primary key
    # following attributes are visual to aid the identification of the car
    
    manufacturer = models.CharField(max_length = 20, default = None)

# User_Car_Mapping (UCM) maps users to cars 
class User_Car_Mapping(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default = None)
    car =  models.ForeignKey(Car, on_delete=models.CASCADE, default = None)

# Booking model stores data regarding a booking 
class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default = None)# who has made the booking
    car = models.ForeignKey(Car, on_delete = models.CASCADE, default = None) # which car has the booking been made with
    start_datetime = models.DateTimeField(default = datetime(2020,12,31,12,0)) # the date and time of the start of the booking
    end_datetime = models.DateTimeField(default = datetime(2020,12,31,13,0)) # # the date and time of the end of the booking
    #carpark = models.ForeignKey('home.Carpark', on_delete = models.CASCADE, default = None) # which carpark the booking is 
  

