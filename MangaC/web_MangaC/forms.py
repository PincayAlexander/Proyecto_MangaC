from django import forms

class login_form(forms.Form):
    """
    email = forms.EmailField(label=None, widget=forms.EmailInput(attrs={
                    'placeholder': 'email@example.com',
                    'autofocus': True,
                    'class': 'login-campo',
                    'required': True,
    }))
    """
    username = forms.CharField(label=None, widget=forms.TextInput(attrs={
                    'placeholder': 'Usuario',
                    'autofocus': True,
                    'class': 'login-campo',
                    'required': True,
    }))
    password = forms.CharField(label=None, widget=forms.PasswordInput(attrs={
                    'placeholder': 'Contraseña',
                    'class': 'login-campo',
                    'required': True,
    }))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class signup_form(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=200,
                widget=forms.TextInput(attrs={
                    'placeholder': 'Nombre',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
        }))
    last_name = forms.CharField(label="Apellido", max_length=200, 
                widget=forms.TextInput(attrs={
                    'placeholder': 'Apellido',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
    }))
    email = forms.EmailField(label="Correo Electrónico", 
                widget=forms.EmailInput(attrs={
                    'placeholder': 'Correo Electrónico',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
    }))
    password = forms.CharField(label="Contraseña", 
                widget=forms.PasswordInput(attrs={
                    'placeholder': 'Contraseña',
                    'class': 'signup-campo',
                    'autocomplete': 'off',
                    'required': True,
    }))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)