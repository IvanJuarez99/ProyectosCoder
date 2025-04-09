
from customer import Customer
from stock import Store
from buys import Compras
#si no sabe que hacer, use:
#nicolas@coderhouse.com
#cesar@coderhouse.com
def main():
    #stock del json
    store = Store('stock.json')
    compras = Compras(store)
    
    print('-' * 50)
    print("Bienvenido a AzaPC tienda de productos de computadoras.")
    print('-' * 50)
    # Registro o login
    while True:
        option = input("¿Desea registrarse , iniciar sesión o ver el stock? (R para registrar/I para ingresar/S para Stock): ").strip().lower()
        print("Puede utilizar 'Q' para salir en cualquier momento del registro o login.")
        print('-' * 50)

        if option == 'r':
            print('-' * 50)
            print("*Registro de nuevo cliente*:")
            name = input("Ingrese su Nombre: ").strip()
            if name.lower() == 'q':
                    print("Saliendo del registro. Gracias por su visita.")
                    return
            while True:
                mail = input("Ingrese su Correo: ").strip()
                if mail.lower() == 'q':
                    print("Saliendo del registro. Gracias por su visita.")
                    return

                if "@" in mail and (mail.endswith(".com") or mail.endswith(".ar")) and " " not in mail:
                    break 

                else:
                    print("Correo inválido. Asegúrese de que no contenga espacios")
            customer_instance = Customer(name, mail, "")
            customers = customer_instance.load_from_json() 

            if any(customer['mail'] == mail for customer in customers):
                print("El correo ya está en uso. Por favor, intente con otro correo.")
                continue

            while True:
                phone = input("Ingrese su numero de telefono (debe contener 12 dígitos incluido el codigo de pais con'+'): ").strip()
                if phone.lower() == 'q':
                    print("Saliendo del registro. Gracias por su visita.")
                    return
                if phone.startswith("+") and len(phone) == 13 and phone[1:].isdigit(): 
                    break 

                else:
                    print("El número de teléfono debe tener exactamente 12 dígitos y el codigo de pais incluyendo '+'. Por favor, intente de nuevo.")
            new_client = Customer(name, mail, phone)
            new_client.save_to_json()
            print(f"Cliente {new_client.name.title()} registrado con exito.")
            logged_in_client = customer_instance.login(mail)

            if logged_in_client:
                client = Customer(logged_in_client['name'], logged_in_client['mail'], logged_in_client['phone'])
                compras.realizar_compras(client)

            else:
                print("No se pudo iniciar sesión después del registro. Intente de nuevo.")
                continue  

        elif option == 'i':
            print("*Inicio de sesión*:")
            mail = input("Ingrese su correo: ")   # mail para iniciar sesión porque hay 1 por persona en el mundo (en teoria)
            if mail.lower() == 'q':
                    print("Saliendo del login. Gracias por su visita.")
                    return
            special_greetings = {
                                "nicolas@coderhouse.com": "Hola profesor, lo estaba esperando, que se divierta probando el programa.",
                                "cesar@coderhouse.com": "Hola profesor, lo estaba esperando, que se divierta probando el programa."
                }
            customer_instance = Customer("", mail, "")
            logged_in_client = customer_instance.login(mail)

            if logged_in_client:
                client = Customer(logged_in_client['name'], logged_in_client['mail'], logged_in_client['phone'])

                if mail in special_greetings:
                    print('-' * 50)
                    print(special_greetings[mail])
                compras.realizar_compras(client)
                break 

            else:
                print("Correo no registrado o incorrecto. Intente de nuevo.")
                continue 

        elif option == 's':
            print('-' * 50)
            store.display_stock()
            print('-' * 50)
        elif option == 'q':  # Opción para salir
            print("Gracias por venir,Hasta la próxima.")
            print('-' * 50)
            break         
        else:
            print("Opción inválida. Por favor, ingrese 'R' para registrarse, 'I' para iniciar sesión o 'S' para ver el stock.")
            continue
main()




