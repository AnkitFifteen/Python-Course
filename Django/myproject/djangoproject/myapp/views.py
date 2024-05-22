from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
import math
from django.template import loader
# Create your views here.

def demo(request):
    dt = datetime.now()
    pi = math.pi

    resp1 = HttpResponse("Hello this is prachi??+. This is my first Django Project")
#    resp2 = HttpResponse("Today's date and time %s" %dt)
#    resp3 = HttpResponse("Math pi value %s" %pi)
#    resp4 = HttpResponse("Math pi value %s" %pi)

#    resp = resp1 + resp2 + resp3 + resp4
    resp = resp1

    return resp

def welcome(request):
    temp = loader.get_template('demo.html')
    dt = datetime.now()
    msg = "unknown"
    if dt.hour < 12:
        msg = "Good Morning"
    elif dt.hour < 16 and dt.hour > 12:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"
    s1 = {"name":"prachi", "id":2}
    s2 = {"name":"Ram", "id": 1}
    student = {'sdict': [s1,s2], "greeting":msg}
    return HttpResponse(temp.render(student, request))

def top_nav(request):
    temp = loader.get_template('top-nav.html')
    return HttpResponse(temp.render())