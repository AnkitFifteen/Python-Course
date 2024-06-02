from django import forms
from .models import State

class CreateStateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['Name', 'Population', 'Language', 'Capital']