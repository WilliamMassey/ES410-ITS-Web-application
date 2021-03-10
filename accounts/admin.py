from django.contrib import admin
from .models import Details, Booking, User_Car_Mapping, Car, Booking_data
# Register your models here.

# This means that these models are accessible on the admin page
admin.site.register(Details)
admin.site.register(Booking)
admin.site.register(Booking_data)
admin.site.register(User_Car_Mapping)
admin.site.register(Car)


