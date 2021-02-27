from rest_framework import serializers
from .models import Car, Booking
from django.contrib.auth.models import User
from home.serializers import CarparkSerializer


class UserSerializer(serializers.ModelSerializer):
 class Meta():
  model = User
  fields = ['username','first_name','last_name','email']


class CarSerializer(serializers.ModelSerializer): 
 def create(self, validated_data):
   return Car.objects.create(**validated_data)

 class Meta():
  model = Car
  fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
 class Meta():
  model = Booking
  fields = ['user', 'car', 'start_datetime', 'end_datetime', 'carpark']
 user = UserSerializer(required = False)
 car = CarSerializer()
 start_datetime = serializers.DateTimeField()
 end_datetime = serializers.DateTimeField()
 carpark = CarparkSerializer(required = False)
 



