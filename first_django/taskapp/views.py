from django.shortcuts import render
from django.forms import forms,CharField,IntegerField,Em

# Create your views here.
tasks=[
    "check email",
    "send money",
    "give rent"
]
class NewTask(forms.Form):
    addtask=CharField(label=" Add Task :",max_length=64)
    priority=IntegerField(label="Priority :",min_value=2,max_value=17)


def index(request):
    return render(request,"taskapp/index.html",{
        "tasks":tasks
    })

def add(request):
    form=NewTask()
    return render(request,"taskapp/add.html",{
        "form":form
    })