class DiscountCalculator:
    REGULAR_DISCOUNT = 0.10
    PREMIUM_DISCOUNT = 0.15
    VIP_DISCOUNT = 0.25

    def calculate(self, subtotal, user_type):
        if user_type == "regular":
            return subtotal - (subtotal * self.REGULAR_DISCOUNT)

        if user_type == "premium":
            return subtotal - (subtotal * self.PREMIUM_DISCOUNT)

        if user_type == "vip":
            return subtotal - (subtotal * self.VIP_DISCOUNT)

        return subtotal
