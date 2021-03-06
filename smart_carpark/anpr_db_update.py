# Python packages
import os
import schedule
from django.db import connection

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

def anpr_db_updater():
    # Every 5 minutes update the live feed database
    schedule.every(5).minutes.do(update_from_anpr_db)
    schedule.run_all()
