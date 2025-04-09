from stock import Store
from customer import Customer
class Carrito_Compras:
    def shopping ():
            while True:
                store.display_stock()  # Mostrar el stock disponible
                product = input("¿Qué producto desea comprar? (o 'salir' para finalizar): ")

                if product.lower() == 'salir':
                    break
                
                # Verificar si hay stock disponible para el producto
                if product in store.stock and store.stock[product] > 0:
                    client.buy_product(product, store)  # Agregar el producto a la lista de compras del cliente
                    shopping_cart.append(product)  # Agregar el producto al carrito

                    print(f"Producto {product} agregado al carrito.")
                    
                    # Mostrar el carrito de compras
                    print("\nCarrito de compras:")
                    for item in shopping_cart:
                        print(f"- {item}")
                else:
                    print(f"El producto {product} no está disponible o está agotado.")
                    continue  # Si no hay stock, continúa al siguiente ciclo

                # Preguntar si el cliente desea continuar comprando
                continuar = input("\n¿Desea seguir comprando? (s/n): ").strip().lower()
                if continuar != 's':
                    break  # Salir del bucle si no desea seguir comprando

            # Confirmar la compra
            if shopping_cart:
                confirm = input("\n¿Desea confirmar la compra? (s/n): ").strip().lower()
                if confirm == 's':
                    print("\nCompra confirmada.")
                    for product in shopping_cart:
                        store.purchase_product(product)  # Reducir el stock
                        client.buy_product(product, store)  # Agregar el producto a las compras del cliente

                else:
                    print("\nCompra cancelada.")
                    shopping_cart = []  # Vaciar el carrito si la compra es cancelada

            # Mostrar la información del cliente
            print("\nInformación del cliente:")
            print(client.customer_info())
            
            # Mostrar el stock actualizado después de las compras
            store.display_stock()