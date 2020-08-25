from django.shortcuts import render,redirect
from django.forms import forms,CharField,IntegerField

# Create your views here.
tasks=[
    "check email",
    "send money",
    "give rent"
]
class NewTask(forms.Form):
    addtask=CharField(label=" Add Task :",max_length=64)
    priority=IntegerField(label="Priority :",min_value=2,max_value=10)


def index(request):
    return render(request,"taskapp/index.html",{
        "tasks":tasks
    })

def add(request):
    form=NewTask()
    if request.method=="POST":
        form=NewTask(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["addtask"])
            return redirect("index")
        else :
            return render(request,"taskapp/add.html",{
                "form":form
            })

    return render(request,"taskapp/add.html",{
        "form":form
    })