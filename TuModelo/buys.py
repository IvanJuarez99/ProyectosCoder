
from currency_pipe import CurrencyPipe

class Compras:


    def __init__(self, store):
        self.store = store


    def mostrar_categorias(self):

        print('-' * 50)
        print("Categorías de compra disponibles:")

        for i, category in enumerate(self.store.stock.keys(), start=1): #enumerar para elegir mas facil la categoria
            print(f"{i}. {category.title()}")
        print('-' * 50)


    def seleccionar_categoria(self):

        while True: #bucle de categorias
            self.mostrar_categorias()
            opcion = input("Escriba el número de la categoría que desea ver o 'S' para finalizar: ").strip().lower()
            print('-' * 50)

            if opcion == 's':
                return 's'

            try:
                opcion = int(opcion)

                if 1 <= opcion <= len(self.store.stock):
                    category = list(self.store.stock.keys())[opcion - 1]
                    return category
                
                else:
                    print("Número de categoría inválido. Intente nuevamente.")
            except ValueError:
                print("Por favor ingrese un número válido.")


    def filtrar_por_categoria(self, categoria):

        if categoria in self.store.stock:
            productos_categoria = self.store.stock[categoria]
            print(f"\nProductos disponibles en la categoría {categoria.title()}:")

            for i, (product, details) in enumerate(productos_categoria.items(), start=1): #enumerar para elegir mas facil el producto
                print(f"{i}. {product.title()} - {CurrencyPipe.transform(details['precio'])} , hay {details['cantidad']} unidades en stock")
            return productos_categoria
        
        else:
            print('-' * 50)
            print(f"Escribió mal el nombre o no hay productos disponibles para la categoría {categoria}.")
            return {}


    def realizar_compras(self, client):
        shopping_cart = []
        total_price = 0 

        while True:
            categoria = self.seleccionar_categoria()

            if categoria == 's':
                break
            productos_categoria = self.filtrar_por_categoria(categoria)

            if not productos_categoria:
                continue

            while True: #bucle de compra

                print('-' * 50)
                product = input("Escriba el número del producto desea comprar o 'S' para cambiar de categoría: ").strip().lower()
                print('-' * 50)

                if product == 's':
                    break

                try: #ingreso del numero correspondiente al producto
                    product = int(product)

                    if 1 <= product <= len(productos_categoria):
                        selected_product = list(productos_categoria.keys())[product - 1]

                        if productos_categoria[selected_product]["cantidad"] > 0:
                            price = productos_categoria[selected_product]["precio"]
                            client.buy_product(selected_product, self.store)
                            shopping_cart.append({
                                "product": selected_product.title(),
                                "category": categoria.title(),
                                "price": price
                            })
                            total_price += price
                            print("Carrito de compras:")

                            for item in shopping_cart:
                                print(f"- {item['product']} (Categoría: {item['category']}) - {CurrencyPipe.transform(item['price'])}")
                            print(f"\nTotal hasta ahora: {CurrencyPipe.transform(total_price)}")
                            print('-' * 50)

                        else:
                            print(f"El producto {selected_product.title()} no está disponible o está agotado.")
                            print('-' * 50)

                    else:
                        print(f"El número de producto {product} no es válido.")
                except ValueError:
                    print("Por favor ingrese un número válido.")
                    continue

                continuar = input("\n¿Desea seguir comprando productos en esta categoría? (s/n): ").strip().lower()

                if continuar == 's':
                    productos_categoria = self.filtrar_por_categoria(categoria) 
                    continue 

                elif continuar != 's':
                    break 

        if shopping_cart:
            print('-' * 50)
            confirm = input("¿Desea confirmar la compra? (s/n): \n").strip().lower()

            if confirm == 's':
                print('-' * 50)
                print("Información del cliente:")
                print(client.customer_info())
                print('-' * 50)
                print(f"Compra confirmada. Total a pagar: {CurrencyPipe.transform(total_price)}")
                print('-' * 50)
                print('-' * 50)
                print("Gracias por su compra")
                print('-' * 50)
            else:
                print("\nCompra cancelada.\n")
                print('-' * 50)
                print("Gracias por su visita")
                print('-' * 50)
                shopping_cart = []
        display = input("Desea ver el stock? (s/n): ").strip().lower()

        if display == 's':
            print('-' * 50)
            self.store.display_stock()
            print('-' * 50)