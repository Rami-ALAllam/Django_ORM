
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allbook),
    path('create_bk', views.create_book),
    path('book/<int:id>', views.book_view),
    path('authoradd', views.author_add),
    path('return', views.re_turn),
    path('author', views.allauthor),
    path('create_author', views.create_author),
    path('author/<int:id>', views.author_view),
    path('bookadd', views.book_add),
    path('return1', views.re_turn1),
    path('move', views.move),
    path('move1', views.move1),
]