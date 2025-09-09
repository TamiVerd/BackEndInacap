# app2/views.py

from django.shortcuts import render

# Vista para la página de productos (todas las categorías)
def productos(request):
    return render(request, 'app2/productos.html')

# Vista para la categoría de Electrónica
def electronica(request):
    return render(request, 'app2/electronica.html')

# Vista para la categoría de Juguetes
def juguetes(request):
    return render(request, 'app2/juguetes.html')

# Vista para la categoría de Ropa
def ropa(request):
    return render(request, 'app2/ropa.html')