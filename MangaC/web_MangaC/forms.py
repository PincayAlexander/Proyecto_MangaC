from django import forms

class login_form(forms.Form):
    email = forms.EmailField(label=None, widget=forms.EmailInput(attrs={
                    'placeholder': 'email@example.com',
                    'autofocus': True,
                    'class': 'login-campo',
                    'required': True,
    }))
    contraseña = forms.CharField(label=None, widget=forms.PasswordInput(attrs={
                    'placeholder': 'Contraseña',
                    'class': 'login-campo',
                    'required': True,
    }))
        


class signup_form(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200,
                widget=forms.TextInput(attrs={
                    'placeholder': 'Nombre',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
        }))
    apellido = forms.CharField(label="Apellido", max_length=200, 
                widget=forms.TextInput(attrs={
                    'placeholder': 'Apellido',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
    }))
    correo = forms.EmailField(label="Correo Electrónico", 
                widget=forms.EmailInput(attrs={
                    'placeholder': 'Correo Electrónico',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
    }))
    contraseña = forms.CharField(label="Contraseña", 
                widget=forms.PasswordInput(attrs={
                    'placeholder': 'Contraseña',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
    }))