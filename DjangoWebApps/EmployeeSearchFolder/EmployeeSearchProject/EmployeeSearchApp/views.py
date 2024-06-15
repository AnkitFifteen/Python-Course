from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Employee
from .forms import RegisterEmployeeForm

# Create your views here.
class ViewEmployees(ListView):
    model = Employee
    template_name = "show-employees-records.html"
    context_object_name = "employee_records"
    
class RegisterEmployee(CreateView):
    model = Employee
    form_class = RegisterEmployeeForm
    template_name = "register-employee.html"
    success_url = reverse_lazy('ViewEmployees')

def SearchNameStartsWith(request, name):
    if request.method == "GET":
        query_set = Employee.objects.filter(Q(fname__startswith=name)|Q(lname__startswith=name))
        if query_set.exists():
            employee_records = query_set.all()
        return render(request, "search-results.html", {'employee_records':employee_records})

def SearchNameContains(request):
    if request.method == "GET":
        search_data = request.POST.get('search_name_contains_query')
        query_set = Employee.objects.filter(Q(fname__icontains=search_data)|Q(lname__icontains=search_data))
        if query_set.exists():
            employee_records = query_set.all()
        return render(request, "search-results.html", {'employee_records':employee_records})
    
def SearchAgeLessThanEqualTo(request):
    if request.method == "GET":
        search_data = request.POST.get('search_age_less_than_equal_to_query')
        query_set = Employee.objects.filter(age__lte=search_data)
        if query_set.exists():
            employee_records = query_set.all()
        return render(request, "search-results.html", {'employee_records':employee_records})