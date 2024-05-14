from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
import math
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