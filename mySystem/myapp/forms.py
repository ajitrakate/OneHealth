from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from myapp.models import (User, Patient, Doctor, Appointment)


class DoctorSignUpForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.specialization = self.cleaned_data.get('specialization')
        doctor.save()
        return user


class PatientSignUpForm(UserCreationForm):
    city = forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.save()
        return user

