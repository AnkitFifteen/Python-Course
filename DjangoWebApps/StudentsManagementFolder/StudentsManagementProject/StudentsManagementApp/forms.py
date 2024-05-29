from django import forms
from .models import Students

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'phoneno']