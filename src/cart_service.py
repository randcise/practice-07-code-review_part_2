import json

from src.discount_calculator import DiscountCalculator


class CartService:
    def __init__(self):
        self.items = []
        self.discount_calculator = DiscountCalculator()

    def add_item(self, name, price, quantity):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def calculate_total(self, user_type):
        total = 0

        for item in self.items:
            subtotal = item["price"] * item["quantity"]

            subtotal = self.discount_calculator.calculate(
                subtotal,
                user_type
            )

            total += subtotal

        return total

    def calculate_shipping(self):
        total_quantity = 0

        for item in self.items:
            total_quantity += item["quantity"]

        if total_quantity == 0:
            return 0

        if total_quantity < 5:
            return 10

        if total_quantity < 10:
            return 5

        return 0

    def save_cart(self):
        data = json.dumps(self.items)

        with open("cart.json", "w") as file:
            file.write(data)

    def load_cart(self):
        with open("cart.json", "r") as file:
            data = file.read()

        self.items = json.loads(data)

    def clear_cart(self):
        self.items = []