

from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.show_form),
    path('shows/create', views.show_create),
    path('shows/<int:id>', views.show_id),
    path('shows/<int:id>/edit', views.show_edit),
    path('shows/<int:id>/destroy', views.show_destroy),
    path('shows/update', views.show_update),
]