from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.bienvenida, name='index'), 
    path('catalogo/', views.catalogo, name='catalogo'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]