from django.db import models
from django.db.models import Manager

# Create your models here.
class CustomManager(models.Manager):
    def getdata(self,a):
        return super().get_queryset().filter(species=a)
    
class Pet(models.Model):
    gender = (("Male","male"),("Female","female"))
    image = models.ImageField(upload_to="media")
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200, choices=gender)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    slug = models.SlugField(default='',null=False)

    cpetobj = CustomManager()
    objects = Manager()

    class Meta:
        db_table = "Pet"

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "Customer"

class Cart(models.Model):
    cid = models.ForeignKey(Customer,on_delete=models.CASCADE)
    pid = models.ForeignKey(Pet,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalamount= models.FloatField()

    class Meta:
        db_table='Cart'

class Order(models.Model):
    ordernumber = models.CharField(max_length=100)
    orderdate = models.DateField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    orderstatus = models.CharField(max_length=100)

    class Meta:
        db_table = 'Order'

class Payment(models.Model):
    customerid = models.ForeignKey(Customer, on_delete = models.CASCADE)
    oid = models.ForeignKey(Order, on_delete = models.CASCADE)
    paymentstatus = models.CharField(max_length = 100, default = 'Pending')
    transactionid = models.CharField(max_length = 200)
    paymentmode = models.CharField(max_length = 100, default = 'PayPal')

    class Meta:
        db_table = 'Payment'

class OrderDetail(models.Model):
    ordernumber = models.CharField(max_length = 100)
    customerid = models.ForeignKey(Customer, on_delete = models.CASCADE)
    productid = models.ForeignKey(Pet, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    paymentid = models.ForeignKey(Payment, on_delete = models.CASCADE, null = True)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        db_table = 'OrderDetail'
