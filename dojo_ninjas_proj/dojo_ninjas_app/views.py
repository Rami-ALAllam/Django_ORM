from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def form(request):
    context = {
        "dojos": Dojo.show_all(Dojo),
    }
    return render (request,"form.html",context)

def result(request):
    Dojo.create_dojo(
        request.POST['name'],
        request.POST['city'],
        request.POST['state'],
    )
    return redirect('/')

def result2(request):
    Ninja.create_ninja(
        request.POST['fname'],
        request.POST['lname'],
        request.POST['dojo'],
        )
    return redirect('/')

def result3(request):
    Dojo.delete_dojo(
        request.POST['dojodel'],
        )
    return redirect('/')

