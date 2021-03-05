from rest_framework import serializers
from .models import Car, Booking
from django.contrib.auth.models import User
from home.serializers import CarparkSerializer

### This file defines the how models are serialized: choosing which fields are serialized, defining how the fields are serialized and finally defining/redefining serializer methods.  ### 


class CarSerializer(serializers.ModelSerializer): 
 # This defines the create method, where the serializer model creates a car object and then returns it 
  def create(self, validated_data):
    return Car.objects.create(**validated_data)

  # makes the model being serialized is the Car model and serializes all of the fields
  class Meta():
    model = Car
    fields = '__all__'


class BookingDetailSerializer(serializers.Serializer):
  car_number_plate = serializers.CharField(max_length = 7)
  carpark_id = serializers.CharField(max_length = 3)
  start_datetime = serializers.DateTimeField()
  end_datetime = serializers.DateTimeField()

class BookingSerializer(serializers.ModelSerializer):
  # makes the model being serialized is the Booking model and serializes all of the fields
  class Meta():
    model = Booking
    fields = '__all__'
