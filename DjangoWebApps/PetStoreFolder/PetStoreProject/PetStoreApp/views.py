from django.shortcuts import render, redirect
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

    def get_context_data(self, **kwargs):
        data = self.request.session['sessionvalue']
        context = super().get_context_data(**kwargs)
        context['session'] = data
        return context
    
class PetDetails(DetailView):
    model = Pet
    template_name = "pet-details.html"
    context_object_name = "pet"

def SearchPets(request):
    if request.method == "POST":
        search_data = request.POST.get('searchquery')
        pet_records = Pet.objects.filter(Q(name__icontains = search_data)|Q(breed__icontains = search_data)|Q(species__icontains = search_data)|Q(description__icontains = search_data)|Q(price__icontains = search_data))
        return render(request, "view-pets.html", {'pet_records':pet_records})
    
def RegisterUser(request):
    if request.method == "GET":
        return render(request, 'register-user.html')
    elif request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        password = request.POST.get("Password")
        encrypted_password = make_password(password)

        email_present = Customer.objects.filter(email=email)

        if email_present:
            return render(request, "register-user.html", {"EmailPresent":"Flag for email already used."})
        else:
            customer_record = Customer(name=name,email=email,phone=phone,password=encrypted_password)
            customer_record.save()
            pet_records = Pet.objects.all()
            return redirect("../login-user/")
            # return render(request, "view-pets.html", {'pet_records':pet_records})
    
def LoginUser(request):
    if request.method == "GET":
        return render(request, "login-user.html")
    elif request.method == "POST":
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")

        cust = Customer.objects.filter(email=Email)
        if cust:
            custobj = Customer.objects.get(email=Email)

            flag = check_password(Password, custobj.password)

            if flag:
                request.session["sessionvalue"] = custobj.name
                return render(request, "view-pets.html", {"session": request.session["sessionvalue"]})
            else: 
                return render(request, "login-user.html", {"InvalidInput":"Flag for invalid input."})
        else:
            return render(request, "login-user.html", {"InvalidInput":"Flag for invalid input."})

# class LoginSignup(CreateView):
#     model = Pet
#     form_class = SignupForm
#     template_name = "login-signup.html"
#     success_url = reverse_lazy('ViewPets')