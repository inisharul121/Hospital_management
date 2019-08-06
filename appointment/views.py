from django.shortcuts import render
from .form import AppoinmentForm

# Create your views here.

from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def appointment_form(request):
    pass
    # if request.method='POST'
    # form =AppoinmentForm(request.POST)
    # form.save()
    # esle:
    # form=AppoinmentForm
    # return render(request,'appointment.html',{})