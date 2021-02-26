from django.db import models

# Create your models here.

## maybe make it inherited from human? ex: patient -> human, doctor -> human (name, surname, mname, age, phone, etc)
class Patient(models.Model):
  name = models.CharField(max_length=30, null = False, blank = False, unique = False)
  surname = models.CharField(max_length=30, null = False, blank = False, unique = False)
  middlename = models.CharField(max_length=30, null = True, blank = True, unique = False)
  age = models.IntegerField(null = False, blank = False, unique = False)
  gender = models.CharField(max_length=6, null = False, blank = False, unique = False)
  phone = models.PhoneNumberField(null = False, blank = False, unique = True)

class Doctor(models.Model):
  name = models.CharField(max_length=30, null = False, blank = False, unique = False)
  surname = models.CharField(max_length=30, null = False, blank = False, unique = False)
  middlename = models.CharField(max_length=30, null = True, blank = True, unique = False)
  age = models.IntegerField(null = False, blank = False, unique = False)
  gender = models.CharField(max_length=6, null = False, blank = False, unique = False)
  phone = models.PhoneNumberField(null = False, blank = False, unique = True)

  speciality = models.CharField(max_length=50, null = False, blank = False, unique = False)

