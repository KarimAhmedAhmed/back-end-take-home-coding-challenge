import ecommerce
from ecommerce import Check
from ecommerce import Currency
from ecommerce import CurrencyConverter
import sys
import unittest

currency = Currency()

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
# Change The Currency of Products
# Subtotal
a = converter.convert('USD', currency, 35.98)
b = converter.convert('USD', currency, 46.97)
c = converter.convert('USD', currency, 66.96)
d = converter.convert('USD', currency, 60.97)
e = converter.convert('USD', currency, 86.95)
f = converter.convert('USD', currency, 97.94)
# Total
p_a = converter.convert('USD', currency, 38.5182)
p_b = converter.convert('USD', currency, 51.0468)
p_c = converter.convert('USD', currency, 63.8404)
p_d = converter.convert('USD', currency, 64.5078)
p_e = converter.convert('USD', currency, 86.629)
p_f = converter.convert('USD', currency, 99.1576)


# /////////////////////////////////////////////////////////////
arr_a = ["T-SHIRT", "SHOES"]
arr_b = ["T-SHIRT", "SHOES", "T-SHIRT"]
arr_c = ["T-SHIRT", "SHOES", "T-SHIRT", "JACKET"]
arr_d = ["T-SHIRT", "SHOES", "SHOES"]
arr_e = ["T-SHIRT", "SHOES", "T-SHIRT", "JACKET", "JACKET"]
arr_f = ["T-SHIRT", "T-SHIRT", "SHOES", "T-SHIRT", "JACKET", "JACKET"]


class MyTest(unittest.TestCase):

    def setUp(self):

        self.a = Check(arr_a, (a))
        self.b = Check(arr_b, (b))
        self.c = Check(arr_c, (c))
        self.d = Check(arr_d, (d))
        self.e = Check(arr_e, (e))
        self.f = Check(arr_f, (f))

    def runTest(self):

        self.assertEqual(self.a, round(p_a,2))

        self.assertEqual(self.b, round(p_b,2))

        self.assertEqual(self.c, round(p_c,2))

        self.assertEqual(round(self.d, 2), round(p_d,2))

        self.assertEqual(self.e, round(p_e,2))

        self.assertEqual(round(self.f, 2), round(p_f,2))


unittest.TextTestRunner().run(MyTest())
