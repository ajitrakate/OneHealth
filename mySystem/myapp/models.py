from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime,time,date
from django.utils import timezone

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)



class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patientID = models.IntegerField()
    patientUsername = models.CharField(default="", max_length=100)
    doctorID = models.IntegerField()
    doctorUsername = models.CharField(default="", max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100, default="Pending")
    description = models.TextField()
    def __str__(self):
        return self.patientUsername