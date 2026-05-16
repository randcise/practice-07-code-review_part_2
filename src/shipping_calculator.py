class ShippingCalculator:
    def calculate(self, total_quantity):
        if total_quantity == 0:
            return 0

        if total_quantity < 5:
            return 10

        if total_quantity < 10:
            return 5

        return 0
