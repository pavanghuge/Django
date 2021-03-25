from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World !!")

def pavan(request):
    return HttpResponse("Helloo, Pavan !!!")

def greet(request,name):
    return HttpResponse(f"Hello, {name.capitalize()} !!!")

def hello_from_htmlpage(request):
    return render(request,"hello/index.html")

def greeting(request,name):
    return render(request,"hello/greeting.html",{
        "name": name.capitalize()
    })
