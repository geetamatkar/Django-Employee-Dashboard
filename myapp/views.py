from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):

    if request.method=='POST':
        check = request.POST['check']
        print(check)

    

    date=datetime.datetime.now()
    isActive = True
    name = 'IIT'
    list_of_programs = [
        'Web Dev',
        'Algorithms',
        'Programming',
        'OOP'
    ]
    student = {
        'student_name':"John",
        'student_address':"Chicago"
    }

    data = {
        'date':date,
        'isActive' : isActive,
        'name' : name,
        'list_of_programs' : list_of_programs,
        'student_data':student,
    }

    print("Home function from view")
    #return HttpResponse("<h1>This is index page</h1>"+str(date))
    return render(request, "home.html", data)

def about(request):
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html", {})

def services(request):
    #return HttpResponse("<h1>This is services page</h1>")
    return render(request, "services.html", {})