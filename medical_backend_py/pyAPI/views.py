from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from werkzeug.security import check_password_hash, generate_password_hash
from pyAPI.models import User, Clinic, Person, Doctor, Patient, Patient_Doctor
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        d = json.loads(request.body)
        if any (k not in d for k in ("username","password")):
            return HttpResponse(status = 400)

        un = d["username"]
        if un == "" or un == None:
            return HttpResponse(status = 400)
        ps = d["password"]
        if ps == "" or ps == None:
            return HttpResponse(status = 400)
        user = User.objects.get(username = un)
        if not check_password_hash(User.password, ps):
            return HttpResponse(status = 401)
        return HttpResponse(status = 200)

@csrf_exempt
def register(request):
    if request.method == "POST":
        d = json.loads(request.body)
        if any (k not in d for k in ("username","password","password_confirmation","email")):
            return HttpResponse(status = 400)

        un = d["username"]
        if un == "" or un == None:
            return HttpResponse(status = 400)
        ps = d["password"]
        pscon = d["password_confirmation"]
        if ps != pscon:
            return HttpResponse(status = 400)
        hashed = generate_password_hash(ps)
        em = d["email"]
        user = User(username = un, password = hashed, email = em)
        user.save()
        return HttpResponse(status = 201)

@csrf_exempt
def register_person(request):
    if request.method == "POST":
        d = json.loads(request.body)
        if any (k not in d for k in ("username","name","surname","dob","gender","phone")):
            return HttpResponse(status = 400)

        n = d["name"]
        if n == "" or n == None:
            return HttpResponse(status = 400)

        sn = d["surname"]
        if sn == "" or sn == None:
            return HttpResponse(status = 400)

        if "middlename" in d:
            mn = d["middlename"]
        else:
            mn = ""

        if d["dob"] == "" or d["dob"] == None:
            return HttpResponse(status = 400)
        else:
            dob = int(d["dob"])

        gender = d["gender"]
        if gender == "" or gender == None:
            return HttpResponse(status = 400)

        phone = d["phone"]
        if phone == "" or phone == None:
            return HttpResponse(status = 400)

        un = d["username"]
        if un == "" or un == None:
            return HttpResponse(status = 400)

        user = User.objects.get(username = un)
        person = Person(name = n, surname = sn, middlename = mn, dob = dob, gender = gender, phone = phone, user = user)
        person.save()
        return HttpResponse(status = 201)

@csrf_exempt
def patients(request):
    if request.method == 'GET':
        return HttpResponse({"patients":"patients"}, content_type = "text/json")

@csrf_exempt
def clinics(request):
    if request.method == 'GET':
        return HttpResponse({}, content_type = "text/json")

@csrf_exempt
def appointments(request):
    if request.method == 'GET':
        return HttpResponse({}, content_type = "text/json")

@csrf_exempt
def history(request):
    if request.method == 'GET':
        return HttpResponse({}, content_type = "text/json")
