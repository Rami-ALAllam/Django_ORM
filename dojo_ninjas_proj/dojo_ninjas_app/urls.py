

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form),
    path('result', views.result),
    path('result2', views.result2),
    path('result3', views.result3),
]
