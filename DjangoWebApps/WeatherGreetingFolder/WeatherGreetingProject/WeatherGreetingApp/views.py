from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time, timezone
# Create your views here.

def greeting1(request):
    dt = datetime.now()
    TimeTuple = dt.timetuple()
    index = 0
    for value in TimeTuple:
        print(value)
        index += 1
    t = time.hour
    resp2 = HttpResponse("Today's date and time %s" %t)
    return resp2

def greeting(request):
    dt = datetime.now()
    msg = "unknown"
    if dt.hour < 12:
        msg = "Good Morning"
    elif dt.hour < 16 and dt.hour > 12:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"
    return HttpResponse(msg)
