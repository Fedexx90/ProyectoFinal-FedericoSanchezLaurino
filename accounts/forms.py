from django import forms
from django.contrib.auth.models import User
from .models import Profile

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
