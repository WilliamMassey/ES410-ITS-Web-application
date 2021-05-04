from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Car, Booking
from home.models import Carpark
from django.contrib.auth.models import User
from home.serializers import CarparkSerializer

### This file defines the how models are serialized: choosing which fields are serialized, defining how the fields are serialized and finally defining/redefining serializer methods.  ### 

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','username','password', 'first_name', 'last_name','email']
    extra_kwargs = {'password': {'write_only':True, 'required':True}}

  def create(self, validated_data):
    user  = User.objects.create_user(**validated_data)
    Token.objects.create(user = user)
    return user


class CarSerializer(serializers.ModelSerializer): 
 # This defines the create method, where the serializer model creates a car object and then returns it 
  def create(self, validated_data):
    return Car.objects.create(**validated_data)

  # makes the model being serialized is the Car model and serializes all of the fields
  class Meta():
    model = Car
    fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
  # makes the model being serialized is the Booking model and serializes all of the fields
  class Meta():
    model = Booking
    fields = '__all__'

class CarparkSerializer(serializers.ModelSerializer):
  # makes the model being serialized is the Booking model and serializes all of the fields
  class Meta():
    model = Carpark
    fields = '__all__'

