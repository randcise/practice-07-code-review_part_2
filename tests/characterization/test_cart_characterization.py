from src.cart_service import CartService


def test_add_item():
    cart = CartService()

    cart.add_item("Phone", 100, 2)

    assert len(cart.items) == 1


def test_regular_discount():
    cart = CartService()

    cart.add_item("Phone", 100, 1)

    assert cart.calculate_total("regular") == 90


def test_premium_discount():
    cart = CartService()

    cart.add_item("Phone", 100, 1)

    assert cart.calculate_total("premium") == 85


def test_vip_discount():
    cart = CartService()

    cart.add_item("Phone", 100, 1)

    assert cart.calculate_total("vip") == 75


def test_without_discount():
    cart = CartService()

    cart.add_item("Phone", 100, 1)

    assert cart.calculate_total("unknown") == 100


def test_shipping_less_than_5():
    cart = CartService()

    cart.add_item("Phone", 100, 2)

    assert cart.calculate_shipping() == 10


def test_shipping_less_than_10():
    cart = CartService()

    cart.add_item("Phone", 100, 7)

    assert cart.calculate_shipping() == 5


def test_shipping_more_than_10():
    cart = CartService()

    cart.add_item("Phone", 100, 15)

    assert cart.calculate_shipping() == 0


def test_clear_cart():
    cart = CartService()

    cart.add_item("Phone", 100, 1)

    cart.clear_cart()

    assert len(cart.items) == 0


def test_multiple_items():
    cart = CartService()

    cart.add_item("Phone", 100, 1)
    cart.add_item("Laptop", 200, 1)

    assert cart.calculate_total("regular") == 270
