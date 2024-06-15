from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=500)

    class Meta:
        db_table = 'Employee'
