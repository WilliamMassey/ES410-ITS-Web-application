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


class BookingDetailSerializer(serializers.Serializer):
  car_number_plate = serializers.CharField(max_length = 7)
  carpark_id = serializers.CharField(max_length = 3)
  start_datetime = serializers.DateTimeField()
  end_datetime = serializers.DateTimeField()

class BookingSerializer(serializers.ModelSerializer):
 class Meta():
  model = Booking
  fields = '__all__'
#  car_number_plate = serializers.CharField(max_length = 7)
#  start_datetime = serializers.DateTimeField()
#  end_datetime = serializers.DateTimeField()
#  carpark_name = serializers.CharField(max_length = 30)
#  def to_internal_value(self,data):
#   try:
#      data['user'] = data['user']['id']
#   except TypeError:
#     pass
#   try:
#      data['carpark'] = data['carpark']['id']
#   except TypeError:
#     pass
#   try:
#      data['car'] = data['car']['car_number_plate']
#   except TypeError:
#     pass
#   return super(PlayerSerializer, self).to_internal_value(data)

#   def to_representation(self,instance):
#     return ReadBookingSerializer(instance).data

# class ReadBookingSerializer(serializers.ModelSerializer):
#   user = UserSerializer()
#   car = CarSerializer()
#   carpark = CarparkSerializer()
#   class Meta(BookingSerializer.Meta):
#     pass

 



