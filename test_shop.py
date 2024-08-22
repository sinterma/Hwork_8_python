import pytest



class TestProducts:
    def test_product_check_quantity(self, product):
        assert product.check_quantity(500) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1500) is False

    def test_product_buy(self, product):
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1500)

class TestCart:
    def test_add_product(self, cart, product):
        cart.add_product(product, 2)
        assert cart.products[product] == 2

    def test_remove_product(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert cart.products[product] == 1
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 2)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 2)
        assert cart.get_total_price() == 200

    def test_cart_buy(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 998
        assert len(cart.products) == 0

    def test_cart_buy_not_enough_product(self, cart, product):
        cart.add_product(product, 2000)
        with pytest.raises(ValueError):
            cart.buy()