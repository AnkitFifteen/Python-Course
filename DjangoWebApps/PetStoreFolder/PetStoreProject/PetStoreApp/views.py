from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from .models import Pet, Customer, Cart, Order
from datetime import datetime
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
                request.session["sessionvalue"] = custobj.email
                return render(request, "view-pets.html", {"session": request.session["sessionvalue"]})
            else: 
                return render(request, "login-user.html", {"InvalidInput":"Flag for invalid input."})
        else:
            return render(request, "login-user.html", {"InvalidInput":"Flag for invalid input."})

def AddToCart(request):
    productid = request.POST.get('ProductID')
    custsession = request.session['sessionvalue'] #email of customer
    custobj = Customer.objects.get(email = custsession) #fetch record from database table using email
    custid = custobj.id #fetch customer id using customer object
    pobj = Pet.objects.get(id = productid)

    flag = Cart.objects.filter(cid = custobj.id,pid = pobj.id)
    if flag:
        cartobj = Cart.objects.get(cid = custobj.id,pid = pobj.id)
        cartobj.quantity = cartobj.quantity +1
        cartobj.totalamount = pobj.price * cartobj.quantity
        cartobj.save()
    else:
        cartobj = Cart(cid = custobj,pid = pobj,quantity = 1,totalamount = pobj.price*1)
        cartobj.save()

    return redirect('../view-pets/')


def ViewCart(request):
    custsession = request.session['sessionvalue'] #email of customer
    custobj = Customer.objects.get(email = custsession) 
    cart_products = Cart.objects.filter(cid = custobj.id)

    return render(request,'cart.html',{'cart_products':cart_products})

def ChangeQuantity(request):
    cemail = request.session['sessionvalue']
    pid = request.POST.get('pid')
    custobj = Customer.objects.get(email = cemail)
    pobj = Pet.objects.get(id = pid)
    cartobj = Cart.objects.get(cid = custobj.id,pid=pobj.id)

    if request.POST.get('changequantitybutton') == '+':
        cartobj.quantity = cartobj.quantity + 1
        cartobj.totalamount = cartobj.quantity * pobj.price
        cartobj.save()

    elif request.POST.get('changequantitybutton') == '-':
        if cartobj.quantity == 1:
            cartobj.delete()
        else :
            cartobj.quantity = cartobj.quantity - 1
            cartobj.totalamount = cartobj.quantity * pobj.price
            print(cartobj.totalamount)
            cartobj.save()

    return redirect('../view-cart/')

def OrderCheckout(request):
    if request.method == "GET":
        custsession = request.session['sessionvalue'] 
        custobj = Customer.objects.get(email = custsession) 
        cart_products = Cart.objects.filter(cid = custobj.id)
        total_amount = 0
        for product in cart_products:
            total_amount += product.totalamount
        return render(request,'order-checkout.html',{'cart_products':cart_products, 'total_amount':total_amount})
    
def PlaceOrder(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    phoneno = request.POST.get('phoneno')

    datetimev = datetime.now()
    print(datetimev.date)
    orderobj = Order(firstname = first_name, lastname = last_name, address = address, city = city, state = state, pincode = pincode, phoneno = phoneno, orderdate = datetimev)
    orderobj.save()

    order_no = str(orderobj.id) + str(datetimev.date).replace('-','')
    orderobj.ordernumber = order_no
    orderobj.save()

    custsession = request.session['sessionvalue'] 
    custobj = Customer.objects.get(email = custsession) 
    cart_products = Cart.objects.filter(cid = custobj.id)

    total_amount = 0
    for product in cart_products:
        total_amount += product.totalamount

    return render(request, 'payment.html', {'orderobj':orderobj, 'session':custsession, 'cart_products':cart_products, 'total_amount':total_amount})

        