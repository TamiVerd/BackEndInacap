from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Estas son las dos líneas que probablemente te faltan
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/', views.perfil_usuario, name='perfil'),

    # Estas dos ya las tenías
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]