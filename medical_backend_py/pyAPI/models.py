from django.db import models

# Create your models here.
class userP(models.Model):
  username = models.CharField(max_length=30, null = False, blank = False, unique = False)
  email = models.CharField(max_length=30, null = False, blank = False, unique = False)
  password = models.CharField(max_length=30, null = False, blank = False, unique = False)

## hospital -> doctors -> patients
## patients -> medical card, doctors
## maybe make it inherited from human? ex: patient -> human, doctor -> human (name, surname, mname, age, phone, etc)
class Patient(models.Model):
  ## add foreign keys -> doctors
  # -> medical card
  # -> foreign key userP id
  name = models.CharField(max_length=30, null = False, blank = False, unique = False)
  surname = models.CharField(max_length=30, null = False, blank = False, unique = False)
  middlename = models.CharField(max_length=30, null = True, blank = True, unique = False)
  age = models.IntegerField(null = False, blank = False, unique = False)
  gender = models.CharField(max_length=6, null = False, blank = False, unique = False)
  phone = models.PhoneNumberField(null = False, blank = False, unique = True)

class Doctor(models.Model):
  ## add foreign keys -> patients
  name = models.CharField(max_length=30, null = False, blank = False, unique = False)
  surname = models.CharField(max_length=30, null = False, blank = False, unique = False)
  middlename = models.CharField(max_length=30, null = True, blank = True, unique = False)
  age = models.IntegerField(null = False, blank = False, unique = False)
  gender = models.CharField(max_length=6, null = False, blank = False, unique = False)
  phone = models.PhoneNumberField(null = False, blank = False, unique = True)

  speciality = models.CharField(max_length=50, null = False, blank = False, unique = False)

## hospital model -> foreign keys doctors
class Clinic(models.Model):
  name = models.CharField(max_length=30, null = False, blank = False, unique = False)
  phone = models.PhoneNumberField(null = False, blank = False, unique = True)
  address = models.CharField(max_length=30, null = False, blank = False, unique = False)
## medical card (which has diseases(numbers), treatment, diagnose)
            ## to do : area of research -> disease -> diagnosis, treatment
