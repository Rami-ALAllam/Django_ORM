from django.shortcuts import render, redirect
from .models import book, author

def allbook(request):
    context={
        "books": book.show_all()
    }
    return render(request,"allbook.html",context)

def create_book(request):
    book.create(
        request.POST['title'],
        request.POST['desc']
        )
    return redirect("/")

def book_view(request,id):
    context={
        "onebook":book.show(id),
        "allauthors":author.show_all()
    }

    return render(request,"onebook.html",context)

def author_add(request):
    book.add_author(
        request.POST['author1'],
        request.POST['bk']
        )
    return redirect("/book/"+request.POST['bk'])

def re_turn(request):
    return redirect("/")

def move(request):
    return redirect("/author")

# ===========================================================================

def allauthor(request):
    context={
        "authors": author.show_all()
    }
    return render(request,"allauthor.html",context)

def create_author(request):
    author.create(
        request.POST['fname'],
        request.POST['lname'],
        request.POST['notes']
        )
    return redirect("/author")

def author_view(request,id):
    context={
        "oneauthor":author.show(id),
        "allbooks":book.show_all()
    }

    return render(request,"oneauthor.html",context)

def book_add(request):
    author.add_book(
        request.POST['book1'],
        request.POST['au1']
        )
    return redirect("/author/"+request.POST['au1'])

def re_turn1(request):
    return redirect("/author")

def move1(request):
    return redirect("/")