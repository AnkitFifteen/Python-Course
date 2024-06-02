from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CreateStateForm
from .models import State

# Create your views here.
class ViewStates(ListView):
    model = State
    template_name = "show-states-records.html"
    context_object_name = "states_records"
    
class CreateState(CreateView):
    model = State
    form_class = CreateStateForm
    template_name = "create-state.html"
    success_url = reverse_lazy('ViewStates')

class UpdateState(UpdateView):
    model = State
    form_class = CreateStateForm
    template_name = "edit-state-record.html"
    context_object_name = "State"
    success_url = reverse_lazy('ViewStates')

class DeleteState(DeleteView):
    model = State
    template_name = "confirm-to-delete-state.html"
    success_url = reverse_lazy('ViewStates')
