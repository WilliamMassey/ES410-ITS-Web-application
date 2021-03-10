from rest_framework import serializers
from .models import Carpark

class CarparkSerializer(serializers.ModelSerializer):
 class Meta():
  model = Carpark
  fields = ['name']  
  
