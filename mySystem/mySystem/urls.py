"""mySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import home, about, contact, doctors, SignUpView, PatientSignUpView, DoctorSignUpView, dashboard, dashDoctors, createAppointment, allAppointments, profile, cancel, bookAppointment, book, approve,reject

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('doctors', doctors, name='doctors'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/cancel/<int:pk>', cancel, name='cancel'),
    path('dashboard/action1/<int:pk>', approve, name='approve'),
    path('dashboard/action0/<int:pk>', reject, name='reject'),
    path('dashboard/doctors', dashDoctors, name='dashDoctors'),
    path('dashboard/doctors/book/<int:pk>', bookAppointment, name='bookAppointment'),
    path('dashboard/doctors/booked', book, name='book'),
    path('dashboard/profile', profile, name='profile'),
    path('dashboard/create', createAppointment, name='create'),
    path('dashboard/all', allAppointments, name='all'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/patient/', PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
]
