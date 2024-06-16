from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Formulario de inicio de sesión
class login_form(AuthenticationForm):
    username = forms.CharField(
        label=None, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'autofocus': True,
            'required': True,
        }))
    password = forms.CharField(
        label=None, 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'required': True,
        }))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulario de registro
class signup_form(forms.Form):
    first_name = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre',
            'class': 'signup-campo',
            'required': True,
        }))
    last_name = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellido',
            'class': 'signup-campo',
            'required': True,
        }))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo Electrónico',
            'class': 'signup-campo',
            'required': True,
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'signup-campo',
            'required': True,
        }))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)