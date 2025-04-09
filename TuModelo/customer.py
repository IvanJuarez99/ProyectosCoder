from currency_pipe import CurrencyPipe
import json
import os

class Customer:
    def __init__(self, name, mail, phone):
        self.name = name
        self.mail = mail
        self.phone = phone
        self.purchased_products = [] 


    def __str__(self):
        return f"Cliente: {self.name}, Correo: {self.mail}, Teléfono: {self.phone}"


    def save_to_json(self, filename='clientes.json'): # JSON de clientes
        customers = self.load_from_json(filename)

        for customer in customers:

            if customer['mail'] == self.mail:
                return
            
        new_customer = {
            'name': self.name,
            'mail': self.mail,
            'phone': self.phone
        }
        customers.append(new_customer)
        with open(filename, 'w') as file:
            json.dump(customers, file, indent=4)


    def load_from_json(self, filename='clientes.json'):

        if not os.path.exists(filename):
            return []
        
        with open(filename, 'r') as file:
            customers = json.load(file)
        return customers
    

    def login(self, mail, filename='clientes.json'):
        customers = self.load_from_json(filename)

        for customer in customers:

            if customer['mail'] == mail:
                return customer
        return None


    def buy_product(self, product, store):

        for category, products in store.stock.items():

            if product in products:
                product_info = products[product]
                category_name = category
                price = product_info["precio"]
                self.purchased_products.append({
                    "product": product,
                    "category": category_name,
                    "price": price
                })

                if store.purchase_product(product):
                    print(f"Se agregó {product} al carrito de compras de {self.name}")
                    print('-' * 50)

                else:
                    print(f"No se pudo comprar el producto {product} debido a stock insuficiente.")


    def customer_info(self): # Información del cliente en el ticket

        if self.purchased_products:
            product_details = []

            for item in self.purchased_products:
                product_details.append(f"{item['category'].title()} - {item['product'].title()}: {CurrencyPipe.transform(item['price'])}")
            products_info = '\n'.join(product_details)
            
        else:
            products_info = "No ha comprado productos aún"
        print (f"Cliente: {self.name}\nCorreo: {self.mail}\nTelefono: {self.phone}\nProductos comprados:\n{products_info}")
        return ('-' * 50)
