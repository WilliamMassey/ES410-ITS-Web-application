from django.contrib import admin
from .models import Carpark, Carpark_Data

# Add carpark model to admin page
admin.site.register(Carpark)
admin.site.register(Carpark_Data)