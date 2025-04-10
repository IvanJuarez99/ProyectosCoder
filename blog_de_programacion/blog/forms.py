from django import forms
from .models import Autor, Categoria, Articulo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
    'username': 'No se permiten espacios, tildes (á, é, í, ó, ú) ni símbolos especiales como #, !, &, *.',
}

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

from django import forms
from .models import Autor, Categoria, Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor', 'categoria']
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'categoria': 'Categoría',
        }

    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=False, label="Autor")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label="Categoría")

    nuevo_autor = forms.CharField(max_length=100, required=False, label="Nuevo Autor")
    nueva_categoria = forms.CharField(max_length=50, required=False, label="Nueva Categoría")


class BusquedaArticuloForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Buscar Artículo')
