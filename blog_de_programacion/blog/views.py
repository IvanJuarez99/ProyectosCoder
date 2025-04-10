from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticuloForm, BusquedaArticuloForm, RegistroUsuarioForm
from .models import Articulo,Autor, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib import messages


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            Autor.objects.get_or_create(user=user, nombre=user.username)
            login(request, user)
            autor = Autor.objects.get(user=user)
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'blog/registro.html', {'form': form})


@login_required
def perfil_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    articulos = Articulo.objects.filter(autor=autor)
    es_mi_perfil = request.user == autor.user

    return render(request, 'blog/perfil.html', {
        'autor': autor,
        'articulos': articulos,
        'es_mi_perfil': es_mi_perfil,
    })

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)


    if articulo.autor.user != request.user:
        return HttpResponseForbidden("No tenés permiso para editar este artículo.")
    
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('perfil_autor', autor_id=articulo.autor.id)

    else:
        form = ArticuloForm(instance=articulo)

    return render(request, 'blog/editar_articulo.html', {'form': form, 'articulo': articulo})

@login_required
def eliminar_articulo(request, pk):
    try:
        articulo = Articulo.objects.get(pk=pk)
    except Articulo.DoesNotExist:

        return redirect('articulo_list') 

    if articulo.autor.user != request.user:
        return HttpResponseForbidden("No tenés permiso para eliminar este artículo.")
    
    articulo.delete()
    return redirect('perfil_autor', autor_id=articulo.autor.id) 

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
    
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
        return redirect('inicio')

    return render(request, 'blog/eliminar_cuenta.html')

@login_required
def buscar_autor(request):
    autor = request.GET.get('autor')
    if autor:
        articulos = Articulo.objects.filter(autor__nombre__icontains=autor)
    else:
        articulos = []


    todos_los_autores = Autor.objects.all()

    return render(request, 'blog/buscar_autor.html', {
        'articulos': articulos,
        'todos_los_autores': todos_los_autores
    })

@login_required
def buscar_categoria(request):
    categoria = request.GET.get("categoria", "")
    articulos = Articulo.objects.filter(categoria__nombre__icontains=categoria) if categoria else []
    todas_las_categorias = Categoria.objects.all()
    
    return render(request, 'blog/buscar_categoria.html', {
        "articulos": articulos,
        "todas_las_categorias": todas_las_categorias
    })



@login_required
def buscar_articulos(request):
    query = request.GET.get('query', '')
    
    if query:
        resultados = Articulo.objects.filter(titulo__icontains=query)
    else:
        resultados = None

    todos_los_articulos = Articulo.objects.all()

    form = BusquedaArticuloForm(request.GET)
    return render(request, 'blog/buscar_articulos.html', {'form': form, 'resultados': resultados, 'todos_los_articulos': todos_los_articulos, 'query': query})
@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            nueva_categoria = form.cleaned_data.get('nueva_categoria')

            if nueva_categoria:
                categoria, _ = Categoria.objects.get_or_create(nombre=nueva_categoria)


            autor, _ = Autor.objects.get_or_create(
                user=request.user,
                defaults={
                    'nombre': request.user.username,
                    'especialidad': 'Sin especialidad',
                    'biografia': 'Biografía no disponible.'
                }
            )

            articulo = form.save(commit=False)
            articulo.autor = autor
            articulo.categoria = categoria
            articulo.save()

            return redirect('articulo_list')

    else:
        form = ArticuloForm()

    return render(request, 'blog/crear_articulo.html', {'form': form})

@login_required
def articulo_list(request):
    articulos = Articulo.objects.all() 
    return render(request, 'blog/articulo_list.html', {'articulos': articulos})

@login_required
def inicio(request):
    return render(request, 'blog/inicio.html')
