from django import forms
from .models import Employee

class RegisterEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid', 'fname', 'lname', 'age', 'address']