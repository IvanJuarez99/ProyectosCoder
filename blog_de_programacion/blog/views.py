from django.shortcuts import render, redirect
from .forms import ArticuloForm, BusquedaArticuloForm
from .models import Articulo,Autor, Categoria


def buscar_autor(request):
    autor = request.GET.get('autor')
    if autor:
        articulos = Articulo.objects.filter(autor__nombre__icontains=autor)
    else:
        articulos = []
    return render(request, 'blog/buscar_autor.html', {'articulos': articulos})


def buscar_categoria(request):
    categoria = request.GET.get("categoria", "")
    articulos = Articulo.objects.filter(categoria__nombre__icontains=categoria) if categoria else []
    return render(request, 'blog/buscar_categoria.html', {"articulos": articulos})




def buscar_articulos(request):
    query = request.GET.get('query', '')
    
    if query:
        resultados = Articulo.objects.filter(titulo__icontains=query)
    else:
        resultados = None

    todos_los_articulos = Articulo.objects.all()

    form = BusquedaArticuloForm(request.GET)
    return render(request, 'blog/buscar_articulos.html', {'form': form, 'resultados': resultados, 'todos_los_articulos': todos_los_articulos, 'query': query})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():

            autor = form.cleaned_data.get('autor')
            nuevo_autor = form.cleaned_data.get('nuevo_autor')
            if nuevo_autor:
                autor, created = Autor.objects.get_or_create(nombre=nuevo_autor)
            
            categoria = form.cleaned_data.get('categoria')
            nueva_categoria = form.cleaned_data.get('nueva_categoria')
            if nueva_categoria:
                categoria, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
            
            articulo = form.save(commit=False)
            articulo.autor = autor
            articulo.categoria = categoria
            articulo.save()

            return redirect('articulo_list') 

    else:
        form = ArticuloForm()

    return render(request, 'blog/crear_articulo.html', {'form': form})

def articulo_list(request):
    articulos = Articulo.objects.all() 
    return render(request, 'blog/articulo_list.html', {'articulos': articulos})


def inicio(request):
    return render(request, 'blog/inicio.html')
