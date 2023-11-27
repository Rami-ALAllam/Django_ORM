from django.shortcuts import render,redirect
from django.contrib import messages
from .models import show

def show_form(request):
    return render(request,"show_form.html")

def show_create(request):
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        X = show.create(
            request.POST['title'],
            request.POST['network'],
            request.POST['release_date'],
            request.POST['desc'],
        )
        messages.success(request, "Show successfully created")
    return redirect("/shows/"+str(X.id))

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
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/shows/"+request.POST['editshow_id']+"/edit")
    show.update(
        request.POST['editshow_id'],    
        request.POST['title'],
        request.POST['network'],
        request.POST['release_date'],
        request.POST['desc'],
    )
    return redirect("/shows/"+request.POST['editshow_id'])
