from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from StudentProfile.models import StudentProfile
from django.core import serializers
from django.contrib.auth.models import User
from django.middleware.csrf import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hack(request):
    print(request.META)
    return HttpResponse("")