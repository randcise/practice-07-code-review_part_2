import json


class CartService:
    def __init__(self):
        self.items = []

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

            if user_type == "regular":
                subtotal = subtotal - (subtotal * 0.1)

            elif user_type == "premium":
                subtotal = subtotal - (subtotal * 0.15)

            elif user_type == "vip":
                subtotal = subtotal - (subtotal * 0.25)

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
