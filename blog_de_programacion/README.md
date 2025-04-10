# Blog de Programación
En esta aplicación se pueden crear artículos de programación, autores y categorías, y realizar búsquedas por título, nombre del autor o categoria.
Tambien se tendra un perfil exclusivo para cada cuenta.
# *************************************************************

# Funcionalidades incluidas

-  Uso del patrón MVT
-  Herencia de plantillas HTML
-  Modelos en base de datos: `Articulo`, `Autor`, `Categoria`, `Perfil`, `Usuario`, `Contraseña`, `mail`.
-  Formularios para crear instancias de Articulos, con su Autor(el que inicio sesion), y su Categoria
-  Formulario de búsqueda de artículos por título
-  Diseño estilo blog de programación
-  Login de antiguos Trabajos practicos
-  Eliminacion de Cuentas creadas
# *************************************************************

# ¿Cómo probar la app?

cd blog_de_programacion
python manage.py runserver
ingresar a http://127.0.0.1:8000
# *************************************************************

# Estructura

- blog/models.py: Definición de los modelos.

- blog/forms.py: Formularios para crear instancias.

- blog/views.py: Lógica para crear, listar y buscar artículos.

- blog/templates/: Archivos HTML.

- blog/urls.py: Rutas internas.

- blog_de_programacion/urls.py: Rutas principales.
# *************************************************************

# Orden de funcionalidades

1. Inicio del sitio:

- Abrí http://127.0.0.1:8000/

- Verás la página de inicio con enlaces a las secciones del blog.

2. Crear un articulo:

- Ir a: /Nuevo Artículo/

- Completá el formulario con nombre, contenido, autor y categoria.

3. Buscar Articulo por Autor:

- Ir a: /Buscar Autor/

- Escribí el nombre del autor del Articulo.

4. Buscar Categoría:

- Ir a: /Buscar Categoría/

- Ingresá la categoria del Articulo.

5. Buscar Artículo por nombre:

- Ir a: /Buscar Artículo/

- Se listan todos los artículos creados con su título, autor y categoría y se puede buscar uno en particular.

6. Perfil y cerrar sesion:

- Ir a: Tu nombre (esquina derecha) donde podra entrar al perfil del usuario o cerrar sesion.

7. Perfil

- Dentro del perfil podra ver los articulos creados, editarlos o eliminarlos y tambien eliminar la cuenta.

# *************************************************************

# HTML y CCS

- Creados con ChatGPT para darle estetica al blog