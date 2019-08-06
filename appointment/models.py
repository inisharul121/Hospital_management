from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from config import settings


class User(AbstractUser):
    USER_TYPES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('A', 'Admin'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPES)


class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)


class Doctor(models.Model):
    id=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    department=models.OneToOneField(Department,on_delete=models.CASCADE)


class Patient(models.Model):
    id=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Appointment(models.Model):
    id=models.AutoField(primary_key=True)
    patient_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='pat_id')
    doctor_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='doc_id')
    appointment_date=models.DateTimeField(null=False)
