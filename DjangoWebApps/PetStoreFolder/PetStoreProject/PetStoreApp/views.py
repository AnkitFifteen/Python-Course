from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from .models import Pet, Customer
#from .forms import CreateTaskForm

# Create your views here.
class ViewPets(ListView):
    model = Pet
    template_name = "view-pets.html"
    context_object_name = "pet_records"

def Search(request):
    if request.method == "POST":
        search_data = request.POST.get('searchquery')
        pet_records = Pet.objects.filter(Q(name__icontains = search_data)|Q(breed__icontains = search_data)|Q(species__icontains = search_data)|Q(description__icontains = search_data)|Q(price__icontains = search_data))
        return render(request, "view-pets.html", {'pet_records':pet_records})
    
def Register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        password = request.POST.get("Password")
        encrypted_password = make_password(password)

        customer_record = Customer(name=name,email=email,phone=phone,password=encrypted_password)
        customer_record.save()
        return render(request, "view-pets.html")

# class LoginSignup(CreateView):
#     model = Pet
#     form_class = SignupForm
#     template_name = "login-signup.html"
#     success_url = reverse_lazy('ViewPets')