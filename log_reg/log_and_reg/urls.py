

from django.urls import path
from . import views

urlpatterns = [
    path('', views.form),
    path('register', views.register),
    path('login', views.login),
    path('main', views.main),
    path('logout', views.logout),
]