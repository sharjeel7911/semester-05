# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:30:32 2026

@author: faiza.khadim
"""
#T1
class Currency:
    def __init__(self, amount, code):
        self.amount = amount
        self.code = code

    def __add__(self, other):

        if self.code != other.code:
            raise ValueError("Currency codes do not match!")
        return Currency(self.amount + other.amount, self.code)

    # def __str__(self):
    #     return f"{self.code} {self.amount:,.2f}"

    def __repr__(self):
        return f"Currency(amount={self.amount}, code='{self.code}')"

# Creating Currency objects
c1 = Currency(3000, "PKR")
c2 = Currency(2000, "PKR")

# Adding two Currency objects
c3 = c1 + c2
print(c3)
# Developer-friendly representation
#print(repr(c3))
# Trying to add different currencies
c4 = Currency(100, "USD")
try:
    print(c1 + c4)
except ValueError as e:
    print(e)
# %% T2
class Component:
    def startup(self):
        print("Component Starting...")
class PowerDevice(Component):
    def startup(self):
        print("Power Grid Connected")
        super().startup()
class NetworkDevice(Component):
    def startup(self):
        print("Network Connected")
        super().startup()
class SmartLift(PowerDevice, NetworkDevice):
    def startup(self):
        print("Smart Lift Initializing...")
        super().startup()
# Creating object
lift = SmartLift()
# Starting the smart lift
lift.startup()
print(f"MRO Order: {[c.__name__ for c in SmartLift.mro()]}")
# %%

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShippingMixin:
    def __init__(self, weight):
        self.weight = weight

    def calculate_freight(self):
        # $10 per kg (rounded up), minimum $10
        return max(10, self.weight * 10)

class DiscountMixin:
    def apply_discount(self, percent):
        self.price = self.price - self.price * percent / 100


class Laptop(Product, ShippingMixin, DiscountMixin):
    def __init__(self, name, price, weight):
        Product.__init__(self, name, price)
        ShippingMixin.__init__(self, weight)


# Sample Call
macbook = Laptop(name="Macbook Air", price=1200, weight=1.2)
macbook.apply_discount(10)
print(f"Price after 10% discount: ${macbook.price:.2f}")
print(f"Freight: ${macbook.calculate_freight()}")
# %%
class Product:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.price = kwargs["price"]

class ShippingMixin:
    def __init__(self, **kwargs):
        self.weight = kwargs["weight"]

    def calculate_freight(self):
        return max(10, self.weight * 10)

class DiscountMixin:
    def apply_discount(self, percent):
        self.price = self.price - self.price * percent / 100

class Laptop(Product, ShippingMixin, DiscountMixin):

    def __init__(self, **kwargs):

        Product.__init__(self, **kwargs)
        ShippingMixin.__init__(self, **kwargs)

# Sample Call
macbook = Laptop(name="Macbook Air", price=1200, weight=1.2)
macbook.apply_discount(10)

print(f"Price after 10% discount: ${macbook.price:.2f}")
print(f"Freight: ${macbook.calculate_freight()}")

# %%

from abc import ABC, abstractmethod
# 1. PaymentProvider Base Class
class PaymentProvider(ABC):
    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def settle(self, amount):
        pass

# 2. CreditCardPay Abstract Class
class CreditCardPay(PaymentProvider):
    def __init__(self, card_number, card_holder, expiry_date):
        self.card_number = card_number      # 20 digits
        self.card_holder = card_holder
        self.expiry_date = expiry_date

    def display_card(self):
        # Displays only the last 4 digits
        return f"Card Ending In: {self.card_number[-4:]}"

# 3. StripePay Class
class StripePay(PaymentProvider):
    def __init__(self, api_key):
        self.api_key = api_key

    def authorize(self, amount):
        fee = amount * 0.025
        print(f"Stripe Authorized: {amount}. Surcharge Fee (2.5%): {fee}")

    def settle(self, amount):
         print(f"Stripe Settled: {amount}")
    
# 4. VisaPay Class
class VisaPay(CreditCardPay):
    def authorize(self, amount):
        print(f"Visa Authorized: {amount} for {self.display_card()}")

    def settle(self, amount):
        fee_percentage = amount * 0.025
        fee = min(fee_percentage, 10.0)
        print(f"Visa Settled: {amount}. Surcharge Fee: {fee}")

# 5. UnionPay Class
class UnionPay(CreditCardPay):
    def authorize(self, amount):
        print(f"UnionPay Authorized: {amount} for {self.display_card()}")

    def settle(self, amount):
        fee = 8.0
        print(f"UnionPay Settled: {amount}. Flat Surcharge Fee: {fee}")

# 6. RaastPay Class
class RaastPay(CreditCardPay):
    def authorize(self, amount):
        print(f"RaastPay Authorized: {amount} for {self.display_card()}")

    def settle(self, amount):
        print(f"RaastPay Settled: {amount}. No surcharge applied.")

# 7. Validation Class (Missing settle method)
class GenericPayment(PaymentProvider):
    def authorize(self, amount):
        print(f"Generic Authorized: {amount}")
    # Missing settle() method intentionally to test ABC enforcement

# Verification and Sample Execution
if __name__ == "__main__":
    print("--- Running Sample Call for StripePay ---")
    pay = StripePay(api_key="sk_test_123")
    pay.authorize(50.0)
    pay.settle(50.0)

    print("\n--- Verifying GenericPayment Block ---")
    try:
        generic = GenericPayment()
    except TypeError as e:
        print(f"Success! Cannot instantiate GenericPayment: {e}")
# %%
class Signal:
    def __init__(self, values):
        self.values = list(values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Signals must be of equal length for addition.")
    
        combined_values = [a + b for a, b in zip(self.values, other.values)]
        return Signal(combined_values)

    def __str__(self):
        size = len(self.values)
        mean = sum(self.values) / size if size > 0 else 0.0
        return f"Signal(Size: {size}, Mean: {mean:.2f})"


# --- Sample Call Demonstration ---
if __name__ == "__main__":
    sig_a = Signal([1.0, 2.0, 3.0, 4.0])
    sig_b = Signal([0.5, 1.5, 2.5, 3.5])

    print(f"Length of sig_a: {len(sig_a)}")
    print(f"Sample at index 2: {sig_a[2]}")

    sig_c = sig_a + sig_b
    print(f"Result of addition: {sig_c.values}")
    print(sig_c)
    
# %%
class Student:
    pass

print(type(Student))

s1 = Student()

print(type(s1))
# %%
# MyMeta is a custom metaclass.
# MyMeta inherits from type.
# Student is created using MyMeta.
class MyMeta(type):
    pass

class Student(metaclass=MyMeta):
    pass
print(type(Student))
# %%

#mcs:Metaclass itself : ImmutableMeta
#name:Class ka naam:WireTransfer
#bases: parent: ()
#namespace:Class ke methods aur attributes (dictionary):set_amount, etc.
class ImmutableMeta(type):
    def __new__(mcs, name, bases, dct):
        # Iterate through the class dictionary to check for setter methods
        for key in dct:
            if key.startswith("set_"):
                raise TypeError(f"Setter methods like '{key}' are not allowed in immutable classes.")
        
        # Create and return the class if no setter methods are found
        return super().__new__(mcs, name, bases, dct)


try:
    class WireTransfer(metaclass=ImmutableMeta):
        def set_amount(self, val):  # This triggers the Metaclass error
            self.amount = val
except TypeError as e:
    print(f"Metaclass blocked class creation: {e}")
# %%
#past paper question
class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id

    def get_info(self):
        return self.device_id

class SmartLight(SmartDevice):
    def __init__(self, device_id, brightness):
        super().__init__(device_id)
        self.brightness = brightness

    def get_info(self):
        return f"{super().get_info()}, Brightness: {self.brightness}"

    # Dunder Methods
    # a. __lt__: Compare brightness
    def __lt__(self, other):
        return self.brightness >other.brightness

    # b. __add__: Sum brightness (capped at 100)
    def __add__(self, other):
        new_brightness = self.brightness + other.brightness
        if new_brightness > 100:
            new_brightness = 100
        return SmartLight("Combined", new_brightness)

    # c. __int__: Cast to integer
    def __int__(self):
        return self.brightness


