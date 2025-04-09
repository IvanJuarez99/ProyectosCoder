#biblioteca random para sugerir nombres con numeros

import random

#Registro de usuario
#Input con "lower"para evitar errores de sintaxis
#El usuario no puede estar vacio
#Si el nombre esta en uso se le da sugerencias con 3 numeros random
#Registro de contraseña
#La contraseña no puede estar vacia
#Se guarda el usuario y la contraseña en el diccionario USUARIOS

def registrar_usuario(usuarios):
    print("\n-- Registrar nuevo usuario --")
    nombre = input("Ingrese el nombre de usuario: ").lower()
    if nombre == "":
        print("\nEl nombre de usuario no puede estar vacío.")
        return 

    if nombre in usuarios:
        sugerencias= []
        for _ in range (3):
            numero_aleatorio = random.randint(100, 999)
            sugerencias.append(f"{nombre}{numero_aleatorio}")
        print(f"\nEl nombre de usuario: {nombre} ya existe. Sugerencias:")
        for sugerencia in sugerencias:
            print(f"-{sugerencia}")
        return 

    contrasena = input("Ingrese la contraseña: ")
    if contrasena == "":
        print("\nLa contraseña no puede estar vacía.")
        return

    usuarios[nombre] = contrasena
    print(f"\nUsuario {nombre} registrado exitosamente")

#Muestra de usuarios
#Se utiliza "len" para ver la cantidad de usuarios, en caso de ser 0 lo muestra
#Se usa el bucle "for" para imprimir usuario por usuario

def mostrar_usuarios(usuarios):
    if len(usuarios) == 0:
        print("\nNo hay usuarios registrados.")
    else:
        print("\n-- Usuarios Registrados --\n")
        for nombre, contrasena in usuarios.items():
            # print(f"Usuario: {nombre}, Contraseña: {contrasena}")
            print(f"Usuario: {nombre}, Contraseña: {len(contrasena)*'*'}")

#Inicio de Sesion
#se usa 2 if 2 else para corroborar si el usuario y la contraseña son correctos por separado

def Ingreso(usuarios):
    print("\n-- Iniciar Sesion --")
    nombre = input("\nIngrese su usuario: ").lower()
    contraseña = input ("Ingrese su contraseña: ")
    if nombre in usuarios:
        if usuarios[nombre]==contraseña :
            print(f"\nIngreso correctamente")
        else:
            print("\nContraseña incorrecta\n¿Olvido su contraseña?")
    else:
        print("\nUsuario incorrecto\n¿Olvido su usuario?")

#Menu de opciones
#Es una funcion que llama al resto de funciones (Me dio la idea el tutor Nico :D)
#Se utiliza el bucle while para repetir las opciones
#Menu sumple con input, if, elif y else
#Break para salir del programa
#En caso de no ingresar una opcion mostrada sea cual sea, imprime opcion invalida 

def opciones():
    #Diccionario donde se guardaran los usuarios y contraseñas
    usuarios = {}
    while True:
    
        print("\n-- Menú de opciones --")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Ingresar")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")    

        
        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            mostrar_usuarios(usuarios)
        elif opcion == "3":
            Ingreso(usuarios)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor elige una opción válida.")

#Llama al menu de opciones que llama al resto de funciones dependiendo de la opcion ingresada

opciones()