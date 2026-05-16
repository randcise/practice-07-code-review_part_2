import json


class CartService:
    def __init__(self):
        self.items = []

def add_item(self, name, price, quantity):
    if price < 0 or quantity <= 0:
        return

    self.items.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })
def calculate_total(self, user_type):
    DISCOUNTS = {
        "regular": 0.1,
        "premium": 0.15,
        "vip": 0.25
    }

    total = 0

    for item in self.items:
        subtotal = item["price"] * item["quantity"]

        discount = DISCOUNTS.get(user_type, 0)
        subtotal = subtotal - (subtotal * discount)

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
    try:
        data = json.dumps(self.items)

        with open("cart.json", "w") as file:
            file.write(data)
    except Exception:
        pass
def load_cart(self):
    try:
        with open("cart.json", "r") as file:
            data = file.read()

        self.items = json.loads(data)
    except Exception:
        self.items = []
    def clear_cart(self):
        self.items = []
