from datetime import datetime, timedelta
from django.http import HttpResponse


# This converts the format given by HTML date time form submission to a datetime object 
def conv_html_datetime(html_datetime):
    dash_1_pos = 4
    dash_2_pos = 7
    T_pos = 10
    colon_pos = 13
    print("The html datetime format" + html_datetime)
    year = html_datetime[:dash_1_pos]
    month = html_datetime[dash_1_pos+1:dash_2_pos]
    day = html_datetime[dash_2_pos+1:T_pos]
    hour = html_datetime[T_pos+1:colon_pos]
    minute = html_datetime[colon_pos+1:]

    if year and month and day and hour and minute:
        return datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute))

    else:
        return datetime(2000,1,1)

# creates dictionary with a string key for every 15 min slot in the day, in the iso format (HH:MM:SS) and sets all of the values to 0 
def time_slot_default():
    no_slots = 24*4
    slot_length = timedelta(minutes=15)
    time_slot = dict()

    for slot in range(0,no_slots):
        time_slot[((datetime(year=2020, month=1, day=1) + slot*slot_length).time()).isoformat()] = 0 
    return time_slot

