# Python packages
import os
import schedule
from django.db import connection

from django.core.mail import send_mail
from accounts.models import Booking
from home.models import Carpark, Carpark_Data
from datetime import timedelta, datetime, timezone

def update_from_anpr_db():
    # Obtain database connections
    anpr_db_path = "../SVM_ANPR/database/anpr_db.sqlite3"
    if os.path.isfile(anpr_db_path):
        with connection.cursor() as cursor:
            # Update webapp with anpr live feed
            cursor.execute("ATTACH DATABASE %s AS other;", (anpr_db_path,))
            cursor.execute("\
                    INSERT OR IGNORE INTO home_live_feed(id, timestamp, car_number_plate, carpark) \
                    SELECT id, timestamp, car_number_plate_id, carpark_id \
                    FROM other.anpr_live_feed ;")
    else:
        print("Error: Unable to make ANPR database connection!")
        schedule.clear()

def remind_bookings():
    print("remind bookings running")
    now = datetime.now(timezone.utc)
    in_hour = now - timedelta(minutes=now.minute%15,seconds=now.second,microseconds=now.microsecond)+ timedelta(hours=1)
    bookings = Booking.objects.filter(start_datetime = in_hour)
    print(in_hour)
    print(bookings)
    for booking in bookings:
        print(f"sedning email for booking {booking.id}")
        send_mail('Warwick Carpark Booking Reminder',f'<h1>Warwick Carparking<h1>Dear {booking.user.first_name},\nYou have a booking at the  {booking.carpark.name} carpark from {booking.start_datetime.ctime()} to {booking.end_datetime.ctime()}. Do you still plan to attend? Using the following link to confirm: ___','will.a.c.massey@gmail.com',['w.massey.1@warwick.ac.uk'],fail_silently=False)

def add_new_booking_data():
    carparks = Carpark.objects.all()
    in_week = (datetime.now(timezone.utc) + timedelta(days = 7)).date
    for carpark in carparks:
        Carpark_Data.objects.create(carpark = carpark, date = in_week, is_booking = True)

    print("adding new booking data")

def anpr_db_updater():
    # Every 5 minutes update the live feed database
    schedule.every(15).minutes.do(remind_bookings)
    #schedule.every(5).minutes.do(update_from_anpr_db)
    # schedule.every().day.at("23:59").do(add_new_booking_data)
    schedule.run_all()
