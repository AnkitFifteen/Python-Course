from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Pet
#from .forms import CreateTaskForm

# Create your views here.
class ViewPets(ListView):
    model = Pet
    template_name = "view-pets.html"
    context_object_name = "pet_records"

# class LoginSignup(CreateView):
#     model = Pet
#     form_class = SignupForm
#     template_name = "login-signup.html"
#     success_url = reverse_lazy('ViewPets')