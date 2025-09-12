# usuarios/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Usamos el modelo de Usuario por defecto de Django
        model = User
        # Especificamos los campos que queremos en el formulario
        fields = ('username', 'email')