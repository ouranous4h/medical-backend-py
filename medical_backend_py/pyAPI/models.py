from django.db import models


class User(models.Model):
  username = models.CharField(max_length=30)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=100)

class Admin(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Clinic(models.Model):
  name = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  address = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)

class Person(models.Model):
  name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  middlename = models.CharField(max_length=30)
  dob = models.IntegerField() #ddmmyy
  gender = models.CharField(max_length=6)
  phone = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Doctor(models.Model):
  ### speciality (change maybe to foreign key)
  speciality = models.CharField(max_length=30)
  clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Patient(models.Model):
  info = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Patient_Doctor(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)



# ## medical card (which has diseases(numbers), treatment, diagnose)
#             ## to do : area of research -> disease -> diagnosis, treatment
