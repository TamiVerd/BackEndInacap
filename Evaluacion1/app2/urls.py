# app2/urls.py

from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.productos, name='productos'),
    path('electronica/', views.electronica, name='electronica'),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('ropa/', views.ropa, name='ropa'),
]