from django.shortcuts import render
from django.views.generic import ListView
from .models import Tasks

# Create your views here.
class TaskList(ListView):
    model = Tasks
    template_name = "show-tasks.html"
    context_object_name = "tasks_records"