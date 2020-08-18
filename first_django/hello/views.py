from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello world </h1>")

def avish(request):
    return HttpResponse("<h1> Hello Avish </h1>")

def dhruvil(request):
    return HttpResponse("<h1> hello Dhruvil </h1>")

def about(request):
    return HttpResponse("<h1> About Page </h1>")