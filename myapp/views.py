from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    date=datetime.datetime.now()
    print("Home function from view")
    #return HttpResponse("<h1>This is index page</h1>"+str(date))
    return render(request, "home.html", {})

def about(request):
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html", {})

def services(request):
    #return HttpResponse("<h1>This is services page</h1>")
    return render(request, "services.html", {})