from django.db import models


class userP(models.Model):
  username = models.CharField(max_length=30)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=30)

class Patient(models.Model):
  name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  middlename = models.CharField(max_length=30)
  age = models.IntegerField()
  gender = models.CharField(max_length=6)
  phone = models.CharField(max_length=30)

  userP = models.ForeignKey(userP, on_delete=models.CASCADE)

# class Doctor(models.Model):
#   ## add foreign keys -> patients
#   name = models.CharField(max_length=30, null = False, blank = False, unique = False)
#   surname = models.CharField(max_length=30, null = False, blank = False, unique = False)
#   middlename = models.CharField(max_length=30, null = True, blank = True, unique = False)
#   age = models.IntegerField(null = False, blank = False, unique = False)
#   gender = models.CharField(max_length=6, null = False, blank = False, unique = False)
#   phone = models.PhoneNumberField(null = False, blank = False, unique = True)

#   speciality = models.CharField(max_length=50, null = False, blank = False, unique = False)

# ## hospital model -> foreign keys doctors
# class Clinic(models.Model):
#   name = models.CharField(max_length=30, null = False, blank = False, unique = False)
#   phone = models.PhoneNumberField(null = False, blank = False, unique = True)
#   address = models.CharField(max_length=30, null = False, blank = False, unique = False)
# ## medical card (which has diseases(numbers), treatment, diagnose)
#             ## to do : area of research -> disease -> diagnosis, treatment
