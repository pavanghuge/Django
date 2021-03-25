from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    context = {
    "newyear" : now.month == 1 and now.day == 1 
    #"newyear" : True
    }

    return render(request,"newyear/index.html",context)


