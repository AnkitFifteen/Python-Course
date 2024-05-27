from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
import math
from django.template import loader
from .models import Students
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
    student = {'sdict': [s1,s2], "greeting":msg, "number":3}
    return HttpResponse(temp.render(student, request))

def top_nav(request):
    temp = loader.get_template('top-nav.html')
    return HttpResponse(temp.render())

def register_student(request):
    if request.method == "GET":
        return render(request, "register-student.html")
    elif request.method == "POST":
        firstname = request.POST.get("firstname")
        phoneno = request.POST.get("phonenovalue")
        emailvalue = request.POST.get("emailvalue")

        student_object = Students(name=firstname, email=emailvalue, phoneno=phoneno)
        student_object.save()
        return HttpResponse("Student Registered Successfully.")
    
def show_students_records(request):
    if request.method == "GET":
        student_records = Students.objects.all()
        return render(request, "show-students-records.html", {"student_records":student_records})
    
def edit_student_record(request, student_id):
    if request.method == "GET":
        student_record = Students.objects.get(id = student_id)
        return render(request, "edit-student-record.html", {"student_record":student_record})
    elif request.method == "POST":
        studentID = request.POST.get("id")
        student_record = Students.objects.get(id = student_id)
        firstname = request.POST.get("firstname")
        phoneno = request.POST.get("phonenovalue")
        emailvalue = request.POST.get("emailvalue")
        student_object = Students(id=studentID, name=firstname, email=emailvalue, phoneno=phoneno)

    
