from datetime import datetime
from django.http import HttpResponse

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
    





    
        
