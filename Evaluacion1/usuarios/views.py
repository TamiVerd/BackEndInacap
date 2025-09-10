from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('productos:index') # Redirige al inicio después del registro
    else:
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def perfil(request):
    return render(request, 'usuarios/perfil.html')
