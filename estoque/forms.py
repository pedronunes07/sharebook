from django import forms
from .models import Livro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'paginas', 'preco']

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']