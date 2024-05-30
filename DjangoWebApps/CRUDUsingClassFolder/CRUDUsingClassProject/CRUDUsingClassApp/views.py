from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
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

class UpdateTask(UpdateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = "update-task.html"
    success_url = reverse_lazy('TaskList')

class DetailViewTask(DetailView):
    model = Tasks
    template_name = "view-task-details.html"
    context_object_name = "task"

class DeleteTask(DeleteView):
    model = Tasks
    template_name = "confirm-to-delete-task.html"
    success_url = reverse_lazy('TaskList')


