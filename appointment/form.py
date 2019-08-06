from django import forms

from .models import Appointment

class AppoinmentForm(forms.ModelForm):
    class meta:
        model = Appointment
        fields='__all__'
