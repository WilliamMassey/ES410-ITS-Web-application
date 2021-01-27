from django.shortcuts import render, redirect
from .models import Carpark, Live_Feed
from accounts.models import User_Car_Mapping, Car, Booking, Booking_data
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from datetime import datetime, timedelta, time, date

# Create your views here.
def home(request):
    # make database
    today = date.today()
    three_days = timedelta(days=3)
    carparks = Carpark.objects.all()
    carpark_list = []
    for carpark in carparks:
        carpark_data_object = Booking_data.objects.filter(carpark = carpark, date__lte =  today + three_days , date__gte = today)
        carpark_list.append(carpark_data_object)

    if request.user.is_authenticated:

        numberplates = User_Car_Mapping.objects.filter(user__exact = request.user).values_list('car', flat = True)
        cars = Car.objects.filter(car_number_plate__in = numberplates)
        bookings = Booking.objects.filter(car__in = cars)
    else:
        cars =[]
        bookings=[]
    if cars:
        is_car_empty = False
    else:
        is_car_empty = True
    if bookings:
        is_booking_empty = False
    else: 
        is_booking_empty = True
    
    return render(request, 'index.html', {'carparks' : carpark_list, 'cars' : cars, 'is_car_empty' : is_car_empty, 'is_booking_empty' : is_booking_empty, 'bookings': bookings})

def email_test(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        contents = request.POST['contents']
        from_email = request.user
        if from_email and subject and contents:
            try:
                send_mail(subject, contents, from_email, ['will.a.c.massey@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request,'index.html')
    else:
        return render(request, 'email_test.html')
