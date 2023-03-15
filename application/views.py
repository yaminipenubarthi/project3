from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def yami_application(request):
    return HttpResponse('<h1>my name is yami</h1>')