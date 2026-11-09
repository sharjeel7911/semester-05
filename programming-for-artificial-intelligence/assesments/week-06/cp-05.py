# %%
class Currency:
    def __init__(self, amount: float, code: str):
        self.amount = float(amount)
        self.code = str(code).upper()

    def __add__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        if self.code != other.code:
            raise ValueError(
                f"Cannot add currencies with different codes: {self.code} and {other.code}"
            )
        return Currency(self.amount + other.amount, self.code)

    def __repr__(self) -> str:
        return f"Currency(amount={self.amount}, code={self.code!r})"

    def __str__(self) -> str:
        return f"{self.code} {self.amount:,.2f}"


c1 = Currency(500, "USD")
c2 = Currency(300, "USD")
print(c1 + c2)
print(repr(c1))

# ====================================================================================================


# %%
class Component:
    def startup(self):
        print("Component Initialized")


class PowerDevice(Component):
    def startup(self):
        print("Power Grid Connected")
        super().startup()


class NetworkDevice(Component):
    def startup(self):
        print("Network Interface Ready")
        super().startup()


class SmartLift(PowerDevice, NetworkDevice):
    def startup(self):
        print("SmartLift Starting up...")
        super().startup()


lift = SmartLift()
lift.startup()
print(f"MRO Order: {[c.__name__ for c in SmartLift.mro()]}")


# ====================================================================================================

# %%
import math


class Product:
    def __init__(self, name: str, price: float, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.price = float(price)


class ShippingMixin:
    def __init__(self, weight: float = 0.0, **kwargs):
        super().__init__(**kwargs)
        self.weight = float(weight)

    def calculate_freight(self) -> float:
        increments = max(1, math.ceil(self.weight))
        return float(increments * 10)


class DiscountMixin:
    def apply_discount(self, percent: float):
        discount_amount = self.price * (percent / 100.0)
        self.price -= discount_amount
        return self.price


class Laptop(ShippingMixin, DiscountMixin, Product):
    def __init__(self, name: str, price: float, weight: float):
        super().__init__(name=name, price=price, weight=weight)


macbook = Laptop(name="Macbook Air", price=1200, weight=1.2)
print("Initial Price:", macbook.price)
macbook.apply_discount(10)
print("Discounted Price:", macbook.price)
print("Freight Cost:", macbook.calculate_freight())

# ====================================================================================================

# %%
from abc import ABC, abstractmethod


class PaymentProvider(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass

    @abstractmethod
    def settle(self) -> bool:
        pass


class CreditCardPay(PaymentProvider, ABC):
    def __init__(self, card_number: str, card_holder: str, expiry_date: str):
        self.card_number = str(card_number)
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.fee = 0.0
        self.amount = 0.0

    def __repr__(self) -> str:
        masked = f"****-****-****-{self.card_number[-4:]}"
        return f"{self.__class__.__name__}(Holder: {self.card_holder}, Card: {masked})"


class StripePay(PaymentProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.amount = 0.0
        self.fee = 0.0

    def authorize(self, amount: float) -> bool:
        self.fee = amount * 0.025
        self.amount = amount + self.fee
        print(
            f"[Stripe] Authorized: ${self.amount:.2f} (includes 2.5% fee: ${self.fee:.2f})"
        )
        return True

    def settle(self) -> bool:
        print(f"[Stripe] Settled ${self.amount:.2f} using key {self.api_key[:8]}...")
        return True


class VisaPay(CreditCardPay):
    def authorize(self, amount: float) -> bool:
        self.amount = amount
        print(f"[Visa] Authorized: PKR {self.amount:.2f}")
        return True

    def settle(self) -> bool:
        # 2.5% or 10.0 rupee, whichever is lower
        self.fee = min(self.amount * 0.025, 10.0)
        total = self.amount + self.fee
        print(f"[Visa] Settled: PKR {total:.2f} (Fee: PKR {self.fee:.2f})")
        return True


class UnionPay(CreditCardPay):
    def authorize(self, amount: float) -> bool:
        self.amount = amount
        print(f"[UnionPay] Authorized: PKR {self.amount:.2f}")
        return True

    def settle(self) -> bool:
        # Flat 8.0 fee
        self.fee = 8.0
        total = self.amount + self.fee
        print(f"[UnionPay] Settled: PKR {total:.2f} (Fee: PKR {self.fee:.2f})")
        return True


class RaastPay(CreditCardPay):
    def authorize(self, amount: float) -> bool:
        self.amount = amount
        print(f"[Raast] Authorized: PKR {self.amount:.2f}")
        return True

    def settle(self) -> bool:
        self.fee = 0.0
        print(f"[Raast] Settled: PKR {self.amount:.2f} (Zero fee)")
        return True


# Verification & ABC Validation
pay = StripePay(api_key="sk_test_123456789")
pay.authorize(50.0)
pay.settle()

try:

    class GenericPayment(PaymentProvider):
        def authorize(self, amount: float) -> bool:
            return True

        # Missing settle()

    broken = GenericPayment()
except TypeError as e:
    print(f"Validation success - blocked uninstantiated ABC: {e}")

# ====================================================================================================


# %%
class Signal:
    def __init__(self, values: list):
        self.values = [float(v) for v in values]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, index: int) -> float:
        return self.values[index]

    def __add__(self, other):
        if not isinstance(other, Signal):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError(
                "Signals must be of equal length for element-wise addition."
            )
        added = [a + b for a, b in zip(self.values, other.values)]
        return Signal(added)

    def __str__(self) -> str:
        size = len(self.values)
        mean = sum(self.values) / size if size > 0 else 0.0
        return f"Signal(Size: {size}, Mean: {mean:.2f})"


# Verification
sig_a = Signal([1.0, 2.0, 3.0, 4.0])
sig_b = Signal([0.5, 1.5, 2.5, 3.5])

print(f"Length of sig_a: {len(sig_a)}")
print(f"Sample at index 2: {sig_a[2]}")
sig_c = sig_a + sig_b
print(f"Result of addition: {sig_c.values}")
print(sig_c)

# ====================================================================================================


# %%
class ImmutableMeta(type):
    def __new__(mcs, name, bases, namespace):
        for attr_name, attr_val in namespace.items():
            if callable(attr_val) and attr_name.startswith("set"):
                raise TypeError(
                    f"Modification method '{attr_name}' is forbidden on immutable class '{name}'."
                )
        return super().__new__(mcs, name, bases, namespace)


# Verification
try:

    class WireTransfer(metaclass=ImmutableMeta):
        def set_amount(self, val):  # Triggers Metaclass error
            self.amount = val
except TypeError as e:
    print(f"Metaclass blocked class creation: {e}")
