from django.shortcuts import render,redirect
from .models import show

def show_form(request):
    return render(request,"show_form.html")

def show_create(request):
    show.create(
        request.POST['title'],
        request.POST['network'],
        request.POST['release_date'],
        request.POST['desc'],
    )
    return redirect("/shows")

def shows(request):
    context={
    "allshows":show.show_all()
    }
    return render(request,"show_all.html",context)

def show_id(request,id):
    context={
        "oneshow":show.show_id(id)
    }
    return render(request,"Show_id.html",context)

def show_edit(request,id):
    context={
        "editshow":show.show_id(id)
    }
    return render(request,"show_edit.html",context)

def show_destroy(request,id):
    show.show_delete(id)
    return redirect("/shows")

def show_update(request): 
    show.update(
        request.POST['editshow_id'],    
        request.POST['title'],
        request.POST['network'],
        request.POST['release_date'],
        request.POST['desc'],
    )
    return redirect("/shows/"+request.POST['editshow_id'])