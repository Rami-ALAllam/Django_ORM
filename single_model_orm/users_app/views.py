from django.shortcuts import render, redirect
from .models import users

def form(request):
    context = {
        "all_the_users": users.show_all(users)
    }
    return render(request,"form.html",context)

def handle(request):
    users.create_user(
        request.POST['first_name'],
        request.POST['last_name'],
        request.POST['email'],
        request.POST['age']
        )
    return redirect('/')