from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def avish(request):
    return HttpResponse("<h1> Hello Avish </h1> ")

def dhruvil(request):
    return HttpResponse("<h1> hello Dhruvil </h1>")

def about(request):
    return HttpResponse("<h1> About Page </h1>")

def greet(request,name):
    return render(request,"greet.html",{
        "name":name
    })
