from turtle import done
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,UpdateView)
from django.contrib.auth import login

from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import User, Patient, Doctor, Appointment


# def dashboard(request):
#     param = {'user':request.user}
#     return render(request, 'dashboard.html', param)


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')



class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    doctors = Doctor.objects.all()
    param = {'doctors':doctors}
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'myapp/home.html', param)

@login_required
def dashboard(request):
    if request.user.is_doctor:
        mydoctor = Doctor.objects.get(user=request.user)
        appointments = Appointment.objects.filter(doctorID=mydoctor.pk)
        totalAppointments = len(appointments)
    else:
        mypatient = Patient.objects.get(user=request.user)
        appointments = Appointment.objects.filter(patientID=mypatient.pk)
        totalAppointments = len(appointments)
    pendingApointments = 0
    appovedAppointments = 0
    myappointments = []
    for appointment in appointments:
        if appointment.status == "Approved":
            appovedAppointments += 1
        elif appointment.status == "Pending":
            pendingApointments += 1
            myappointments.append(appointment)
        else:
            pendingApointments += 1
    param = {'user': request.user, 'appointments':myappointments, 'totalAppointments':totalAppointments, 'appovedAppointments':appovedAppointments, 'pendingApointments':pendingApointments}
    return render(request, 'dashboard.html', param)

@login_required
def dashDoctors(request):
    doctors = Doctor.objects.all()
    param = {'doctors': doctors}
    for doctor in doctors:
        print(doctor.specialization)
    return render(request, 'dashDoctors.html', param)


@login_required
def bookAppointment(request, pk):
    dr = Doctor.objects.get(pk=pk)
    param = {'id':pk, 'username':dr.user.username}
    return render(request, 'bookAppointment.html', param)

@login_required
def book(request):
    doctorID = request.GET.get('doctorId')
    dr = Doctor.objects.get(pk=doctorID)
    doctorUsername = dr.user.username
    patient = Patient.objects.get(user=request.user)
    patientUsername = patient.user.username
    patientID = patient.pk
    date = request.GET.get('date')
    desc = request.GET.get('desc')
    appointment = Appointment.objects.create(doctorID=doctorID,patientID=patientID,patientUsername=patientUsername,doctorUsername=doctorUsername,date=date,status="Pending",description=desc)
    appointment.save()
    return redirect('dashboard')


@login_required
def approve(request,pk):
    appointment = Appointment.objects.get(pk=pk)
    appointment.status = "Approved"
    appointment.save()
    return redirect('dashboard')

@login_required
def reject(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    appointment.status = "Rejected"
    appointment.save()
    return redirect('dashboard')

@login_required
def cancel(request,pk):
    appointment = Appointment.objects.get(pk=pk)
    appointment.delete()
    return redirect('dashboard')



@login_required
def profile(request):
    param = {'user': request.user}
    return render(request, 'profile.html', param)

@login_required
def createAppointment(request):
    param = {'user': request.user}
    return render(request, 'createAppointment.html', param)

@login_required
def allAppointments(request):
    appointments = Appointment.objects.all()
    param = {'appointments':appointments}
    return render(request, 'allAppointments.html', param)


# def home(request):
#     return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def doctors(request):
    doctors = Doctor.objects.all()
    param = {'doctors':doctors}
    return render(request, 'myapp/doctors.html', param)

def contact(request):
    return render(request, 'myapp/contact.html')