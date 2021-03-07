from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from werkzeug.security import check_password_hash, generate_password_hash
from pyAPI.models import userP
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        un = request.form.get("username")
        if un == "" or un == None:
            return HttpResponse(status = 400)
        ps = request.form.get("password")
        if ps == "" or ps == None:
            return HttpResponse(status = 400)
        user = userP.objects.get(username = un)
        if len(user) != 1 or not check_password_hash(user.password, ps):
            return HttpResponse(status = 401)
        return HttpResponse(status = 200)
        ###

@csrf_exempt
def register(request):
    if request.method == "POST":
        un = request.form.get("username")
        if un == "" or un == None:
            return HttpResponse(status = 400)
        ps = request.form.get("password")
        pscon = request.form.get("password_confirmation")
        if ps != pscon:
            return HttpResponse(status = 400)
        em = request.form.get("email")
        ##create email regex validation
        hashed = generate_password_hash(ps)
        user = userP()
        user.username = un
        user.password = hashed
        user.email = em
        user.save()
        return HttpResponse(status = 201)
        ###

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
