from django.shortcuts import render

# Create your views here.
tasks=[
    "check email",
    "send money",
    "give rent"
]

def index(request):
    return render(request,"taskapp/index.html",{
        "tasks":tasks
    })

def add(request):
    return render(request,"taskapp/add.html")