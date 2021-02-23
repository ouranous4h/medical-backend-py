from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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
