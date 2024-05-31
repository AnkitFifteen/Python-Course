from django.db import models

# Create your models here.
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

    class Meta:
        db_table = "Pet"

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "Customer"