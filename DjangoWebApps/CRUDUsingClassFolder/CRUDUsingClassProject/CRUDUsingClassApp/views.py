from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Tasks
from .forms import CreateTaskForm

# Create your views here.
class TaskList(ListView):
    model = Tasks
    template_name = "show-tasks.html"
    context_object_name = "tasks_records"

class CreateTask(CreateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = "create-task.html"
    success_url = reverse_lazy('TaskList')