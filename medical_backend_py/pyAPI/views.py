from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from werkzeug.security import check_password_hash, generate_password_hash
from pyAPI.models import User, Admin, Clinic, Person, Doctor, Patient, Patient_Doctor
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # login
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
        if not check_password_hash(user.password, ps):
            return HttpResponse(status = 401)

        data = {
            'id': user.pk
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json', status = 200)

@csrf_exempt
def register(request):
    if request.method == "POST":
        # register user
        d = json.loads(request.body)
        if any (k not in d for k in ("username","password","password_confirmation","email")):
            return HttpResponse(status = 400)
        if User.objects.filter(username = d["username"]).exists():
            return HttpResponse(status = 400)
        un = d["username"]
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
        # register person info
        d = json.loads(request.body)
        if any (k not in d for k in ("user_id","name","surname","dob","gender","phone")):
            return HttpResponse(status = 400)

        n = d["name"]
        sn = d["surname"]
        dob = int(d["dob"])
        gender = d["gender"]
        phone = d["phone"]
        uid = d["user_id"]
        if "middlename" in d:
            mn = d["middlename"]
        else:
            mn = ""

        user = User.objects.get(id = uid)
        person = Person(name = n, surname = sn, middlename = mn, dob = dob, gender = gender, phone = phone, user = user)
        person.save()
        return HttpResponse(status = 201)

@csrf_exempt
def register_patient(request):
    # register patient
    if request.method == "POST":
        d = json.loads(request.body)
        if not "user_id" in d:
            return HttpResponse(status = 400)
        if "info" in d:
            info = d["info"]
        else:
            info = ""
        user = User.objects.get(id = d["user_id"])
        patient = Patient(info = info, user = user)
        patient.save()
        return HttpResponse(status = 201)

@csrf_exempt
def register_doctor(request):
    # register doctor
    if request.method == "POST":
        d = json.loads(request.body)
        if not "user_id" in d or not "clinic_id" in d:
            return HttpResponse(status = 400)
        if "speciality" in d:
            speciality = d["speciality"]
        else:
            speciality = ""
        if not Clinic.objects.filter(id = d['clinic_id']).exists():
            return HttpResponse(status = 400)
        if not User.objects.filter(id = d['user_id']).exists():
            return HttpResponse(status = 400)
        user = User.objects.get(id = d["user_id"])
        clinic = Clinic.objects.get(id = d["clinic_id"])
        doctor = Doctor(speciality = speciality, clinic = clinic, user = user)
        doctor.save()
        return HttpResponse(status = 201)

@csrf_exempt
def register_patient_doctor(request):
    # bounds patient and doctor
    if request.method == "POST":
        d = json.loads(request.body)
        if not "user_id" in d or not "doctor_id" in d:
            return HttpResponse(status = 400)
        patient = Patient.objects.get(pk = d["user_id"])
        doctor = Doctor.objects.get(pk = d["doctor_id"])
        patient_doctor = Patient_Doctor(patient = patient, doctor = doctor)
        patient_doctor.save()
        return HttpResponse(status = 201)

@csrf_exempt
def register_clinic(request):
    # create new clinic, must be admin
    if request.method == "POST":
        d = json.loads(request.body)
        if any (k not in d for k in ("user_id","name","city","address","phone")):
            return HttpResponse(status = 400)
        user = None
        if not User.objects.filter(id = d["user_id"]).exists():
            return HttpResponse(status = 400)
        else:
            user = User.objects.get(id = d["user_id"])
        if not Admin.objects.filter(user=user).exists():
            return HttpResponse(status = 400)
        clinic = Clinic(name = d["name"], city = d["city"], address = d["address"], phone = d["phone"])
        clinic.save()
        return HttpResponse(status = 201)

@csrf_exempt
def clinic(request):
    # get all rows
    if request.method == 'GET':
        data = {}
        clinics = Clinic.objects.all()
        for clinic in clinics:
            data[clinic.id] = {
                'id':clinic.id,
                'name':clinic.name,
                'city':clinic.city,
                'address':clinic.address,
                'phone':clinic.phone
            }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type = "text/json", status=200)

    # update row
    elif request.method == 'POST':
        d = json.loads(request.body)
        if any (k not in d for k in ("user_id","clinic_id","name","city","address","phone")):
            return HttpResponse(status = 400)
        user = User.objects.get(id = d["user_id"])
        admin = Admin.objects.get(user=user)
        if not admin:
            return HttpResponse(status = 400)
        clinic = Clinic.objects.get(id = d["clinic_id"])
        clinic.name = d["name"]
        clinic.city = d["city"]
        clinic.address = d["address"]
        clinic.phone = d["phone"]
        clinic.save()
        return HttpResponse(status = 201)
@csrf_exempt
def doctor(request):
    # get doctors
    if request.method == 'GET':
        d = json.loads(request.body)
        ## to do -> make it only one query instead of looping
        if "clinic_id" in d:
            if not Clinic.objects.filter(id = d["clinic_id"]).exists():
                return HttpResponse(status = 400)
            ids = Doctor.objects.filter(clinic = d["clinic_id"])
            data = {}
            for i in ids:
                ddx = Person.objects.get(user = i.user)
                ddy = Doctor.objects.get(user = i.user)
                data[ddy.id] = {
                    'speciality':ddy.speciality,
                    'name':ddx.name,
                    'surname':ddx.surname,
                    'phone':ddx.phone
                }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type = "text/json", status=200)
        elif "doctor_id" in d:
            if not Doctor.objects.filter(id = d["doctor_id"]).exists():
                return HttpResponse(status = 400)
            data = {}
            ddy = Doctor.objects.get(id = d["doctor_id"])
            ddx = Person.objects.get(user = ddy.user)
            data[ddy.id] = {
                'speciality':ddy.speciality,
                'name':ddx.name,
                'surname':ddx.surname,
                'phone':ddx.phone
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type = "text/json", status=200)
        else:
            return HttpResponse(status = 400)


@csrf_exempt
def docAppointment(request):
    if request.method == 'POST':
        d = json.loads(request.body)
        if any (k not in d for k in ("user_id","doctor_id","time","info")):
            return HttpResponse(status = 400)

        ## add check if the user is patient user
        user = User.objects.get(id = d['user_id'])
        doctor = Doctor.objects.get(id = d['doctor_id'])

        Patient_Doctor = Patient_Doctor(patient = user, doctor = doctor)
        Patient_Doctor.save()
        return HttpResponse(status = 201)


@csrf_exempt
def appointments(request):
    if request.method == 'GET':
        return HttpResponse({}, content_type = "text/json")

@csrf_exempt
def history(request):
    if request.method == 'GET':
        return HttpResponse({}, content_type = "text/json")
