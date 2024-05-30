from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Students
from .forms import RegisterStudentForm

# Create your views here.
class ViewStudents(ListView):
    model = Students
    template_name = "view-students.html"
    context_object_name = "students_records"
    
class RegisterStudent(CreateView):
    model = Students
    form_class = RegisterStudentForm
    template_name = "register-student.html"
    success_url = reverse_lazy('ViewStudents')

class UpdateStudent(UpdateView):
    model = Students
    form_class = RegisterStudentForm
    template_name = "edit-student-record.html"
    success_url = reverse_lazy('ViewStudents')

class DeleteStudent(DeleteView):
    model = Students
    template_name = "confirm-to-delete-student.html"
    success_url = reverse_lazy('ViewStudents')
