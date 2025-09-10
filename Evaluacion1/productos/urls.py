from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.index, name='catalogo'), # Reutiliza la vista 'index' para el catálogo
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]