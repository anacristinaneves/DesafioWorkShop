from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuarios


class RegistroUsuarioForm(UserCreationForm):
    email_usuario = forms.EmailField(label="Informe seu e-mail")
    nome_usuario = forms.CharField(label="Informe seu nome")
    class Meta:
        model = Usuarios
        fields = ['email_usuario', 'nome_usuario', 'password1', 'password2']

class IniciarSessaoForm(AuthenticationForm):
    class Meta:
        model = Usuarios
        fields = ['email_usuario', 'senha_usuario']