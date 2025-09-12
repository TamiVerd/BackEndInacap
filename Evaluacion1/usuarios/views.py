# usuarios/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu cuenta ha sido creada exitosamente! Ya puedes iniciar sesión.')
            return redirect('productos:index') 
    else:
<<<<<<< Updated upstream
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def perfil(request):
    return render(request, 'usuarios/perfil.html')
=======
        form = CustomUserCreationForm()

    return render(request, 'usuarios/registrousuario.html', {'form': form})

def perfil_usuario(request):
    """
    Esta es la función que faltaba.
    Por ahora, solo muestra la página de perfil.
    """
    return render(request, 'usuarios/perfil.html')
>>>>>>> Stashed changes
