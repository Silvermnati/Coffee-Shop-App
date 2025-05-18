import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_init(self):
        c = Customer("Test")
        cof = Coffee("TestCoffee")
        o = Order(c, cof, 5.0)
        assert o.customer == c
        assert o.coffee == cof
        assert o.price == 5.0
    
    def test_price_validation(self):
        c = Customer("Test")
        cof = Coffee("TestCoffee")
        with pytest.raises(TypeError):
            Order(c, cof, "5.0")
        with pytest.raises(ValueError):
            Order(c, cof, 0.5)
        o = Order(c, cof, 5.0)
        with pytest.raises(AttributeError):
            o.price = 6.0
    
    def test_customer_validation(self):
        cof = Coffee("TestCoffee")
        with pytest.raises(TypeError):
            Order("Not a customer", cof, 5.0)
    
    def test_coffee_validation(self):
        c = Customer("Test")
        with pytest.raises(TypeError):
            Order(c, "Not a coffee", 5.0)