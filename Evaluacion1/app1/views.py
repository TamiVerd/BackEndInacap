# app1/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html')

def productos(request):
    return render(request, 'app2/productos.html')