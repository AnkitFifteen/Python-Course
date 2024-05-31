from django import forms
from .models import Pet

class SignupForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'email', 'phone', 'password']
