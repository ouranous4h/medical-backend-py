"""medical_backend_py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from pyAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login),
    path('register/', views.register),
    path('register_person/', views.register_person),
    path('register_patient/', views.register_patient),
    path('register_doctor/', views.register_doctor),
    path('register_patient_doctor/', views.register_patient_doctor),
    path('register_clinic/', views.register_clinic),
    path('clinic/', views.clinic),
    path('doctor/', views.doctor),
    path('docAppointment/', views.docAppointment)
    # path('patients/', views.patients), ##tolko dlya doctorov (ih pacienti)
    # path('appointments/', views.appointments),
    # path('history/', views.history)
]