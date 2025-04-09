import json
import os
from currency_pipe import CurrencyPipe

class Store:


    def __init__(self, filename):
        self.filename = filename
        self.stock = self.load_from_json(filename)


    def load_from_json(self, filename): #stock guardado en JSON
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"El archivo {filename} no se encontró.")
            return {}


    def display_stock(self):
        print("Stock actual:")

        for category, products in self.stock.items():
            print(f"{category.title()}:")

            for product, details in products.items():
                print(f"  - {product.title()}: {details['cantidad']} unidades - {CurrencyPipe.transform(details['precio'])}")


    def display_categories(self):
        print('-' * 50)
        print("Categorías de compra disponibles:")

        for category in self.stock:
            print(f"- {category.title()}")


    def purchase_product(self, product):

        for category, products in self.stock.items():

            if product in products:

                if products[product]["cantidad"] > 0:
                    self.stock[category][product]["cantidad"] -= 1
                    self.save_to_json()
                    return True
                
                else:
                    print(f"No hay stock disponible para el producto {product.title()}.")
                    return False
        print(f"El producto {product.title()} no está disponible.")
        return False


    def save_to_json(self, filename="stock.json"):
        with open(filename, 'w') as file:
            json.dump(self.stock, file, indent=4)            