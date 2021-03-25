from django.shortcuts import render
from django import forms 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#taskList = ["Pavan","Teju","Bhargav"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task: ")
    priority = forms.IntegerField(label = "Priority", min_value =1, max_value=10 )



# Create your views here.
def index(request):
    if "taskList" not in request.session:
        request.session["taskList"] = []
    
    context = {
        "taskList" : request.session["taskList"]
    }
    return render(request,"tasks/index.html",context)

def add(request):
    context = {
        "form": NewTaskForm()
    }
   
    if request.method == "POST":
        form = NewTaskForm(request.POST)#saving data that has been posted
        
        context2 ={
        "form":form
        }

        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["taskList"] += [task] #changed the append method
            return HttpResponseRedirect(reverse("tasks:index"))
        else: 
            return render(request,"tasks/add.html", context2)

    
    return render(request, "tasks/add.html", context)
