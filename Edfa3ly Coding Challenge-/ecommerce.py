import sys
import csv
from sys import argv
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from collections import Counter

# To get the currency
def Currency():
    return argv[1]

# Handle and get the arguments
if len(argv) > 0:

    length = len(argv)
    arr = []
    for i in range(2, length):

        arr.append(
            argv[i].upper()
        )



# Adapter Structural Pattern
class Tshirt:
    def __init__(self):
        self.name = "Tshirt"

    def PriceofTshirt(self):
        return 10.99

class Pants:
    def __init__(self):
        self.name = "Pants"

    def PriceofPants(self):
        return 14.99
        

class Jacket:
    def __init__(self):
        self.name = "Jacket"

    def PriceofJacket(self):
        return 19.99
        

class Shoes:
    def __init__(self):
        self.name = "Shoes"

    def PriceofShoes(self):
        return 24.99


# Change Currency
class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount




class Adapter:

    def __init__(self, object, **adapted_method):
        self._object = object

        self.__dict__.update(adapted_method) 

    def __getattr__(self, attr):
        return getattr(self._object, attr)




# Create an array
objects = []

Tshirt = Tshirt()
Pants = Pants()
Jacket = Jacket()
Shoes = Shoes()

# Append Products in the array 
objects.append(Adapter(Tshirt, cost = Tshirt.PriceofTshirt))
objects.append(Adapter(Pants, cost = Pants.PriceofPants))
objects.append(Adapter(Jacket, cost = Jacket.PriceofJacket))
objects.append(Adapter(Shoes, cost = Shoes.PriceofShoes))


# Change The Currency of Products
currency = Currency()
url = 'https://api.exchangerate-api.com/v4/latest/USD'
Tshirt_Price = CurrencyConverter(url).convert('USD', currency, objects[0].cost())
Pants_Price = CurrencyConverter(url).convert('USD', currency, objects[1].cost())
Jacket_Price = CurrencyConverter(url).convert('USD', currency, objects[2].cost())
Shoes_Price = CurrencyConverter(url).convert('USD', currency, objects[3].cost())


# # if the customer write the products in lower or upper case
# for i in arr:
#     i = i.upper()


# Calculate the Subtotal of products
subtotal = 0
for i in arr:
    if i == "T-SHIRT":
        subtotal += Tshirt_Price
    elif i == "PANTS":
        subtotal += Pants_Price
    elif i == "JACKET":
        subtotal += Jacket_Price
    elif i == "SHOES":
        subtotal += Shoes_Price
subtotal = round(subtotal, 2)
print(f"Subtotal: {currency}{subtotal}")


# Count the Number of occurrences
def countX(arr, name):
    return arr.count(name)


# Calculate the discounts
def Check(arr, subtotal):
    # Variables
    Name_Tshirt = "T-SHIRT"
    Name_Jacket = "JACKET"
    Name_Shoes = "SHOES"
    Jacket_Actual_Discout = 0

    # Calculate the Taxes 14% of products
    taxes = round((0.14*subtotal), 3)

    # Check if the customer has 2 T-shirts or more and has a jacket to discount
    if countX(arr, Name_Tshirt) >= 2:

        Jacket_discounts = int(countX(arr, Name_Tshirt)/2)
        Jacket_count = int(countX(arr, Name_Jacket))
        if Jacket_count <= Jacket_discounts:

            subtotal -= round(Jacket_count*(0.5*Jacket_Price), 3)
            Jacket_Actual_Discout = Jacket_count
        else:
            subtotal -= round(Jacket_discounts*(0.5*Jacket_Price), 3)
            Jacket_Actual_Discout = Jacket_discounts


# Get ---How many shoes there? and calculate the discounts
    Shoes_count = int(countX(arr, Name_Shoes))
    subtotal -= Shoes_count*0.1*Shoes_Price
    print(f"Taxes: {currency}{taxes}")

# Print Discounts of Jackets
    if Jacket_Actual_Discout > 0 and Shoes_count > 0:
        print(
            f"Discounts:\n 10% off {Shoes_count} shoes: -{currency}{round((Shoes_count*0.1*Shoes_Price),2)} \n 50% off {Jacket_Actual_Discout} jacket: -{currency}{round((Jacket_Actual_Discout*(0.5*Jacket_Price)),2)}")
#    Print Discounts of Shoes

    elif Shoes_count > 0:
        print(
            f"Discounts:\n 10% off {Shoes_count} shoes: -{currency}{round((Shoes_count*0.1*Shoes_Price),2)}")

    elif Jacket_Actual_Discout > 0:
        print(
            f"Discounts:\n 50% off {Jacket_Actual_Discout} jacket: -{currency}{round((Jacket_Actual_Discout*(0.5*Jacket_Price)),2)}")
# Add taxes to subtotal
    subtotal = round((subtotal + taxes), 2)
    print(f"Total: {currency}{subtotal}")
    return subtotal


# Call Function Check
total_check = Check(arr, subtotal)


