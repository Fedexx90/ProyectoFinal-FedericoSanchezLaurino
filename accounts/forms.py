from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': '150 caracteres o menos. Solo letras, números y @/./+/-/_ permitidos.',
            'password1': (
                'Tu contraseña debe tener al menos 8 caracteres, '
                'no puede ser una contraseña común ni completamente numérica.'
            ),
            'password2': 'Repite la misma contraseña para confirmarla.',
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']
        labels = {
            'avatar': 'Foto de perfil',
            'bio': 'Biografía',
            'birth_date': 'Fecha de nacimiento',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
