##--------------broken restored preveious version below
# import json
# import uuid
# from datetime import datetime, timedelta
# from abc import ABC, abstractmethod

# class Product(ABC): # made internal & not private in order to allow inheritance
#     def __init__(self, name_of_product, category_of_product, date_of_manufacture, expiration_date, price, discount=0):
#         self._name_of_product = name_of_product
#         self._category_of_product = category_of_product
#         self._date_of_manufacture = date_of_manufacture
#         self._expiration_date = expiration_date
#         self._id = str(uuid.uuid4()) # generate unique id for each product => print inventory -> get id -> sell product
#         self._price = price
#         self._discount = discount

#     @property
#     def name_of_product(self):
#         return self._name_of_product # Ex: Carnati

#     @property
#     def category_of_product(self):
#         return self._category_of_product # Ex: meat product

#     @property
#     def date_of_manufacture(self):
#         return self._date_of_manufacture

#     @property
#     def expiration_date(self):
#         return self._expiration_date

#     @property
#     def id(self):
#         return self._id

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

#     @property
#     def discount(self):
#         return self._discount

#     @discount.setter
#     def discount(self, value):
#         self._discount = value

#     def __eq__(self, other): # two products are the same if everything matches except id
#         return (self._name_of_product == other._name_of_product and
#                 self._category_of_product == other._category_of_product and
#                 self._price == other._price and
#                 self._discount == other._discount)

# # Setup inheritance so that each meat category inherits its attributes from Product & gets category automatically populated 
# class MeatFrozen(Product): # when MeatFrozen is initiated the Product class category_of_product is populated with 'meat_frozen'
#     def __init__(self, name_of_product, date_of_manufacture, expiration_date, price, discount=0):
#         super().__init__(name_of_product, 'meat_frozen', date_of_manufacture, expiration_date, price, discount)
#         # can further add attributes which are unique to the category 

# class MeatFresh(Product):
#     def __init__(self, name_of_product, date_of_manufacture, expiration_date, price, discount=0):
#         super().__init__(name_of_product, 'meat_fresh', date_of_manufacture, expiration_date, price, discount)

# class MeatProducts(Product):
#     def __init__(self, name_of_product, date_of_manufacture, expiration_date, price, discount=0):
#         super().__init__(name_of_product, 'meat_products', date_of_manufacture, expiration_date, price, discount)

# class Stock: # dictionary to hold products -> {'products':['product':{attributes}, 'quantity':1]} #h2 standardize structure / modular
#     def __init__(self): # dictionary has: product.id == key & value == {another dictionary}
#         self.products = {} # {another dictionary} == {'key1 == 'product' == string': value1 == object, 'key2 == quantity': 'value2 == 1'}

#         # what seems weak is the comments; how could I clarify & simplify what is going on here: dictionary within dictionary
# # True structure of stock: {"products": ['product': {"_name_of_product": "Carnati", ...}, ]}
# # It's a list with a dictionary for each product; within each dictionary 2x items: {key1=='product':value1==dictionary & key2=='quantity':value2==integer_value  
#     def add_product(self, product):
#         if product.id not in self.products: # verify via id that the product is unique / not already added in stock
#             # product.id == unique_object.unique_id ; self.products == {}
#             print("self.products: ", self.products) # Out: {}
#             self.products[product.id] = {'product': product, 'quantity': 0} # product.id works as key to return product == obj/address & quantity
#             print("self.products[product.id]", self.products[product.id]) 
#         self.products[product.id]['quantity'] += 1 # increase quantity of relevant product type if not already in stock
#         print(f"Added {product.name_of_product} to stock.") # inform user


#     # def add_product(self, product):
#     #     if product.id not in self.products:
#     #         self.products[product.id] = {'product': product, 'quantity': 0}
#     #     self.products[product.id]['quantity'] += 1
#     #     result = f"Added {product.name_of_product} to stock."
#     #     print(result)
#     #     return result    

#     def product_sold(self, product_id): # h2 improve the user interface ; M. takes object & id
#         if product_id in self.products:
#             self.products[product_id]['quantity'] -= 1
#             if self.products[product_id]['quantity'] == 0:
#                 del self.products[product_id]
#             print(f"Product with ID {product_id} sold.")
#         else:
#             print(f"Product with ID {product_id} not found in stock.")

#     # def clear_stock(self): # doesn't work property / what is this
#     #     self.products = {pid: pdata for pid, pdata in self.products.items() if pdata['quantity'] > 0}
#     #     print("Cleared out of stock products.")

#     # def update_stock(self): # remove products which have 'quantity': 0

#     # def apply_discount(self): # fix 4
#     #     today = datetime.now().date()
#     #     for product_data in self.products.values():
#     #         product = product_data['product']
#     #         if product.expiration_date == today + timedelta(days=1):
#     #             product.discount = 0.5  # 50% discount
#     #             product.price *= 0.5
#     #             print(f"Applied discount to {product.name_of_product}.")

#     def apply_discount(self, product_id): # can't pass product.id as argument/parameter 
#         # if product_id in self.products: # verify via id that product exists in stock/dict & which object to apply discount to
#     #         print("product_id", product_id, "is not in stock") # Out: {}
#     #         #print({self.products[product_id]}) # product.id == unique_object.unique_id ; self.products == {}
#         if product_id in self.products:
#             print(self.products[product_id])
#         #     product = self.products[product_id]
#         #     product.price *= 0.1
#         # print(f"Applied discount to {product.name_of_product}.")

#     def display_stock(self):
#         if not self.products:
#             print("No products in stock.")
#         else:
#             for product_data in self.products.values():
#                 product = product_data['product']
#                 quantity = product_data['quantity']
#                 print(f"ID: {product.id}, Name: {product.name_of_product}, Category: {product.category_of_product}, "
#                       f"Price: {product.price}, Discount: {product.discount}, Quantity: {quantity}")

#     def update_stock(self):
#         self.products = {pid: pdata for pid, pdata in self.products.items() if pdata['quantity'] > 0}
#         print("Updated stock, removed products with quantity 0.")    

#     def search_product(self, product_name):
#         found = False
#         for product_data in self.products.values():
#             product = product_data['product']
#             if product.name_of_product.lower() == product_name.lower():
#                 print(f"ID: {product.id}, Name: {product.name_of_product}, Category: {product.category_of_product}, "
#                       f"Price: {product.price}, Discount: {product.discount}, Quantity: {product_data['quantity']}")
#                 found = True
#         if not found:
#             print(f"No product found with the name '{product_name}'.")

#     def save_stock(self, filename): #self.stock
#         with open(filename, 'w') as file:
#             data = {'products': [ #data == {} structure is characteristic to Meat_store.py
#                 {'product': vars(product_data['product']), # if you want to show you understood, then change this dict structure
#                  'quantity': product_data['quantity']} # & make it so everything continues to work
#                 for product_data in self.products.values()
#             ]}
#             json.dump(data, file, indent=4, default=str)
#         print(f"Stock saved to {filename}")

#     def load_stock(self, filename):
#         try:
#             with open(filename, 'r') as file:
#                 data = json.load(file)
#                 self.products = {
#                     item['product']['_id']: {'product': self._deserialize_product(item['product']),
#                                              'quantity': item['quantity']}
#                     for item in data['products']
#                 }
#             print(f"Stock loaded from {filename}")
#         except FileNotFoundError:
#             print(f"File {filename} not found.")

#     def _deserialize_product(self, data): # repopulate each product category / reinstantiate object using data
#         if data['_category_of_product'] == 'meat_frozen':
#             return MeatFrozen(data['_name_of_product'], data['_date_of_manufacture'], data['_expiration_date'], data['_price'], data['_discount'])
#         elif data['_category_of_product'] == 'meat_fresh':
#             return MeatFresh(data['_name_of_product'], data['_date_of_manufacture'], data['_expiration_date'], data['_price'], data['_discount'])
#         elif data['_category_of_product'] == 'meat_products':
#             return MeatProducts(data['_name_of_product'], data['_date_of_manufacture'], data['_expiration_date'], data['_price'], data['_discount'])

# def main():
#     stock = Stock()
#     if input("Do you want to import an existing stock? (yes/no): ").strip().lower() == 'yes':
#         filename = input("Enter the filename: ")
#         stock.load_stock(filename)

#     while True:
#         print("\nChoose an option:")
#         print("1. Add a new product")
#         print("2. Sell a product")
#         print("3. Update stock (remove products with quantity 0)")
#         print("4. Apply discount to expiring products")
#         print("5. Display entire stock")
#         print("6. Search for a product")
#         print("7. Save stock")
#         print("8. Exit")
#         choice = input("Enter your choice: ").strip()

#         if choice == '1':
#             name = input("Enter product name: ")
#             category = input("Enter category (meat_frozen, meat_fresh, meat_products): ")
#             date_of_manufacture = input("Enter date of manufacture (YYYY-MM-DD): ")
#             expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
#             price = float(input("Enter price: "))
#             discount = float(input("Enter discount (default 0): ") or 0)

#             if category == 'meat_frozen':
#                 product = MeatFrozen(name, date_of_manufacture, expiration_date, price, discount)
#             elif category == 'meat_fresh':
#                 product = MeatFresh(name, date_of_manufacture, expiration_date, price, discount)
#             elif category == 'meat_products':
#                 product = MeatProducts(name, date_of_manufacture, expiration_date, price, discount)
#             else:
#                 print("Invalid category.")
#                 continue

#             stock.add_product(product)
#             #assert stock.add_product(product) == f"Added {product.name_of_product} to stock."

#         elif choice == '2':
#             product_id = input("Enter product ID to sell: ")
#             stock.product_sold(product_id)

#         elif choice == '3':
#             stock.update_stock()

#         elif choice == '4':
#             product_id = input("Enter product ID to apply 10% discount: ")
#             stock.apply_discount(product_id)

#         elif choice == '5':
#             stock.display_stock()

#         elif choice == '6':
#             product_name = input("Enter product name to search: ")
#             stock.search_product(product_name)

#         elif choice == '7':
#             filename = input("Enter filename to save stock: ")
#             stock.save_stock(filename) # pass filename to save_stock method

#         elif choice == '8':
#             print("Exiting.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()


##--------------broke above

import json
import uuid
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name_of_product, category_of_product, date_of_manufacture, expiration_date, price, discount=0):
        self._name_of_product = name_of_product
        self._category_of_product = category_of_product
        self._date_of_manufacture = date_of_manufacture
        self._expiration_date = expiration_date
        self._id = str(uuid.uuid4())
        self._price = price
        self._discount = discount

    @property
    def name_of_product(self):
        return self._name_of_product

    @property
    def category_of_product(self):
        return self._category_of_product

    @property
    def date_of_manufacture(self):
        return self._date_of_manufacture

    @property
    def expiration_date(self):
        return self._expiration_date

    @property
    def id(self):
        return self._id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value

    def __eq__(self, other):
        return (self._name_of_product == other._name_of_product and
                self._category_of_product == other._category_of_product and
                self._price == other._price and
                self._discount == other._discount)

class MeatFrozen(Product):
    def __init__(self, name_of_product, date_of_manufacture, expiration_date, price, discount=0):
        super().__init__(name_of_product, 'meat_frozen', date_of_manufacture, expiration_date, price, discount)

class MeatFresh(Product):
    def __init__(self, name_of_product, date_of_manufacture, expiration_date, price, discount=0):
        super().__init__(name_of_product, 'meat_fresh', date_of_manufacture, expiration_date, price, discount)

class MeatProducts(Product):
    def __init__(self, name_of_product, date_of_manufacture, expiration_date, price, discount=0):
        super().__init__(name_of_product, 'meat_products', date_of_manufacture, expiration_date, price, discount)

class Stock:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.id not in self.products:
            self.products[product.id] = {'product': product, 'quantity': 0}
        self.products[product.id]['quantity'] += 1
        print(f"Added {product.name_of_product} to stock.")

    def product_sold(self, product_id):
        if product_id in self.products:
            self.products[product_id]['quantity'] -= 1
            if self.products[product_id]['quantity'] == 0:
                del self.products[product_id]
            print(f"Product with ID {product_id} sold.")
        else:
            print(f"Product with ID {product_id} not found in stock.")

    def clear_stock(self):
        self.products = {pid: pdata for pid, pdata in self.products.items() if pdata['quantity'] > 0}
        print("Cleared out of stock products.")

    def apply_discount(self, product_id):
        if product_id in self.products:
            #print(self.products[product_id]) # OUT: {'product': object_address, 'quantity': 1}
            # want product.price ; have product_id ; have: object address
            #print((self.products[product_id]['product'])) # OUT: self.products[product_id]['product'] == obj.address
            #product_address = self.products[product_id]['product']
            #print(product_address.price) # OUT: price
            #print(self.products[product_id]['product'].price) # OUT: price
            self.products[product_id]['product'].price *= 0.9 # 10% discount applied
            print(f"Product name: {self.products[product_id]['product'].name_of_product} has received a 10% discount. New price: {self.products[product_id]['product'].price}")


        # today = datetime.now().date()
        # for product_data in self.products.values():
        #     product = product_data['product']
        #     if product.expiration_date == today + timedelta(days=1):
        #         product.discount = 0.5  # 50% discount
        #         product.price *= 0.5
        #         print(f"Applied discount to {product.name_of_product}.")

    def display_stock(self):
        if not self.products:
            print("No products in stock.")
        else:
            for product_data in self.products.values():
                product = product_data['product']
                quantity = product_data['quantity']
                print(f"ID: {product.id}, Name: {product.name_of_product}, Category: {product.category_of_product}, "
                      f"Price: {product.price}, Discount: {product.discount}, Quantity: {quantity}")

    def search_product(self, product_name):
        found = False
        for product_data in self.products.values():
            product = product_data['product']
            if product.name_of_product.lower() == product_name.lower():
                print(f"ID: {product.id}, Name: {product.name_of_product}, Category: {product.category_of_product}, "
                      f"Price: {product.price}, Discount: {product.discount}, Quantity: {product_data['quantity']}")
                found = True
        if not found:
            print(f"No product found with the name '{product_name}'.")

    def save_stock(self, filename):
        with open(filename, 'w') as file:
            data = {'products': [
                {'product': vars(product_data['product']),
                 'quantity': product_data['quantity']}
                for product_data in self.products.values()
            ]}
            json.dump(data, file, indent=4, default=str)
        print(f"Stock saved to {filename}")

    def load_stock(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.products = {
                    item['product']['_id']: {'product': self._deserialize_product(item['product']),
                                             'quantity': item['quantity']}
                    for item in data['products']
                }
            print(f"Stock loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def _deserialize_product(self, data):
        if data['_category_of_product'] == 'meat_frozen':
            return MeatFrozen(data['_name_of_product'], data['_date_of_manufacture'], data['_expiration_date'], data['_price'], data['_discount'])
        elif data['_category_of_product'] == 'meat_fresh':
            return MeatFresh(data['_name_of_product'], data['_date_of_manufacture'], data['_expiration_date'], data['_price'], data['_discount'])
        elif data['_category_of_product'] == 'meat_products':
            return MeatProducts(data['_name_of_product'], data['_date_of_manufacture'], data['_expiration_date'], data['_price'], data['_discount'])

def main():
    stock = Stock()
    if input("Do you want to import an existing stock? (yes/no): ").strip().lower() == 'yes':
        filename = input("Enter the filename: ")
        stock.load_stock(filename)

    while True:
        print("\nChoose an option:")
        print("1. Add a new product")
        print("2. Sell a product")
        print("3. Clear out of stock products")
        print("4. Apply 10% discount to product (via ID)")
        print("5. Display entire stock")
        print("6. Search for a product")
        print("7. Save stock")
        print("8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter product name: ")
            category = input("Enter category (meat_frozen, meat_fresh, meat_products): ")
            date_of_manufacture = input("Enter date of manufacture (YYYY-MM-DD): ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            price = float(input("Enter price: "))
            discount = float(input("Enter discount (default 0): ") or 0)

            if category == 'meat_frozen':
                product = MeatFrozen(name, date_of_manufacture, expiration_date, price, discount)
            elif category == 'meat_fresh':
                product = MeatFresh(name, date_of_manufacture, expiration_date, price, discount)
            elif category == 'meat_products':
                product = MeatProducts(name, date_of_manufacture, expiration_date, price, discount)
            else:
                print("Invalid category.")
                continue

            stock.add_product(product)

        elif choice == '2':
            product_id = input("Enter product ID to sell: ")
            stock.product_sold(product_id)

        elif choice == '3':
            stock.clear_stock()

        elif choice == '4':
            product_id = input("Enter product ID to apply 10% discount: ")
            stock.apply_discount(product_id)

        elif choice == '5':
            stock.display_stock()

        elif choice == '6':
            product_name = input("Enter product name to search: ")
            stock.search_product(product_name)

        elif choice == '7':
            filename = input("Enter filename to save stock: ")
            stock.save_stock(filename)

        elif choice == '8':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
