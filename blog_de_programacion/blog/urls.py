from django.urls import path
from . import views


urlpatterns = [
    path('buscar_autor/', views.buscar_autor, name='buscar_autor'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('articulos/', views.articulo_list, name='articulo_list'),
    path('buscar_categoria/', views.buscar_categoria, name='buscar_categoria'),
    path('buscar_articulos/', views.buscar_articulos, name='buscar_articulos'),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    
]
